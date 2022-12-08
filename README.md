# pp5_edwinpalinn
#Introduccion: 
- En este trabajo se realizará el ejercicio de "Refinamiento de Código" para la actividad PP5 Calidad y Documentación. Su objetivo es limpiar el código usando herramientas como pylint y autopep8 y subirlo a un repositorio de GitHub.

#Refactorizacion: 
- Primero, se debe crear una función que convierta el archivo externo en una lista usando herramientas como open(), se almacena en una variable y se lo devuelva al usuario. Luego se crea una segunda función que toma como parámetro una variable de la primera función, y luego agrego todos los valores de la lista. La tercera función es la función principal que llama a las dos primeras funciones e imprime el resultado.

#Limpieza 
- se utilizo Pylint se usa para conseguir una puntuacion de mi trabajo y qué errores necesitan corregirse. La mayoría de estos errores consisten en agregar cadenas de documentos a funciones y agregar datos, como codificaciones, cuando se abren archivos. Una vez hecho esto, uso autopep8 para formatear el trabajo de esta manera y luego copio los resultados.

#Gestion de errores 
 - El mayor costo en la ejecución del código fue abrir el archivo con 'with open()', que luego se solucionó cambiando el formato de la función y algunos errores de indentación. Tambien tuve problemas en el paso 6 usando la herramienta try-except, algo que despues arregle al importar la funcion sys.

#prueba unitaria 
- Todas estas pruebas se realizan utilizando la herramienta pytest. La primera prueba utilizada es comprobar que la lista de precios es correcta. La segunda prueba es para confirmar que el costo total es correcto. La última verificación es verificar que la función principal no devuelva datos que no sean los resultados de las dos primeras funciones.

#Control de versiones 
- https://github.com/edwinpalin/pp5_edwinpalinn.git
- ![Captura de Pantalla 2022-12-08 a la(s) 7 35 21 p  m](https://user-images.githubusercontent.com/120063550/206589262-31d3148f-b180-4a20-a0ee-6c0a88c1aee1.png) 