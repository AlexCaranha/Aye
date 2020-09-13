# Beth

Assistente de voz criado com o intuito de ajudar pessoas com alguma deficiência ou dificuldade visual a utilizar o computador e celular para tarefas comuns e específicas.

Configuração Inicial:

1) Instalar o Python 3.7.7 (Release Date: March 10, 2020)
https://www.python.org/downloads/release/python-377/

2) Para criar o ambiente virtual (virtual environment), utilizar o comando:
python -m virtualenv venv

3) Para ativar o ambiente virtual, utilizar o comando:
venv\Scripts\activate

4) Para instalar todos os pacotes da aplicação, para ter o ambiente em python configurado corretamente, utilizar o comando:
pip install -r requirements.txt
pip install libs\PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
copy libs\ff*.exe venv\Scripts

5) Para executar a ferramenta, utilizar o comando:
python main.py

Para atualizar a lista de dependências (requirements.txt):

pip freeze > requirements.txt