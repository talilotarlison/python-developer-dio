from datetime import datetime
import pytz

# Criando um objeto datetime sem fuso horário (na hora local do sistema)
data_local = datetime.now()

# Criando um fuso horário específico (por exemplo, São Paulo)
fuso_sp = pytz.timezone('America/Sao_Paulo')

# Convertendo o datetime para o fuso horário especificado
data_com_fuso = fuso_sp.localize(data_local)

print("Data sem fuso:", data_local)
print("Data com fuso:", data_com_fuso)

# O módulo pytz é amplamente utilizado para manipular fusos horários em Python, pois fornece suporte a todos os fusos horários da base de dados da IANA (Internet Assigned Numbers Authority).