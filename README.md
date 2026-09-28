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

## Usarla en Claude.ai, sin Claude Code

Funciona en la web y en la app de escritorio de Claude, en planes Pro, Max, Team o Enterprise:

1. Descarga el ZIP del repositorio: botón verde **Code** y luego **Download ZIP**. Descomprímelo y vuelve a comprimir solo la carpeta de la skill, de modo que `SKILL.md` quede dentro de una carpeta, por ejemplo `revision-ejecutiva/SKILL.md`.
2. En Claude.ai ve a **Settings → Capabilities** y activa **Code execution and file creation**.
3. En la misma pantalla, en **Skills**, elige **Upload skill** y sube el ZIP.
4. En cualquier conversación, pide algo como "Usa revision-ejecutiva para revisar este deck" y adjunta el archivo.

Diferencias con Claude Code:
- Claude.ai no lanza agentes en paralelo. Las rondas de revisión se hacen una tras otra en el mismo chat, o mejor en chats nuevos pegando los prompts de `references/revisiones.md`.
- El render a imagen depende de que el entorno tenga LibreOffice. Si no lo tiene, revisa las láminas con capturas.

Sin ninguna versión de Claude, `references/` sirve como guía manual, y `checklist.md` como la lista final.

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
