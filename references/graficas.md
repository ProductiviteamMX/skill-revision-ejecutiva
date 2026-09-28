# Gráficas

El color va al final. Primero la forma, después el énfasis y al último los colores.

## 1. Elegir la forma por el trabajo del dato

| Trabajo | Forma |
|---|---|
| Un número que lo dice todo | Cifra grande (stat tile), no una gráfica |
| Cambio en el tiempo | Línea |
| Comparar categorías | Barras con base en cero |
| Brecha contra una referencia | Línea más una línea de referencia punteada, rotulada directo |
| Sensibilidad de dos variables | Tabla o mapa de calor de un solo tono |
| Parte de un todo con 2 a 5 partes | Barra apilada o cifras; nunca una dona para comparar valores cercanos |

## 2. Reglas de énfasis

- **Resalta lo que prueba el título y deja el resto en gris.** Si el título dice "diciembre sube 14%", diciembre (y los meses vecinos del pico) va en color; los demás meses, en gris claro.
- **Etiquetas solo donde importan.** Nunca un número en cada punto. Rotula el pico, el valor de hoy y los extremos.
- **Rotulado directo** en lugar de leyenda cuando hay 1 o 2 series. Para 2 o más series, además, una leyenda con muestra de color y texto en tinta.
- **Un solo eje Y.** Nunca doble eje. Si hay dos medidas de distinta escala, van en dos gráficas.
- Rejilla y ejes en gris claro. Sin sombras, 3D ni degradados.
- Etiquetas de categoría legibles: si son muchas (por ejemplo 52 semanas), rotula solo el primer punto de cada mes.
- Si el orden importa (secuencial), un solo tono de claro a oscuro. Para polaridad, dos tonos opuestos con un gris neutro al centro.
- En un mapa de calor, marca con borde la celda de "hoy" en el color de alerta, y las celdas que cumplen la condición en el color de acento.

## 3. Validar la paleta, sin adivinar

- Contraste de texto y marcas contra el fondo: `scripts/contraste.py "#008C9C,#ED5F18" --fondo "#FBFAF6"`. Mínimo 3:1 para marcas y 4.5:1 para texto normal.
- Si tienes disponible la skill `dataviz` (viene con Claude Code), corre su `validate_palette.js`: revisa la banda de luminosidad, la saturación mínima, la separación para daltonismo (ΔE de 8 o más entre series vecinas) y el contraste. El gris de énfasis puede fallar la saturación a propósito: es el patrón de "resaltar uno y dejar gris el resto".
- La identidad nunca depende solo del color: rotula, o usa textura o forma.

## 4. Notas y fuentes

- Cada gráfica con datos supuestos lleva al pie de dónde salen los datos y qué es supuesto.
- Si la gráfica sale de un modelo, cita el archivo ("Detalle en Modelo_Capacity.xlsx").
- El título de la lámina dice la conclusión; el rótulo de la gráfica solo dice qué se mide ("Agentes FTE por semana").
