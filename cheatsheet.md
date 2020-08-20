# Python Cheat Sheet

    brew install pipenv
    
    pipenv shell
    python --version

    pipenv install <name>
    pipenv uninstall <name>
    pipenv install <name> --dev
    pipenv install -r ./requirements.txt
    pipenv install --ignore-pipfile
    
    pipenv lock
    pipenv lock -r > requirements.txt 

    pipenv check
    pipenv graph