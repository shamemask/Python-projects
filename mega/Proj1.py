# 1.            Даны:
# размер ипотечного кредита — 2 млн. руб,
# процентная ставка — 10 %,
# кол-во лет— 5.
# Найти переплату по кредиту


from collections import Counter
import statistics

mortgage = 2000000  # сумма кредита
interest_rate = 0.1  # процентная ставка
debt_years = 5  # кол-во лет


print(
    f"Расчет кредита на {mortgage} рублей, {debt_years} лет, с {interest_rate*100}% годовых")

debt = mortgage
ir_per_day = (interest_rate / 365)

month_pay = round(mortgage/(debt_years * 12), 2)


calendar = Counter({
    'Января': 31,
    'Февраля': 28,
    'Марта': 31,
    'Апреля': 30,
    'Мая': 31,
    'Июня': 30,
    'Июля': 31,
    'Августа': 31,
    'Сентября': 30,
    'Октября': 31,
    'Ноября': 30,
    'Декабря': 31
})

months = [
    'Января',
    'Февраля',
    'Марта',
    'Апреля',
    'Мая',
    'Июня',
    'Июля',
    'Августа',
    'Сентября',
    'Октября',
    'Ноября',
    'Декабря'
]


current_year = 2022  # int(input("Введите текущий год: "))
current_month = 3  # int(input("Введите текущий месяц: "))
current_day = 20  # int(input("Введите текущий день: "))

last_year = current_year + debt_years
debt_proc = 0  # сумма начисленных процентов


# moy - month of year
def moy(year):
    global months, calendar, last_year, current_year, current_month
    if year == current_year:
        return months[current_month-1:12]
    elif year == last_year:
        return months[0:current_month-1]
    else:
        return months

# dom - day of month


def dom(year, month):
    global months, calendar, last_year, current_year, current_month, current_day
    if year == current_year and months.index(month)+1 == current_month:
        return current_day, calendar[month]+1
    elif year == last_year and months.index(month)+1 == current_month:
        return 1, current_day+1
    else:
        return 1, calendar[month]+1


# расчет оплаты
ir_calc = mortgage
proc_calc_list = []
month_proc_calc = 0
i = 0
for year in range(current_year, last_year+1):
    month_of_year = moy(year)
    for month in month_of_year:
        first_day_month, last_day_month = dom(year, month)
        for day in range(first_day_month, last_day_month):
            proc_calc = round(ir_calc * ir_per_day, 2)
            month_proc_calc += proc_calc
            

        proc_calc_list.append(month_proc_calc)
        month_proc_calc = 0
        ir_calc -= month_pay
        i += 1

mid_ir_pay = statistics.mean(proc_calc_list)
mid_ir_pay += (month_pay + mid_ir_pay * (365-28)/365 ) / (debt_years * 12)
mid_ir_pay = round(mid_ir_pay, 2)
print(f"Средняя оплата процентов {mid_ir_pay}")


# Main
for year in range(current_year, last_year+1):
    month_of_year = moy(year)
    for month in month_of_year:
        first_day_month, last_day_month = dom(year, month)
        for day in range(first_day_month, last_day_month):
            print(f"{day} {month} {year}г.")
            proc = round(debt * ir_per_day, 2)
            print(f"Процент начисленный за день - {proc}руб.")
            debt_proc += proc
            debt_proc = round(debt_proc, 2)
            print(f"общая сумма процентов - {debt_proc}руб.")
            debt += proc
            debt = round(debt, 2)
            print(f"общая сумма долга - {debt}руб.")

        debt -= month_pay + mid_ir_pay
        debt = round(debt, 2)
        print(f"оплата долга - {month_pay}руб. + {mid_ir_pay}руб. проц")
        print(f"общая сумма долга - {debt}руб.")

print(
    f"\nСумма начисленных процентов за {debt_years} лет, на {mortgage}руб., при ставке {interest_rate * 100}% --- {debt_proc} руб.")
