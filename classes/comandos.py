from datetime import date
from datetime import datetime

def current_day():
    meses = ('janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
    today = date.today()
    return f"Hoje é dia {today.day} de {meses[today.month-1]} de {today.year}"

def current_time():
    now = datetime.now()
    # dd/mm/YY H:M:S
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    output = "Horário atual: " + now.strftime("%H e %M")
    return output

# print(current_day())
# print(current_time())

def identify_request(request):
    if request == "comando que dia é hoje":
        return current_day()

    if request == "comando horário atual":
        return current_time()

    return None