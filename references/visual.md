# Sistema visual

## 1. Partir de la marca, no de una plantilla

Si el documento va para una empresa, busca su identidad real antes de diseñar:

- El sitio oficial suele cargar un archivo de tokens o CSS con variables de color y `@font-face`. Busca "tokens.css", `--color`, `theme-color` y la fuente del logo.
- Anota el origen de cada hex. Lo que deduzcas de una imagen se marca como inferido.
- Si la fuente de la marca es propietaria y el deck va a Google Slides, usa la más cercana de Google Fonts y dilo.

Define los roles antes de usar los colores:

| Rol | Uso | Regla |
|---|---|---|
| Fondo dominante | ~70% de las láminas | Claro y cálido o neutro |
| Primario oscuro | Láminas de tensión o cierre, bloques de énfasis | 3 o 4 láminas oscuras intercaladas para dar ritmo |
| Acento de marca | Cifras clave, datos, barra de progreso | Un solo acento para datos |
| Color de alerta | Solo lo que es riesgo, tensión o urgencia | Nunca como color de categoría |
| Tinta y gris | Texto y elementos secundarios | El texto nunca va en el color de una serie de datos |

## 2. Lo que delata una plantilla hecha por IA

- Una etiqueta en mayúsculas sobre cada título.
- Tarjetas blancas redondeadas con sombra en casi todas las láminas.
- Diez láminas claras seguidas con la misma estructura.
- Círculos decorativos concéntricos en la portada.
- Puntos de color en lugar de íconos.
- El color de alerta usado como categoría ("Negocio" en naranja).
- Un pie de lámina con "Autor · Título · 03 / 15" en todas.

Alternativas: reglas finas en lugar de tarjetas, cifras grandes sueltas, una barra de progreso por sección, la portada con el dato del caso (por ejemplo, una barra 80/20) y el número de página solo.

## 3. Retícula y tipografía

- Lámina de 13.333 × 7.5 in con márgenes laterales de 0.7 in. Todo alineado a esa retícula.
- Título de 26 a 28 pt, a lo ancho de la lámina. Si pasa de unos 70 caracteres ocupa dos líneas, y el subtítulo y el contenido bajan.
- Cuerpo de 11.5 a 14 pt. No bajes de 10 pt salvo en las fuentes y notas al pie.
- Tipografía de títulos sin negrita forzada si solo tiene un peso: Google Slides la engruesa artificialmente.
- Interlineado de 1.0 en títulos grandes con tildes. Con menos se cortan los acentos.
- Viñetas reales (buChar) con sangría colgante, no "•" escrito a mano.

## 4. Compatibilidad con Google Slides (desde python-pptx)

- Quita el `p:style` de cada forma. `shadow.inherit = False` no alcanza: las sombras del tema reaparecen.
- Las gráficas nativas pueden importarse como imagen; define la fuente de la gráfica (`chart.font.name`).
- Deja 10% a 15% de holgura vertical en las cajas de texto: al cambiar de fuente el texto crece.
- Evita formas fuera del lienzo. Se ven en el editor.
- Algunos glifos ("→") pueden no existir en la fuente de títulos. Ponlos en la fuente del cuerpo.

## 5. Renderizar y mirar

Siempre se revisa en imagen antes de entregar:

```bash
scripts/render_preview.sh deck.pptx /tmp/render
```

Luego lee las hojas de contacto (`sheet-*.png`) y busca:

- Texto que se sale de su caja o se encima con otro (títulos de dos líneas sobre el subtítulo, es lo más común).
- Cifras que se parten en dos líneas.
- Etiquetas de eje amontonadas.
- Numeración de página que no coincide.
- Colores fuera de su rol.

### LibreOffice sin sudo (Linux)

Si no hay `soffice` ni permisos de administrador:

1. Descarga el AppImage de LibreOffice y extráelo con `--appimage-extract`.
2. Baja las librerías que falten con `apt-get download <paquete>`, que no pide sudo, y extráelas con `dpkg-deb -x` en una carpeta local.
3. Arma un `fonts.conf` que apunte a esa carpeta y a `~/.local/share/fonts`.
4. Corre `soffice.bin --headless` con `LD_LIBRARY_PATH`, `FONTCONFIG_FILE` y `SAL_USE_VCLPLUGIN=svp`.
5. La primera corrida termina con el código 81 al crear el perfil. Repítela.
