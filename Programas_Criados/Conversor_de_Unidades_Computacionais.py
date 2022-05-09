#Author: William Monte de Moura
#Title: Conversor de Unidades Computacionais

print('=' * 80)
mega = float(input('Digite o valor em Megabyts:'))
bytes = mega * (1024**2)
print('O valor fornecido de {}MB, equivale a {}B (Bytes)'.format(mega, bytes))
kilobytes = mega * 1024
print('O valor fornecido de {}MB, equivale a {}kB (Kilobytes)'.format(mega, kilobytes))
gigabytes = mega / 1024
print('O valor fornecido de {}MB, equivale a {}GB (Gigabytes)'.format(mega, gigabytes))
terabytes = mega / (1024**2)
print('O valor fornecido de {}MB, equivale a {}TB (Terabytes)'.format(mega, terabytes))
print('=' * 80)

print('=' * 80)
kilobytes = float(input('Digite o valor em Kilobyts:'))
bytes = kilobytes * 1024
print('O valor fornecido de {}kB, equivale a {}B (Bytes)'.format(kilobytes, bytes))
mega = kilobytes / 1024
print('O valor fornecido de {}kB, equivale a {}MB (Megabytes)'.format(kilobytes, mega))
gigabytes = kilobytes / (1024**2)
print('O valor fornecido de {}kB, equivale a {}GB (Gigabytes)'.format(kilobytes, gigabytes))
terabytes = kilobytes / (1024**3)
print('O valor fornecido de {}kB, equivale a {}Terabytes (Bytes)'.format(kilobytes, terabytes))
print('=' * 80)