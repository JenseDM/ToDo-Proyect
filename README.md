# Jensen ToDo
 Proyecto de gestion de tareas desarrollado en pyhton con el framework Django, HTML5 Y CSS3.

# Descripción funcional
 Este proyecto de Django, "Jensen ToDo", presenta una serie de vistas funcionales diseñadas para una aplicación de gestión de proyectos y tareas. Estas vistas abordan diversas funcionalidades clave, como el registro de usuarios, la creación de proyectos y tareas, la gestión de proyectos y la realización de tareas específicas. Cada vista está diseñada para ser clara, concisa y fácil de entender, proporcionando una experiencia de usuario intuitiva para la gestión eficiente de proyectos y tareas.

 ## Instalación 
 * git clone <"URL DEL REPOSITORIO">
 * cd DjangoProject
 * python -m venv venv
 * .venv\Scripts\activate
 * pip install django
 * python manage.py runserver
 * abrir servidor local en el navegador port:8000

 ## Uso
* Inicio: http://127.0.0.1:8000/
* Registro: http://127.0.0.1:8000/signup/
* Inicio de Sesión: http://127.0.0.1:8000/signin/
* Cerrar Sesión: http://127.0.0.1:8000/logout/
* Crear Proyecto: http://127.0.0.1:8000/createProject/
* Crear Tarea: http://127.0.0.1:8000/createTask/<project_id>/
* Ver Proyectos: http://127.0.0.1:8000/projects/
* Ver Tareas de un Proyecto: http://127.0.0.1:8000/tasks/<project_id>/
* Detalle de Tarea: http://127.0.0.1:8000/taskDetail/<task_id>/
* Marcar Tarea como Completada: http://127.0.0.1:8000/taskDetail/<task_id>/complete
* Eliminar Tarea: http://127.0.0.1:8000/taskDetail/<task_id>/delete
* Eliminar Proyecto: http://127.0.0.1:8000/projects/<project_id>/delete

## Views
* Inicio (home):
Descripción: La página de inicio del proyecto, que muestra información general y permite a los usuarios navegar hacia otras partes del sistema.
* Registro de Usuario (signup):
Descripción: Permite a los usuarios registrarse en el sistema proporcionando un nombre de usuario y una contraseña.
* Inicio de Sesión (signin):
Descripción: Permite a los usuarios iniciar sesión en el sistema con su nombre de usuario y contraseña.
* Cerrar Sesión (signout):
Descripción: Permite a los usuarios cerrar sesión en el sistema, terminando su sesión activa.
* Crear Proyecto (createProject):
Descripción: Presenta un formulario para que los usuarios creen un nuevo proyecto, proporcionando detalles como el nombre del proyecto.
* Ver Proyectos (projects):
Descripción: Muestra una lista de proyectos creados por el usuario actual, junto con opciones para interactuar con cada proyecto.
* Crear Tarea (createTask):
Descripción: Permite a los usuarios agregar una nueva tarea a un proyecto específico, proporcionando detalles como el nombre y la descripción de la tarea.
* Ver Tareas (tasks):
Descripción: Muestra una lista de tareas asociadas a un proyecto específico, permitiendo a los usuarios ver y gestionar las tareas pendientes.
* Detalle de Tarea (taskDetail):
Descripción: Muestra información detallada sobre una tarea específica, incluyendo su nombre, descripción y estado de finalización.
* Marcar Tarea como Completada (completeTask):
Descripción: Permite a los usuarios marcar una tarea como completada, actualizando su estado en el sistema.
* Eliminar Tarea (deleteTask):
Descripción: Permite a los usuarios eliminar una tarea específica de un proyecto, eliminando su entrada del sistema.
* Eliminar Proyecto (deleteProject):
Descripción: Permite a los usuarios eliminar un proyecto completo, incluyendo todas sus tareas asociadas, del sistema.
