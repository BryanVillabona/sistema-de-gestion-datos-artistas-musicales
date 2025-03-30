# LimeWire - Sistema de Gestión de Artistas Musicales

----------
***

## Tabla de Contenido
1. [Informacion General](#informacion-general)
2. [Tecnologias](#tecnologias)
3. [Instalacion](#instalacion)
4. [Caracteristicas Principales](#caracteristicas-principales)
5. [Estructura del Sistema](#estructura-del-sistema)
6. [Colaboracion](#colaboracion)
7. [FAQs](#faqs)

### Informacion General
***
Este proyecto tiene como objetivo desarrollar un sistema integral de gestión para LimeWire, permitiendo administrar datos de artistas musicales, países, géneros musicales y generar informes detallados.

El sistema permite:

-   Registrar y gestionar información sobre artistas musicales.
    
-   Administrar datos de países y géneros musicales.
    
-   Generar informes sobre actividad musical y ventas.
    
-   Consultar datos específicos según criterios de búsqueda.

## Tecnologias
***

Este sistema ha sido desarrollado utilizando las siguientes tecnologías:

-   **Python**: Lenguaje de programación principal.
    
-   **JSON**: Para almacenamiento y persistencia de datos.
    
-   **GitHub**: Para la gestión de versiones y colaboración en el desarrollo.

## Instalacion
***
Siga estos pasos para instalar y ejecutar el sistema:
```
$ git clone [BryanVillabona/sistema-de-gestion-datos-artistas-musicales](https://github.com/BryanVillabona/sistema-de-gestion-datos-artistas-musicales)
$ cd sistema-de-gestion-datos-artistas-musicales-main
$ python main.py
```
**Información adicional:** Si se desea usar la aplicación en un entorno virtual:
 ```
$ python -m venv env
$ source env/bin/activate  # En Windows: env\Scripts\activate
$ pip install -r requirements.txt
$ python main.py
```

## Caracteristicas Principales
***
-   **Gestión de Datos de Artistas Musicales**
    
    -   Registro de artistas con información detallada (nombre, país, años de actividad, ventas, estado, etc.).
        
-   **Interacción con Países y Géneros Musicales**
    
    -   Registro de países con código ISO e ISO3.
        
    -   Registro de géneros musicales con identificadores y descripciones.
        
-   **Generación de Informes**
    
    -   Listado de artistas por país y período de tiempo.
        
    -   Reportes de ventas musicales por artista y año.
        
    -   Análisis de actividad musical en los últimos 10 años.

## Estructura del Sistema
***
El sistema sigue una estructura modular para gestionar la información de artistas, países y géneros musicales, además de permitir la generación de informes.

#### Datos Almacenados en JSON:

-   **artistas.json**: Contiene la información detallada de cada artista musical.
    
-   **paises.json**: Almacena los datos de los países y sus códigos ISO.
    
-   **generos.json**: Guarda la información sobre los géneros musicales disponibles.
    

#### Módulos del Sistema:

1.  **Módulo de Gestión de Artistas**:
    
    -   Agregar, editar y eliminar artistas.
        
    -   Consultar artistas por país, género y años de actividad.
        
2.  **Módulo de Gestión de Países y Géneros**:
    
    -   Administración de países y sus códigos ISO.
        
    -   Gestión de géneros musicales.
        
3.  **Módulo de Reportes**:
    
    -   Generación de informes específicos según los filtros solicitados.
        
    -   Obtención de estadísticas de ventas y actividad musical.

## Colaboracion
***

Si deseas colaborar en el proyecto, puedes:

1.  Hacer un fork del repositorio.
    
2.  Crear una rama con tus cambios (`git checkout -b mi-rama`).
    
3.  Realizar un commit (`git commit -m "Descripción de cambios"`).
    
4.  Enviar un pull request.
    

Cualquier aporte es bienvenido, ya sea en el código, la documentación o sugerencias para mejorar el sistema.

## FAQs
***
1.  **¿Cómo se almacenan los datos?** Los datos se almacenan en archivos JSON para facilitar su persistencia y manipulación.
    
2.  **¿Se requiere una base de datos?** No, toda la información se maneja mediante archivos JSON, por lo que no se necesita una base de datos adicional.
    
3.  **¿El sistema permite filtrar artistas por múltiples criterios?** Sí, se pueden realizar búsquedas por país, género, años de actividad y más filtros disponibles.
