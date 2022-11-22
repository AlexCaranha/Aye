# Beth

Assistente de voz criado com o intuito de tornar tarefas simples e complexas mais acessíveis a todos por comandos de voz.

Configuração Inicial:

1) Instalar o Python 3.7.7 (Release Date: March 10, 2020)
https://www.python.org/downloads/release/python-377/

2) Criar o ambiente virtual do python:
python -m virtualenv venv

3) Ativar o ambiente virtual:
venv\Scripts\activate

4) Para instalar todos os pacotes da aplicação, para ter o ambiente em python configurado corretamente, utilizar o comando:
pip install -r requirements.txt
pip install libs\PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
copy libs\ff*.exe venv\Scripts

5) Executar a ferramenta:
python main.py

Para atualizar a lista de dependências (requirements.txt):

pip freeze > requirements.txt

Gerar executável:
generate_executable.bat



In linux:
sudo apt-get install portaudio19-dev python-pyaudio
pip install PyAudio