# Rondas de revisión con agentes

Quien escribe no ve sus propios tics ni sus huecos. Lanza agentes nuevos, sin el contexto de la redacción, para cada ronda. Pásales el texto extraído (`scripts/extraer_texto.py`), los renders y las guías. Pídeles que no editen archivos y que entreguen tablas de "original → propuesta".

Aplica lo que mejora el documento. Descarta con razón lo que contradice una decisión del usuario o reescribe sus frases propias, y díselo al usuario.

## Ronda 1: corrector de estilo

```
Eres corrector de estilo. Busca todo lo que suene escrito por IA en este documento de <autor> para <lector>.
Lee primero <ruta>/references/escritura.md.
Texto: <ruta al texto extraído>.
Revisa frase por frase, incluidos los títulos y las celdas de las tablas: tríadas, contrastes falsos, títulos-eslogan,
meta-comentarios, aforismos, paralelismos, voz pasiva donde actúa el autor, muletillas, términos inconsistentes
(el mismo concepto dicho de dos formas) y términos de industria que deberían ir en inglés (o sobran).
No cambies cifras ni el mensaje. No agregues contenido. No edites archivos.
Entrega una tabla: ubicación | texto original | problema | propuesta lista para pegar. Máximo 30 filas, por gravedad.
```

## Ronda 2: abogado del diablo (el destinatario)

```
Actúa como <cargo del destinatario> de <empresa>. Le pediste a <autor> esto: "<pedido literal>".
Datos que tú le diste: <lista>.
Lee el documento (<ruta>) y el modelo si existe (<ruta>); córrelo si puedes.
Entrega: 1) tu reacción en 3 líneas (¿pasa a la siguiente etapa?), 2) los 5 huecos más serios, cada uno con su corrección,
3) las 8 preguntas más difíciles que harías, cada una con una pista de respuesta, 4) errores factuales, de cálculo o de
consistencia, 5) qué quitarías. Sin adular. No edites archivos.
```

Lo que suele encontrar:

- Un modelo que contradice la realidad del lector ("tu modelo dice 111 y yo opero con 25").
- Un tono que incomoda a otro equipo, por ejemplo cuando se audita al bot que otro construyó.
- La falta de metas numéricas.
- Pedir presupuesto cuando el lector dijo que no hay.
- Calendarios que no cierran.

## Ronda 3: lector en frío

```
Eres <destinatario> y lees el documento en frío, sin que el autor te lo presente.
Material: texto por lámina (<ruta>) y renders (<ruta>/hd-*.png); míralos todos.
Para cada lámina: 1) el mensaje que entendiste, en una línea, 2) qué frase, cifra o elemento visual no se entiende
(cita exacta), 3) si hay un salto lógico respecto de la lámina anterior, 4) una propuesta concreta.
Pon atención especial en <lámina que el usuario dijo que no se entiende>.
Cierra con los 5 problemas de claridad más importantes. No edites archivos.
```

Esta ronda encuentra lo que las otras dos no ven:

- Un cierre que mezcla lo necesario, las decisiones y los riesgos.
- Términos sin definir.
- Una cifra que en una lámina es dato y en otra es supuesto.
- Metas que cambian entre láminas.

## Ronda opcional: dirección de arte

```
Eres director de arte. Lee <ruta>/references/visual.md y graficas.md (y las skills de diseño que haya disponibles).
Mira los renders <ruta>/hd-*.png y el código que los genera (<ruta>), sin editarlo.
Entrega: veredicto en 3 líneas (¿profesional o de plantilla?, ¿qué lo delata?), los 10 cambios visuales de mayor impacto
en términos de código (posición, tamaño, color, forma), frases con tono de IA y los riesgos al convertir a Google Slides.
```

## Después de cada ronda

1. Aplica los cambios.
2. Vuelve a renderizar y mira.
3. Corre `scripts/consistencia.py` si hay más de un archivo.
4. Cuéntale al usuario qué aplicaste, qué descartaste y por qué, y qué supuestos nuevos agregaste para que los valide.
