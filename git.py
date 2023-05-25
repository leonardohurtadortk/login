import os

def push_to_github(commit_message, repository_url, branch='main'):
    """Sube los cambios a un repositorio remoto en GitHub.

    Esta función realiza los siguientes pasos:
    1. Inicializa un repositorio local de Git.
    2. Agrega todos los archivos al área de preparación de Git.
    3. Hace un commit con el mensaje especificado.
    4. Agrega un remote con la URL especificada.
    5. Hace push de los cambios al repositorio remoto en la rama especificada.

    Args:
        commit_message (str): Mensaje del commit.
        repository_url (str): URL del repositorio remoto en GitHub.
        branch (str): Rama a la que se hará push de los cambios (por defecto es 'main').
    """
    # Inicializa un repositorio local de Git
    os.system('git init')

    # Agrega todos los archivos al área de preparación de Git
    os.system('git add .')

    # Hace un commit con el mensaje especificado
    os.system(f'git commit -m "{commit_message}"')

    # Agrega un remote con la URL especificada
    os.system(f'git remote add origin {repository_url}')

    # Hace push de los cambios al repositorio remoto en la rama especificada
    os.system(f'git push -u origin {branch}')

# Ejemplo de uso
push_to_github("mensaje del commit", "URL_DEL_REPOSITORIO")