---
name: revision-ejecutiva
description: Crea y revisa documentos ejecutivos (decks, memos, propuestas, case studies, business cases) con estándar de consultoría. Cubre la historia (SCQA, pirámide, respuesta primero), los títulos de acción, la escritura sin tics de IA, el sistema visual a partir de la marca, las gráficas con énfasis, la consistencia numérica entre archivos y las rondas de revisión con agentes (corrector, abogado del diablo, lector en frío). Úsala cuando pidan armar, mejorar, "hacer más profesional", revisar o validar una presentación o un documento para un directivo, un cliente o una entrevista, o cuando digan "que no parezca hecho por IA", "action titles", "storytelling" o "que se entienda".
---

# Revisión ejecutiva

Un documento ejecutivo se lee en frío, sin que el autor lo presente. Tiene que sostenerse solo: la conclusión arriba, cada afirmación probada y ninguna cifra que contradiga a otra. Esta skill convierte eso en un proceso con puertas de control.

## Principios que no se negocian

1. **La voz es del autor.** Tú estructuras, investigas y revisas. No inventas anécdotas, cifras ni logros. Si falta un dato, dejas `[DATO PENDIENTE: ...]` y preguntas.
2. **Respuesta primero.** El resumen ejecutivo va al inicio y dice la recomendación. Ver `references/storytelling.md`.
3. **Cada título es un título de acción:** una oración con la conclusión de la lámina, con cifras cuando se pueda. Leídos en orden, los títulos cuentan la historia completa.
4. **Supuestos a la vista.** Todo número que no venga de una fuente se marca como supuesto y dice por qué se eligió.
5. **Una fuente de verdad para las cifras.** Si hay un modelo (Excel o script), el memo y el deck salen de ahí. Nunca se escriben cifras a mano en dos lugares.
6. **Mirar antes de entregar.** Siempre se renderiza a imagen y se revisa. El texto correcto no garantiza una lámina correcta.

## Flujo

Sigue las fases en orden. Cada una tiene su referencia y su puerta de control; no avances con la puerta abierta.

| Fase | Qué haces | Referencia | Puerta de control |
|---|---|---|---|
| 1. Brief | Audiencia, decisión que se pide, formato, extensión, fecha. Qué dijo exactamente quien pidió el documento | — | El pedido literal está copiado y respondido punto por punto |
| 2. Material del autor | Entrevista breve al autor: su experiencia, sus criterios y sus pruebas. Un mapa de evidencia (cada pilar del plan con su prueba) | `references/storytelling.md` | Ningún pilar sin prueba o sin marca de hipótesis |
| 3. Esqueleto | Ghost deck: solo títulos de acción en orden SCQA. Se valida leyendo los títulos en voz alta | `references/storytelling.md` | Los títulos solos cuentan la historia |
| 4. Redacción | Cuerpo que prueba cada título, con las reglas de escritura | `references/escritura.md` | `scripts/lint_texto.py` sin hallazgos graves |
| 5. Diseño | Sistema visual desde la marca del destinatario o del autor, y gráficas con énfasis | `references/visual.md`, `references/graficas.md` | Render revisado: sin solapes, cortes ni tarjetas de plantilla |
| 6. Revisiones | Tres rondas con agentes independientes (el autor no ve sus propios tics) | `references/revisiones.md` | Hallazgos aplicados o descartados con razón |
| 7. Consistencia | Las cifras, fechas y términos coinciden entre deck, memo y modelo | `scripts/consistencia.py` | Cero diferencias sin explicar |
| 8. Entrega | Lista final y cambios explicados al usuario | `references/checklist.md` | Todo el checklist en verde |

## Herramientas incluidas

- `scripts/render_preview.sh archivo.pptx|docx [salida]`: convierte a PDF con LibreOffice y genera PNGs y hojas de contacto de 2×2 para revisar con Read.
- `scripts/lint_texto.py archivo [...]`: busca tics de IA, muletillas, rayas, tríadas sospechosas y contrastes falsos en pptx, docx, md o txt.
- `scripts/consistencia.py a.pptx b.docx [--claves "40;49;16 de noviembre"]` (claves separadas por punto y coma): extrae las cifras de cada archivo, muestra las que aparecen solo en uno y verifica las claves.
- `scripts/contraste.py "#hex1,#hex2" --fondo "#FFFFFF"`: contraste WCAG entre colores y el fondo.
- `scripts/extraer_texto.py archivo.pptx`: vuelca el texto por lámina para las revisiones con agentes.

Dependencias: `python-pptx`, `python-docx`, `pymupdf`, `pillow` y LibreOffice (`soffice`). Si no hay LibreOffice ni sudo, ver la nota de instalación en `references/visual.md`.

## Cuándo preguntar al usuario

Pregunta solo lo que cambia el resultado: quién decide, qué se le pide, qué experiencia propia sostiene la propuesta, qué datos son confidenciales. Todo lo demás se resuelve con un supuesto explícito.

## Qué no hacer

- Un documento largo cuando se pidió un "breve esquema". Si el contenido crece, el deck es la versión corta y el memo el respaldo.
- Adornos de plantilla: etiquetas en mayúsculas sobre cada título, tarjetas con sombra en todas las láminas, círculos decorativos, íconos de puntos de color.
- Nombrar empleadores o datos confidenciales del autor sin su permiso explícito.
- Declarar "listo" sin haber visto el render.
