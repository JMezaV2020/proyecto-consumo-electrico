# Proyecto de Consumo Eléctrico Anual por Comuna y Tipo de Cliente

https://jmezav.pythonanywhere.com/

## Descripción del Proyecto
Este proyecto tiene como objetivo analizar el consumo eléctrico anual en distintas comunas de Chile, desglosado por tipo de cliente. Los datos utilizados provienen de las entregas de antecedentes de empresas distribuidoras a la Comisión Nacional de Energía (CNE). A través de este análisis, se busca identificar patrones de consumo, tendencias estacionales y diferencias en el consumo entre diversos tipos de clientes y regiones.

## Estructura del Repositorio
El repositorio incluye los siguientes elementos:

- **Datos**: Archivos CSV procesados y limpiados.
- **Scripts**: Scripts y notebooks utilizados para el análisis de datos.
- **Visualizaciones**: Gráficos y reportes generados a partir del análisis.
- **Documentación**: Instrucciones detalladas para reproducir el análisis y contribuir al proyecto.

## Datos
La información procesada incluye los siguientes campos:

|   Column               | Non-Null Count | Dtype  |
|------------------------|----------------|--------|
| anio                   | 390009         | int64  |
| mes                    | 390009         | int64  |
| region                 | 390009         | object |
| comuna                 | 390009         | object |
| tipo_clientes          | 390009         | object |
| tarifa                 | 390009         | object |
| clientes_facturados    | 390008         | float64|
| e1_kwh                 | 389393         | object |
| e2_kwh                 | 389400         | object |
| energia_kwh            | 390009         | int64  |

**Descripción de los campos:**
- **anio**: Año del registro.
- **mes**: Mes del registro.
- **region**: Región de la comuna.
- **comuna**: Nombre de la comuna.
- **tipo_clientes**: Tipo de clientes (residencial, comercial, industrial, etc.).
- **tarifa**: Tipo de tarifa aplicada.
- **clientes_facturados**: Número de clientes facturados.
- **e1_kwh**: Energía en kWh (primera medición).
- **e2_kwh**: Energía en kWh (segunda medición).
- **energia_kwh**: Energía total consumida en kWh.

La tabla de datos cuenta con 389392 filas y 10 columnas.

**Nota**: Esta data podría sufrir modificaciones ya que se encuentra en revisión.

## Tecnologías Utilizadas
- **Python**: Para la manipulación y análisis de datos.
- **Pandas**: Biblioteca para el manejo de estructuras de datos.
- **Matplotlib / Seaborn**: Bibliotecas para la visualización de datos.
- **Flask**: Framework web utilizado para desarrollar la aplicación web.
- **PythonAnywhere**: Plataforma utilizada para desplegar la aplicación web.

## Despliegue
El proyecto será desplegado utilizando [PythonAnywhere](https://www.pythonanywhere.com/) y el framework [Flask](https://flask.palletsprojects.com/). Esto permitirá que el análisis y las visualizaciones sean accesibles a través de una interfaz web amigable.

## Instalación y Ejecución
Para reproducir este proyecto en tu máquina local, sigue estos pasos:

1. Clona el repositorio:
    ```bash
    git clone https://github.com/usuario/proyecto-consumo-electrico.git
    cd proyecto-consumo-electrico
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Inicia la aplicación Flask:
    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development  # Para habilitar el modo de desarrollo
    flask run
    ```

4. Accede a la aplicación web en tu navegador:
    ```
    http://127.0.0.1:5000
    ```
