# Grimonio

<p>
  <a href="https://www.npmjs.com/package/serverless-offline">
    <img src="https://img.shields.io/npm/v/serverless-offline.svg?style=flat-square">
  </a>
  <a href="https://github.com/dherault/serverless-offline/actions/workflows/integrate.yml">
    <img src="https://img.shields.io/github/workflow/status/dherault/serverless-offline/Integrate">
  </a>
  <img src="https://img.shields.io/node/v/serverless-offline.svg?style=flat-square">
  <a href="https://github.com/serverless/serverless">
    <img src="https://img.shields.io/npm/dependency-version/serverless-offline/peer/serverless.svg?style=flat-square">
  </a>
  <a href="https://github.com/prettier/prettier">
    <img src="https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square">
  </a>
  <img src="https://img.shields.io/npm/l/serverless-offline.svg?style=flat-square">
  <a href="#contributing">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square">
  </a>
</p>

Este es un API Rest que simula la inscripcion de alumnos a un grimonio de forma aleatoria.
Realizado con las siguientes tecnologias:
<ol>
  <li>lenguaje: Python 3.10</li>
  <li>Framework: Flask</li>
  <li>Base de datos: Postgres</li>
</ol>

<h3>Manos a la obra</h3>

<ol type=”A”>
  <li>
    Requisitos previos:
    <ol>
        <li>Python 3.10 y pip3 instalados</li>
        <li>Postgres o base compatible (ejemplo: AuroraDB)</li>
    </ol>
  </li>
  <li>
    Instalación de dependencias:
    <ol>
        <li>Abrir terminal y ubicarse en la carpeta del proyecto, teclear los siguientes comandos</li>
        <li>cd init</li>
        <li>pip3 install -r requirements.txt</li>
        <li>Ejecutar los query para creacion de tablas en base de datos</li>
        <ol>
            <li>Ejecutar los comandos del archivo /init/data_base.sql</li>
            <li>Ejecutar los comandos del archivo /init/catalog_magic_affinity.sql</li>
            <li><img src="https://github.com/OscarGregorio19/ia-execirse/blob/master/images/img1.png"></li>
        </ol>
    </ol>
  </li>
  <li>
    Configuración conexión a basse de datos
    <ol>
        <li>La forma mas segura es cargar las siguientes variablles en tu entorno (variables de entorno)</li>
        <li>La otra forma es agregar los valores directamente al archivo /project/config/sql.py</li>
        <li><img src="https://github.com/OscarGregorio19/ia-execirse/blob/master/images/img2.png"></li>
    </ol>
  </li>
  <li>
    Ejecución de api rest
    <ol>
        <li>Ubicado en terminal path /project</li>
        <li>Ejecutar comando: python3 app.py</li>
        <li><img src="https://github.com/OscarGregorio19/ia-execirse/blob/master/images/img3.png"></li>
    </ol>
  </li>
  <li>
    Pruebas API Rest
    <ol>
        <li>Colección API Rest en /init/IA.postman_collection.json</li>
        <li>En este ejemplo, el archivo se cargo en postman</li>
        <li><img src="https://github.com/OscarGregorio19/ia-execirse/blob/master/images/img4.png"></li>
        <li>
            El listado de servicios es el siguiente:
            <ol>
                <li>Get Catalogos: Servicio que regresa los catalogs cargados en base de datos</li>
                <li><ol>
                    <li>Status: listado de estaus que puede tener un estudiante</li>
                    <li>Grimonios. listado de grimoniso al cual puede ir asignado un alumno</li>
                    <li>Afinidad magica: listado de afinidad magina que tiene un estudiante</li>
                </ol></li>
                <li>Solicitud de ingreso</li>
                <li>Actualización Solicitud de ingreso</li>
                <li>Consulta de todas las solicitudes de ingreso</li>
                <li>Consulta de solicitudes por grimonio</li>
                <li>Solicitud de ingreso</li>
                <li>Baja de estudiante</li>
            </ol>
        </li>
    </ol>
  </li>
</ol>

