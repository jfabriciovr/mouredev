## DICCIONARIOS

Los **Diccionarios** son colecciones que almacenan pares de clave-valor (key-value pairs), permitiendo acceder a los valores mediante su clave.

- Para representar datos estrucuturados, como entradas de bases de datos o la configuración de una aplicación

En esta lección aprenderás:

- **Definición o Declaración**: `{}`, `dict()`, `{"clave": "valor", "clave2": "valor2"...}`
- **Acceso a Elemento**: se accede al valor de un elemento, buscando la clave específica y no un índice.
- **Inserción y actualización de elementos**: los diccionarios son mutables por lo que se se pueden modificar.
- **Eliminación de elemento**: `del` más el nombre de la clave, para eliminar un par clave-valor.
- **Operaciones comunes**: `keys()`para obtener sólo las claves, `values()` para obtener sólo los valores e `items()` para obtener todos los pares clave-valor.
- **Comprobación de claves**: para comprobar que una clave existe se utiliza el operador `in`. Da como resultado un boolean.
- **Diccionarios anidados**: un diccionario puede contener un valor que sea otro diccionario, permitiendo representar estructuras más complejas.
- **Conversión de Listas a Diccionarios**: `fromkeys([lista])`para crear un diccionario donde las claves provienen de una lista, y los valores pueden ser definidos o dejados vacíos.
