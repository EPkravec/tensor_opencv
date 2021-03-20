from tensor_first import Month, Money
from seal import seal_func
from config import *

'''
=======================================================================================================================
Запуская данный файл, Вы получаете результирующие данные по колличеству отработаных месяцев, общую сумму дохода, доход
за первый и последний месяцы, а так же средный доход. Так же будет обнаружено положение печати и обведенно квадратом.  
=======================================================================================================================
'''
number_1 = Month.binar_ml(month_left)
noises_1 = Month.noises_ml(number_1)
number_2 = Month.binar_mr(month_right)
noises_2 = Month.noises_mr(number_2)
result = Month.quantity_month(noises_1, noises_2)

list_number_l = Money.rgb_l(table_left)
sums_l = Money.noises_l(list_number_l)
list_number_r = Money.binarized_r(table_right)
sums_r = Money.noises_r(list_number_r)
total_money = sum(sums_l) + sum(sums_r)

average_monthly = int(total_money / result)

print(f' За {result} месяцев общая сумма дохода составила: {total_money} руб. \n '
      f'Доход за первый месяц {sums_l[0]} руб. за последний месяц {sums_r[5]} руб. \n '
      f'Среднемесячный доход составляет {average_monthly} руб.')

seal_func(image)
