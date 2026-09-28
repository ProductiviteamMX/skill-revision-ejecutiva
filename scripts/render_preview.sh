#!/bin/sh
# Renderiza un pptx o docx a PNGs y hojas de contacto 2x2 para revisarlos visualmente.
# Uso: render_preview.sh archivo.pptx|docx [carpeta_salida] [dpi]
# Requiere LibreOffice (soffice) y python con pymupdf y pillow.
# Variables opcionales: SOFFICE (ruta a soffice o a un wrapper), PYTHON (intérprete con las librerías).
set -e
f="$1"; out="${2:-./render}"; dpi="${3:-60}"
[ -z "$f" ] && { echo "Uso: $0 archivo.pptx|docx [salida] [dpi]"; exit 1; }
SOFFICE="${SOFFICE:-$(command -v soffice || command -v libreoffice || true)}"
PYTHON="${PYTHON:-python3}"
[ -z "$SOFFICE" ] && { echo "No encuentro LibreOffice. Instálalo o define SOFFICE (ver references/visual.md)."; exit 1; }
mkdir -p "$out"
b=$(basename "${f%.*}")
"$SOFFICE" --headless --convert-to pdf --outdir "$out" "$f" >/dev/null 2>&1 || true
if [ ! -f "$out/$b.pdf" ]; then  # la primera corrida de un perfil nuevo sale con código 81
  "$SOFFICE" --headless --convert-to pdf --outdir "$out" "$f" >/dev/null 2>&1 || true
fi
[ -f "$out/$b.pdf" ] || { echo "La conversión falló"; exit 1; }
"$PYTHON" - "$out/$b.pdf" "$out" "$dpi" <<'PY'
import sys
import pymupdf
from PIL import Image
pdf, out, dpi = sys.argv[1], sys.argv[2], int(sys.argv[3])
doc = pymupdf.open(pdf)
imgs = []
for i, p in enumerate(doc):
    fn = f"{out}/p-{i + 1:02d}.png"
    p.get_pixmap(dpi=dpi).save(fn)
    imgs.append(Image.open(fn))
w, h = imgs[0].size
for k in range(0, len(imgs), 4):
    hoja = Image.new("RGB", (w * 2 + 10, h * 2 + 10), "white")
    for j, im in enumerate(imgs[k:k + 4]):
        hoja.paste(im, ((j % 2) * (w + 10), (j // 2) * (h + 10)))
    hoja.save(f"{out}/sheet-{k // 4 + 1}.png")
print(f"{len(imgs)} páginas -> {out}/p-*.png y {out}/sheet-*.png")
PY
