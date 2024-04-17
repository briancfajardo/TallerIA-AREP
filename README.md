# Taller LLM

En este taller experimentamos con diferentes retos implementando un LLM en python haciendo uso de Lang CHain,  Pinecone y OpenAI.

## Iniciando

Estas instrucciones te ayudarán a tener una copia de este proyecto corriendo en tu máquina local.

### Prerrequisitos

* Git 
* Python
* Pip

Si aún no tienes instaladas estas tecnologias, los siguientes tutoriales te pueden ayudar

* Git: https://www.youtube.com/watch?v=4xqVv2lTo40
* Python: https://www.python.org/downloads/
* Pip: https://pip.pypa.io/en/stable/installation/

### Instalando el proyecto

Para hacer una copia local del proyecto, debes abrir tu terminal, dirigirte al directorio donde quieras que este el proyecto y usar el siguiente comando

```
git clone https://github.com/briancfajardo/TallerIA-AREP.git
```

Luego muevete al directorio creado y desde ahi ejecuta el siguiente comando

```
pip install requests
```

Ahora, en la carpeta src encontrarás 3 archivos referentes a los retos(pasos) que se realizaron durante el taller.

Para poder corrar cada reto toca que presiones SHIFT+F10 o usar la opción de RUN de tu ide.

## Explicación de los retos

- Reto 1:

Este script en Python utiliza la biblioteca "langchain" para generar respuestas a preguntas basadas en plantillas. Primero, importa las clases necesarias y establece la clave de la API de OpenAI. Luego, define una plantilla para preguntas y respuestas, crea una instancia de PromptTemplate, inicializa el modelo de OpenAI, y ejecuta una cadena LLM para responder a una pregunta específica sobre la teoría de la ciencia de Popper. La respuesta generada se imprime posteriormente.

- Reto 2:

Primero, importa las bibliotecas necesarias como bs4 para el análisis de HTML y clases específicas de la biblioteca "langchain". Luego, establece la clave de la API de OpenAI en la variable de entorno OPENAI_API_KEY.

Después, inicializa un cargador web para cargar documentos de una URL específica, dividir el texto en fragmentos y procesarlo para su posterior uso en la recuperación de información. A continuación, se crea un vectorstore utilizando los fragmentos de texto y un modelo de incrustaciones de OpenAI para representar el contenido de los documentos en un espacio vectorial.

Posteriormente, se define un encadenamiento de operaciones para recuperar información utilizando el modelo RAG (Retrieve And Generate) y el modelo de lenguaje de chat de OpenAI. Se establecen las operaciones de formateo y se invoca el encadenamiento con una pregunta sobre la descomposición de tareas. Finalmente, se imprime la respuesta generada por el encadenamiento.

- Reto 3:

Este código carga un archivo de texto llamado "Conocimiento.txt", lo divide en fragmentos más pequeños y los convierte en vectores utilizando incrustaciones de OpenAI. Luego, estos vectores se almacenan y se indexan en Pinecone para permitir búsquedas eficientes. Una vez que se ha indexado el texto, se realiza una búsqueda de similitud utilizando una consulta específica y se imprime el contenido del documento más relevante encontrado.

## Construido con

* [Python](https://www.python.org/) - Lenguaje de programación
* [PyCharm IDEA](https://www.jetbrains.com/es-es/pycharm/) - IDE de desarrollo

## Version

1.0-SNAPSHOT

## Autores

Brian Camilo Fajardo Sanchez - [briancfajardo](https://github.com/briancfajardo)

## Licencia

GNU General Public License family

## Agradecimientos

* Al profesor de Arquitecturas empresariales, Daniel Benavides