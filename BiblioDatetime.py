from datetime import datetime
from datetime import date
data_atual = date.today()
data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,
data_atual.year)
print(data_em_texto)