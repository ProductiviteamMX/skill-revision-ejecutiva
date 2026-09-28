# Escritura sin tics de IA

El texto tiene que sonar a una persona concreta con criterio. Cada regla abajo viene de errores reales que delatan un texto generado.

## Lista negra de estructuras

| Patrón | Ejemplo | Qué hacer |
|---|---|---|
| Contraste falso | "No es X, es Y"; "no solo X, sino Y"; "más que X, es Y"; "X, no cuando Y" | Afirma Y directo. Máximo uno por documento |
| Tríada automática | "rápido, claro y medible"; "resuelve a la primera, rápido y aprende" | Usa el número real de elementos o quédate con uno |
| Título-eslogan | "Cada hallazgo tiene dueño, acción, plazo y verificación" | Título informativo o de acción con dato |
| Revelación armada | "¿El resultado? ..."; "La clave: ..."; "es otra cosa: ..." | Di el resultado en la frase |
| Meta-comentario | "En la tabla está...", "Esta es la ruta que uso:", "donde no existe, lo digo" | Borra; el contenido se explica solo |
| Frase redonda / aforismo | "Cada recontacto es un cliente sin resolver" | Frase concreta: "Si el cliente vuelve a escribir, su problema sigue abierto" |
| Paralelismo o anáfora | "Para X... Para Y..."; "Con... Con..."; "hoy... mañana..." | Varía la estructura |
| Cierre moralizante o resumen | "En conclusión...", "Recuerda que..." | Termina en una acción concreta |
| Apertura genérica | "En el entorno actual...", "Hoy más que nunca..." | Empieza con el dato o el hallazgo |
| Personificación | "El cálculo todavía no ve...", "el promedio esconde dónde sufre" | Di quién hace qué |
| Voz pasiva donde actúa el autor | "Las metas se fijan", "se presenta" | "Las fijamos", "lo presento" |

## Vocabulario a evitar

- ES: crucial, fundamental, clave (salvo en "indicador clave"), potenciar, impulsar, optimizar (salvo el sentido técnico), sinergia, robusto, integral, holístico, ecosistema, panorama, "juega un papel", "desempeña un rol", "cabe destacar", "es importante señalar", "sin duda", "en resumen", "en conclusión", "de vanguardia", transformar, excelencia (sin prueba), innovador.
- EN: delve, leverage, unlock, elevate, empower, streamline, seamless, robust, pivotal, game-changer, cutting-edge.
- Muletillas: "por experiencia" (si no agrega), "seguramente", "casi todo", "además de eso", "a propósito", "básicamente", "de alguna manera".

## Formato

- Pocas rayas (—). Usa comas, puntos o paréntesis.
- Sin negrita al inicio de cada viñeta. Como máximo una negrita por sección.
- Sin emojis, flechas decorativas ni signos de admiración.
- Siglas explicadas la primera vez: FCR (First Contact Resolution).
- Números con el formato del país (1,200 o 1.200) y consistentes en todo el documento.

## Términos de industria en inglés

Muchos equipos usan el término en inglés como estándar. Define con el usuario la lista y aplícala **de forma consistente**:

- Usar el inglés cuando es el estándar del oficio: baseline, forecast, headcount, FTE, AHT, FCR, CSAT, NPS, QA, WFM, shrinkage, service level, backlog, dashboard, stakeholders, customer journey, touchpoints, quick wins, handoff, OJT, go live, microlearning, people management, skills map, roadmap, capacity.
- Dejar el español cuando es lo normal en la región: agente, supervisor, escalamiento, tipificación, capacitación (si el usuario no pidió "training").
- Nunca decir el mismo concepto de dos formas en el mismo documento ("espera hasta un agente" y "FRT").

## Voz del autor

- Primera persona y presente: "mido", "lidero", "decido".
- El autor que entra a un cargo habla como quien ya lo ejerce, no como consultor externo que pide permiso.
- Respeta el grado de certeza del autor. Si dijo "creo", no lo conviertas en "está demostrado".
- Las frases que el autor escribió de su puño se conservan. Solo se corrigen ortografía y ambigüedad, y se le avisa.

## Pasadas de corrección (texto largo)

Una cosa por pasada: 1) claridad, 2) voz, 3) "¿y qué?" (cada afirmación dice por qué le importa al lector), 4) prueba (cada cifra tiene fuente o está marcada como supuesto), 5) concreción, 6) lista negra y forma, 7) cierre con acción.

Ejecuta `scripts/lint_texto.py` al final. El script no sustituye la lectura: detecta patrones, pero no el tono.
