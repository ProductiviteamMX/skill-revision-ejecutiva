#!/usr/bin/env python3
"""Detecta tics de escritura de IA en pptx, docx, md o txt.

Uso: lint_texto.py archivo [archivo ...] [--extra "palabra1,palabra2"]
Reporta cada hallazgo con contexto. No sustituye la lectura: detecta patrones, no tono.
"""
import re
import sys

from extraer_texto import extraer

GRAVE = {
    "contraste falso": r"\bno es [^.;:]{1,40}, es\b|\bno solo\b[^.]{0,60}\bsino\b|\bmás que [^.]{1,30}, es\b|, no cuando\b",
    "revelación armada": r"¿(El|La|Los|Las) [a-záéíóúñ ]{1,20}\?|\b(La clave|El truco|Spoiler)\s*:",
    "meta-comentario": r"\ben la tabla (está|se ve)|\besta es la (ruta|forma|lista) que|\bcomo se ve (arriba|abajo)|\bdonde no existe, lo digo",
    "muletilla": r"\b(es importante (destacar|señalar|mencionar)|cabe (destacar|mencionar)|sin (lugar a )?duda|en resumen|en conclusión|dicho esto|vale la pena señalar)\b",
    "vocabulario inflado": r"\b(crucial|fundamental|potenciar|impulsar|sinergia|robust[oa]|holístic[oa]|ecosistema|de vanguardia|juega un papel|desempeña un rol|transformaci[oó]n digital)\b",
    "vocabulario inflado (EN)": r"\b(delve|leverage|unlock|elevate|empower|streamline|seamless|pivotal|game-changer|cutting-edge)\b",
}
AVISO = {
    "raya": r"—",
    "admiración o emoji": r"[!¡]|[\U0001F300-\U0001FAFF]",
    "tríada posible": r"\b\w+(?:mente)?, \w+(?:mente)? y \w+(?:mente)?\b",
    "voz pasiva con 'se'": r"\bse (fijan|presenta|definen|realiza|lleva a cabo|pueden (leer|medir))\b",
    "relleno": r"\b(básicamente|simplemente|de alguna manera|además de eso|a propósito|casi todo)\b",
    "optimizar/clave (revisar uso)": r"\b(optimiz\w+|clave)\b",
}


def revisar(texto, extra=None):
    hallazgos = []
    reglas = [(k, v, "GRAVE") for k, v in GRAVE.items()] + [(k, v, "aviso") for k, v in AVISO.items()]
    if extra:
        reglas.append(("lista del usuario", r"\b(" + "|".join(map(re.escape, extra)) + r")\b", "GRAVE"))
    for linea_n, linea in enumerate(texto.splitlines(), 1):
        for nombre, patron, nivel in reglas:
            for m in re.finditer(patron, linea, flags=re.IGNORECASE):
                ini, fin = max(0, m.start() - 45), min(len(linea), m.end() + 45)
                hallazgos.append((nivel, nombre, linea_n, linea[ini:fin].strip()))
    return hallazgos


if __name__ == "__main__":
    args = sys.argv[1:]
    extra = None
    if "--extra" in args:
        i = args.index("--extra")
        extra = [p.strip() for p in args[i + 1].split(",") if p.strip()]
        args = args[:i] + args[i + 2:]
    if not args:
        sys.exit(__doc__)
    total_graves = 0
    for ruta in args:
        h = revisar(extraer(ruta), extra)
        graves = [x for x in h if x[0] == "GRAVE"]
        total_graves += len(graves)
        print(f"\n## {ruta}: {len(graves)} graves, {len(h) - len(graves)} avisos")
        for nivel, nombre, n, ctx in sorted(h, key=lambda x: (x[0] != "GRAVE", x[2])):
            print(f"[{nivel}] {nombre} (línea {n}): …{ctx}…")
    sys.exit(1 if total_graves else 0)
