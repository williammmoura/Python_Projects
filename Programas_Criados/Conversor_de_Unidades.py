#Author: William Monte de Moura
#Unit Converter

#Metric Length Units
print('#' * 80)

print('Conversão de metros para quilômetros.')
metro = float(input('Digite o valor em METRO (m):'))
km = metro / 1000
print('{}m = {}Km.'.format(metro,km))

print('' * 80)

print('Conversão de quilômetros para metros.')
km2 = float(input('Digite o valor em QUILÔMETRO (Km):'))
m = km2 * 1000
print('{}km = {}m.'.format(km2,m))

print('#' * 80)

print('Conversão de metros para hectêmetro.')
m3 = float(input('Digite o valor em METRO (m):'))
hm = m3 / 100
print('{}m = {}hm.'.format(m3,hm))

print('' * 80)

print('Conversão de hectômetro para metro.')
hm2 = float(input('Digite o valor em HECTÔMETRO (hm):'))
m4 = hm2 * 100
print('{}hm = {}m.'.format(hm2,m4))

print('#' * 80)