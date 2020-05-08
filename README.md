# Aye

Ferramenta de auxílio a pessoas com alguma deficiência ou dificuldade visual para utilizar o computador e celular para tarefas comuns e específicas.

Configuração Inicial:

Instalar o Python 3.7.7 (Release Date: March 10, 2020)
https://www.python.org/downloads/release/python-377/

Para criar o ambiente virtual (virtual environment), utilizar o comando:
python -m virtualenv aye_venv

Para ativar o ambiente virtualt, utilizar o comando:
aye_venv\Scripts\activate

Para instalar todos os pacotes da aplicação para ter o ambiente em python configurado corretamente, utilizar o comando:
pip install -r requirements.txt 
pip install --force-reinstall git+https://github.com/HeaTTheatR/KivyMD.git

Para gravar em um arquivo texto todos os pacotes instalados do seu ambiente python, utilizar o comando:
pip freeze > requirements.txt





manager.getPluginByName(name, category='Default')
Get the plugin correspoding to a given category and name

