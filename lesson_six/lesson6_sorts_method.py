
from mimetypes import init
from re import S


C = [{
    'car_name' : 'BMW X5',
    'speed' : 250,
    'price': 60000
},{
    'car_name' : 'VW Touareg',
    'speed' : 220,
    'price': 50000
},{
    'car_name' : 'Suzuki JIMMY',
    'speed' : 150,
    'price': 20000,
}]

C.sort( key =  lambda d : len(d['car_name']) )
print (*C,sep = '\n')


K =[]
x = ''
while x != '#':
    x = input('Введите уч: ')
    if x != '#':
        id  = int(x)
        value = int(input('Введите оц: '))
        K.append((id,value))

g ={}
for id, value in K:
    d = g.get(id, {'sum' : 0, 'grades' : []})
    d['sum'] += value
    d['grades'].append(value)
    d['grades'].sort(reverse = True)
    g[id] = d

sorted_s = list(g.keys())
sorted_s.sort(key = lambda id : g[id]['sum'], reverse = True)

R = []
for id in sorted_s:
    R.extend(g[id]['grades'])
print(R)