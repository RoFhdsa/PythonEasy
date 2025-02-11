# # Как объявить аргумент ?
# argument = 1    # int - бесконечности до + бесконечности
# print(argument, type(argument))
# argument = int(9/3)     # float - с плавающей запятой
#                         # Decimal (1) = 1.00
#                         # 9 /3 = 3.0
#                         # 01011 = 2.9999999999999
# argument = int(9/3)
# print(argument, type(argument))
# argument = (9/3)
# print(argument, type(argument))
#


# argument = None # Null
# # СТРОКА
# argument_str = '1490' + ' год'
# print(argument_str)
# d = None
# print(type(d))
# d = 1431
# print(type(d))
import datetime
d = str(1)
print(d, type(d))

print(datetime.date.today())

data_format = datetime.datetime.strftime(datetime.date.today())
print(data_format)

d = {'contract_data':datetime.date.today()}
print(d)

dict = {'a':'aaa'}




if '' == 0:
    print('dsdsds')
