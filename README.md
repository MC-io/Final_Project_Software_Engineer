# Estilos de Programacion usados

## Code Golf
Un estilo de programacion Code Golf se utiliza en los archivos de la carpeta backend/blueprints de la aplicacion ya que cuentan con metodos de pocas lineas, que dependiendo de la complejidad de la peticion JSON a la API pueden ser mas largas.

![alt text](Images/code_golf.PNG "Title")

Captura de pantalla del archivo backend/blueprints/evento_blueprint.py

## Pipeline
Este estilo con programacion orientado a objetos es usado en las clases de backend/models ya que estas clases contienen funciones que retornan datos que no son compartidos entre otras funciones de la misma clase.

![alt text](Images/pipeline.PNG "Title")

Captura de pantalla del archivo backend/models/usuario.py

## Persistent Tables
Los archivos de repositorio de la parte de infraestructura utilizan el estilo de programacion de persistent tables ya que al establecer una conexion directa con la base de datos asociada, cuentan con lineas de queries para la extraccion y modificacion de la Base de Datos.

![alt text](Images/persistent_tables.PNG "Title")

Captura de pantalla del archivo backend/infrastructure/evento_repository.py