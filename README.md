# Documentación oficial
https://python-poetry.org/docs/basic-usage/#using-poetry-run

poetry update para que use el poetry.lock

poetry install -> primero genera poetry.lock si no lo encuentra lo crea.

poetry build -> nos crea carpeta `sdist` que incluye el `wheel` y el`sdist`.

poetry publish -> publicar el paquete al pypi (se necesita credenciales y certificaciones)

poetry check -> chequea estructura del pyproject.tol
poetry search -> busca paquetes


poetry run python your_script.py
poetry run python .\jokes.py

# Activar entorno virtual
Manera facil: 
The easiest way to activate the virtual environment is to create a nested shell with poetry shell.

To deactivate the virtual environment and exit this new shell type exit. To deactivate the virtual environment without leaving the shell use deactivate