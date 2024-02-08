## Project Name: datafun-06-eda
```
This project showcases the continued practice of the integration
of Python and SQL.

Author: Nicole Hansen
```

## Steps
1. Create repo on GitHub
2. Clone repo to local
    git clone https://github.com/nhansen23/datafun-06-eda
3. Create .gitignore, requirements.txt
    ni .gitignore
    ni requirements.txt
4. Add to .gitignore: .venv\, .vscode\, \__pycache__/
5. Create directory for data
    mkdir data
6. Activate virtual environment
    py -m venv .venv
    .\.venv\Scripts\Activate
7. Install packages
    py -m pip install jupyterlab pandas pyarrow matplotlib seaborn
8. Freeze dependencies
    py -m pip freeze > requirements.txt