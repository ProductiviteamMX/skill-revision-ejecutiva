#!/usr/bin/env python3
"""Compara las cifras entre dos o más archivos (pptx, docx, md, txt).

Uso:
  consistencia.py deck.pptx memo.docx
  consistencia.py deck.pptx memo.docx --claves "40;49;16 de noviembre;USD 500;430,000"

Muestra las cifras que aparecen en un archivo y no en los otros (candidatas a inconsistencia)
y verifica que cada clave esté en todos. Ignora años, números de página y números de un dígito.
"""
import re
import sys

from extraer_texto import extraer

NUM = re.compile(r"(?<![\w.])[-−~]?\d{1,3}(?:[,.]\d{3})+(?:\.\d+)?%?|(?<![\w.])[-−~]?\d+(?:\.\d+)?%?")


def normalizar(n):
    n = n.replace("−", "-").lstrip("~")
    return n.replace(",", "") if re.fullmatch(r"-?\d{1,3}(,\d{3})+(\.\d+)?%?", n) else n


def cifras(texto):
    out = set()
    for m in NUM.finditer(texto):
        n = normalizar(m.group())
        base = n.rstrip("%").lstrip("-")
        try:
            v = float(base)
        except ValueError:
            continue
        if v < 10 and "%" not in n and "." not in base:
            continue  # números de un dígito: demasiado ruido
        if 1990 <= v <= 2100 and "%" not in n:
            continue  # años
        out.add(n)
    return out


if __name__ == "__main__":
    args = sys.argv[1:]
    claves = []
    if "--claves" in args:
        i = args.index("--claves")
        claves = [c.strip() for c in args[i + 1].split(";") if c.strip()]
        args = args[:i] + args[i + 2:]
    if len(args) < 2 and not claves:
        sys.exit(__doc__)
    textos = {a: extraer(a) for a in args}
    conj = {a: cifras(t) for a, t in textos.items()}
    ok = True
    if len(args) > 1:
        for a in args:
            otros = set().union(*(conj[b] for b in args if b != a))
            solo = sorted(conj[a] - otros, key=lambda x: float(x.rstrip("%").lstrip("-")))
            print(f"\n## Cifras solo en {a} ({len(solo)}):")
            print(", ".join(solo) if solo else "(ninguna)")
    if claves:
        print("\n## Claves")
        for c in claves:
            estado = {a: (c in t or c.replace(",", "") in t.replace(",", "")) for a, t in textos.items()}
            marca = "OK " if all(estado.values()) else "FALTA"
            ok &= all(estado.values())
            print(f"[{marca}] {c}: " + ", ".join(f"{a.split('/')[-1]}={'sí' if v else 'no'}" for a, v in estado.items()))
    print("\nRevisa a mano las cifras 'solo en': pueden ser detalle legítimo o una contradicción.")
    sys.exit(0 if ok else 1)
