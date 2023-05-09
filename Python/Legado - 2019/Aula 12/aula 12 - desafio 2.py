'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada, exemplo:
0-11 = bom dia, 12-17 = boa tarde e 18-23 = boa noite.
'''
hour = input ('Digite a hora: ')
minute = input ('Digite o minuto: ')

if hour.isdigit() and minute.isdigit():
    hour = int(hour)
    minute = int(minute)
    period = (f'{hour}:{minute}')

    if period < '00:00' or period > '23:59':
         print ('Horário deve estar entre 0 e 23.')
    if period >= '00:00' and period <= '11:59':
         print ('Bom dia! =)')
    elif period >= '12:00' and period <= '17:59:':
         print ('Boa tarde! =)')
    else:
         print ('Boa noite! =)')

#
# period = input ('Digite um horário (0-23): ')
# if period.isdigit():
#     period = int(period)
# 
#     if period < 0 or period > 23:
#         print ('Horário deve estar entre 0 e 23')
#     else:
#         if period <= 11:
#             print ('bom dia! =)')
#         elif period <= 17:
#             print ('Boa tarde! =)')
#         else:
#             ('Boa noite! =)')
# else:
#     print('Por favor, digite um horário entre 0 e 23.')