from datetime import date
from datetime import datetime

def current_day():
    meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
    today = date.today()
    return f"Hoje é dia {today.day} de {meses[today.month-1]} de {today.year}"

def current_time():
    horas = ('zero', 'uma', 'duas', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte', 'vinte e uma', 'vinte e duas', 'vinte e três', 'vinte e quatro')
    now = datetime.now()
    
    # dd/mm/YY H:M:S
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    output = f"Horário atual: {horas[now.hour]} horas e {now.minute} minutos"
    return output

# print(current_day())
# print(current_time())

def identify_request(request):
    if request == "comando que dia é hoje":
        return current_day()

    if request == "comando horário atual":
        return current_time()

    return None