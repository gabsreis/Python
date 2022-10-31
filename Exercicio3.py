from datetime import *
d = date.today()
print(d)
print('{}/{}/{}'.format(d.day, d.month, d.year))
print(d.strftime('%d/%m/%Y'))
dd = datetime.now()
c = (dd.strftime('%d/%m/%Y %H:%M'))
print(c)
c = '14/10/2015 12:15'
print(datetime.strptime(c, '%d/%m/%Y %H:%M'))