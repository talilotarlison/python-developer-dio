import datetime

# Função para calcular a diferença de fuso horário
def calcular_fuso_brasil_e_usa():
    # Definindo os fusos horários de referência
    brasil_tz = datetime.timezone(datetime.timedelta(hours=-3))  # Brasília, Brasil (UTC-3)
    usa_tz = datetime.timezone(datetime.timedelta(hours=-5))  # Hora padrão do Pacífico (UTC-8)
    
    # Data e hora atual (em UTC) - Depreciado
    # agora_utc = datetime.datetime.utcnow()
    
    # Data e hora atual (em UTC) - Valida
    agora_utc = datetime.datetime.now(datetime.timezone.utc)
    
    # Convertendo a hora atual para os fusos horários do Brasil e dos EUA
    brasil_time = agora_utc.replace(tzinfo=datetime.timezone.utc).astimezone(brasil_tz)
    usa_time = agora_utc.replace(tzinfo=datetime.timezone.utc).astimezone(usa_tz)
    
    # Exibindo os horários locais de Brasil e EUA
    print(f"Hora no Brasil (Brasília): {brasil_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Hora nos EUA (Pacific Time): {usa_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Calculando a diferença de fuso horário
    diferenca = brasil_tz.utcoffset(datetime.datetime.now()) - usa_tz.utcoffset(datetime.datetime.now())
    
    print(f"Diferença de fuso horário (em horas): {diferenca.total_seconds() / 3600} horas")

# Chama a função
calcular_fuso_brasil_e_usa()
