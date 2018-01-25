# Accidentes viales en la ZMG

Desarrollo de proyecto gubernamental para disminuir los accidentes viales dentro de la ZMG.

## Requisitos

* Python 3 o superior.
* Virtualenv
* Compilador `pdflatex`


## Uso

### Primer uso
Solicitar el url necesario para clonar el repo desde overleaf.
Al tener tal url, seguir los siguientes pasos
(nota: instrucciones para **linux**):

1. Instala: `sudo apt install texlive-lang-spanish`
1. Crea un ambiente controlado e instala las dependencias:
    * `virtualenv --python=python3 venv`
    * `source venv/bin/activate`
    * `pip install -r requirements.txt`
1. Corre el siguiente comando: `python3 setup.py`
1. Agrega las contribuciones a `main.tex`. 

### Compilar

El archivo `main.py` permite compilar `main.tex` y agregar los resultados.
El pdf resultante se encontrará en la carpeta `output`.
Correr en la terminal:

```bash
python3 main.py --filename {filename}
``` 

Sustituir **{filename}** con el nombre del pdf resultante sin la extensión (e.g. report).

Opciones:

```
    --filename  : nombre del pdf resultante.
    --output    : path para el pdf resultante (default: output/)
```

## Contribuciones y colaboradores
Para contribuir en le proyecto favor de contactar a alguno de los colaboradores.

Colaboradores principales:
* Rodrigo Hernández Mota
* [...]
* [...]
* [...]

## Licencia

Ver archivo **LICENSE.md**.