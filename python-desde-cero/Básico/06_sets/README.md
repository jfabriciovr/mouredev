## SETS

Es una estructura de datos ideal para almacenar elementos únicos y realizar operaciones como la unión, intersección y diferencia. Son colecciones no ordenadas y sin elementos duplicados, lo que los hace muy eficientes cuando se trata de realizar búsquedas y operaciones entre conuntos de datos.

En esta lección aprenderás:

- **Definición y creación de sets**: `set()`, `{elemento1, elemento2}` y pueden almacenar todo tipo de datos. Si se usan las llaves vacías se crea otro dipo de estructura de datos llamada diccionario, y no un set.

- **Intersección de elementos**: `add()` para agregar elementos. Genera un error si se quiere agregar un elemento que ya existe.

- **Búsqueda de Elementos**: con el operador `in` verificamos si un elemento específico está presente en el set.

- **Eliminación de Elementos**: `remove()` produce error si el elemento no existe, `discard()` no arroja error, `clear()` vacía el set.

- **Transformación entre sets y listas**: Los sets no están ordenados (es decir que no se puede acceder a los elementos por su índice), pero podemos convertirlos a lista cuando necesitmos acceder a un elemento específico.

- **Operaciones con Sets**: operaciones de Teoría de Conjuntos como `union()`que combina elementos de dos sets y `difference()` que devuelve los elementos que están en un set pero no en otro.
