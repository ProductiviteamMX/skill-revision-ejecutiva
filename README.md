# revision-ejecutiva

Skill para Claude Code (también sirve como guía manual). Sirve para crear y revisar decks, memos y propuestas ejecutivas con estándar de consultoría:
- historia en SCQA con títulos de acción;
- escritura sin tics de IA;
- sistema visual a partir de la marca;
- gráficas con énfasis;
- consistencia numérica entre archivos;
- rondas de revisión con agentes.

## Instalación

Opción rápida, con git:
```
git clone https://github.com/ProductiviteamMX/skill-revision-ejecutiva.git ~/.claude/skills/revision-ejecutiva
```

Opción manual:

1. Descomprime la carpeta `revision-ejecutiva` en una de estas rutas:
   - `~/.claude/skills/` para tu usuario.
   - `.claude/skills/` dentro de un proyecto.
2. Reinicia Claude Code.
3. Úsala escribiendo `/revision-ejecutiva`, o pide algo como "revisa este deck para un directivo".

Dependencias de los scripts:
```
pip install python-pptx python-docx pymupdf pillow
```
También necesitas LibreOffice (`soffice`) para el render. Si no tienes sudo, lee la nota de `references/visual.md`.

## Contenido

- `SKILL.md`: flujo en 8 fases con puertas de control.
- `references/`: storytelling y títulos de acción, escritura, sistema visual, gráficas, plantillas para los agentes de revisión y checklist de entrega.
- `scripts/`:
  - `render_preview.sh`: genera PNG y hojas de contacto.
  - `lint_texto.py`: detecta tics de IA.
  - `consistencia.py`: compara las cifras entre archivos.
  - `contraste.py`: calcula el contraste WCAG.
  - `extraer_texto.py`: vuelca el texto de pptx y docx.

## Uso rápido de los scripts

```
python scripts/lint_texto.py deck.pptx memo.docx
python scripts/consistencia.py deck.pptx memo.docx --claves "40;16 de noviembre;USD 500"
python scripts/contraste.py "#0C1947,#00BBCE" --fondo "#FFFFFF"
SOFFICE=soffice ./scripts/render_preview.sh deck.pptx ./render
```
