@ECHO OFF
IF "%1"=="" echo "usage: env create|remove"
REM Show help
IF "%1"=="create" conda env create --prefix ./.venv --file environment.yml --force
REM The --force flag forces (re-)creation of environment
REM and will remove previously existing environment of the same name.
IF "%1"=="remove" conda env remove --prefix ./.venv
REM Remove environment completely