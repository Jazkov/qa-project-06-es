Jahaziel Ebed Kolansinsky Victoria 
Sprint 6 

"Creación de un kit para el usuario o usuaria en Urban Grocers"

Urban Grocers es una aplicación de diversos artículos en donde el usuario o 
usuaria puede crear kits personalizados.

Se está comprobando cómo la aplicación Urban Grocers crea kits de productos, para ello se 
han creado  varias listas de comprobación, una de ellas es para el campo name en la solicitud
de creación de un kit de productos.

La tarea a realizar en este proyecto es automatizar las pruebas de la lista de comprobación, 
cargar el código en GitHub y enviar el repositorio a revisión.

Para realizar este proyecto se instaló el entorno de dessarollo Pycharm
y el interprete python.

Dentro de pycharm se configuró el ambiente en "Pure python" con el entorno 
virtual "New Virtualenv Using" 

Se deben descargar las paqueterias de "pytest" y "requests" en el apartado de python "packges"

Para realizar las pruebas se crearón 6 archivos para la ejecución del proyecto:

"configuration" para guardar el servidor y las rutas api de Urban Grocers.
"sender_stan_request" realizar solicitudes "Get" y "Post" para crear un  usuario y un kit.
"data" para guardar el encabezado e información que se utiliza dentro las pruebas.
"create_kit_name" para las solicitudes positivas y negativas con sus respectivas pruebas.
"gitignore" para evitar que varios archivos se suban al repositorio de "GitHub"
"readme" descripción del proyecto.

Para generar el repositorio del proyecto del sprint 6 se utilizó GitHub.

En éste proyecto se automatizaron 9 pruebas de comprobación para la creación 
de un kit dentro de un usuario o usuaria, las cuales fueron:

*Número permitido de caracteres (1)
*El número permitido de caracteres (511)
*El número de caracteres es menor que la cantidad permitida (0)
*El número de caracteres es mayor que la cantidad permitida (512)
*Caracteres especiales
*Espacios
*Números
*Parámetro vacío
*Tipo de parámetro diferente (número)