# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: deepseek

**Prompt usado**:
1er prompt: Necesito trabajar con el siguiente trabajo práctico. Aún no abrí el repositorio de git, pero necesito que lo vayas analizando porque voy a necesitar ayuda con el paso a paso. En breve te haré las consultas necesarias y te solicitaré una guía, además de adjuntarte los datos con los que contamos en el repositorio" (adjunté el pdf del tp2)
2do: pegué el readme
3ro: adjunté una imagen con todo el repositorio y le solicité "qué necesitarías que te copie del repositorio, para que puedas analizar bien las actividades?" a continuación, pegué toda la info que me solicitó
4to:"vayamos analizando uno por uno cada módulo, porque todavía no pude ver Python y me gustaría ir entendiendo cuáles y por qué fueron los cambios realizados. Hagamos el primero, con una explicación breve y concisa de lo solicitado. Si tengo alguna duda te iré consultando antes de hacer el siguiente. también te pido que no confirmes todo lo que digo sin antes analizarlo y, en caso de confundirme, me lo hagas saber así puedo aprenderlo mejor"
> 

**Resultado obtenido**:

analizamos cada una de las funciones, aunque estando tan corto de tiempo (por la hora límite para la entrega) no llegué a ver todo en detalle.
Para cada función me arrojaba dos opciones de código: una simplificada y otra para realizar las operaciones de forma manual (me quedé con la simple para todos los casos) y aproveché para hacer algunas consultas en relación a las explicaciones que me daba

**¿Lo usaste tal cual o lo modificaste?**
no modifiqué nada del código propuesto

---

### 2 - condicionales.py

**Herramienta**: deepseek

**Prompt usado**:(en este punto tuve un problema con pip, así que primero le pegué el error para que me indique cómo solucionarlo)
perfecto, ya pude hacer lo de pip, completé las funciones en variables.py e hice el primer commit. Los test pasaron bien
 Sigamos con el siguiente. Necesito que sigamos el mismo patrón de análisis que el caso anterior, ahora para el siguiente módulo
> 

**Resultado obtenido**:

analizamos cada función, aunque sin proponer variables para cada caso, sino explicando en detalle cada parte del código y planteando posibles preguntas en relación al mismo. 

**¿Lo usaste tal cual o lo modificaste?**

los usé tal cual


---

### 3 - listas.py

**Herramienta**: deepseek

**Prompt usado**:(en este punto, no agregué ningún nuevo prompt e hice lo mismo para los siguientes casos, ya que mantuvimos el mismo formato anterior)

"vamos con el siguiente módulo"
> 

**Resultado obtenido**:

analizamos cada función y sus variantes, ya que se podían solucionar de distintas maneras. Algunos casos de forma manual (loop, como en invertir listas), otra con listas anidadas, etc.


**¿Lo usaste tal cual o lo modificaste?**

lo usé tal cual


---

### 4 - diccionarios.py

**Herramienta**: deepseek

**Prompt usado**:
"vamos con el siguiente módulo"


> 

**Resultado obtenido**:
analizamos cada función y sus variantes, con algunos ejemplos visuales de iteraciones, otras versiones manuales, etc.



**¿Lo usaste tal cual o lo modificaste?**
lo usé tal cual

---

### 5 - loops.py

**Herramienta**: deepseek

**Prompt usado**:
"vamos con el siguiente módulo"

> 

**Resultado obtenido**:
analizamos cada función, acá también habían versiones manuales con loop (como para contar_hasta), una versión alternativa sin string para suma_digitos, etc.


**¿Lo usaste tal cual o lo modificaste?**

lo usé tal cual
---

### 6 - funciones.py

**Herramienta**: deepseek

**Prompt usado**:
"vamos con el siguiente módulo"

> 

**Resultado obtenido**:

analizamos cada función, algunas versiones manuales, explicaciones paso a paso (ya que las funciones de este módulo eran bastante más complejas), también definiciones y comandos.

**¿Lo usaste tal cual o lo modificaste?**
lo usé tal cual


---

### 7 - operaciones.py

**Herramienta**: deepseek

**Prompt usado**:
"vamos con el siguiente módulo"

> 

**Resultado obtenido**:
analizamos las distintas versiones (propuesta/manual), sus explicaciones y ejemplos. 


**¿Lo usaste tal cual o lo modificaste?**

lo usé tal cual

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?

Refiriéndome exclusivamente a este TP, la verdad es que no aprendí nada nuevo sobre cómo formular buenos prompts. El tiempo que tuvimos para resolverlo fue ínfimo e incluso tardé muchísimo en poder abrir el repositorio (tuve que solicitar acceso entre 4 y 5 veces hasta que dejó de tirarme error), por lo que tuve que hacerlo de manera rápida y sin el análisis que me hubiera gustado tener. 
La IA fue imprescindible para realizar este trabajo en tan poco tiempo, tanto para en análisis de los requisitos e interpretación del TP, soporte para configurar pip, análisis de las funciones, escritura y comprensión de Python, etc.
La próxima vez solicitaría una extensión en el tiempo de entrega del trabajo, para poder dedicarle el tiempo y esfuerzo que amerita
