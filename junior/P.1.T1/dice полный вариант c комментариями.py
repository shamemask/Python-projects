import random

gain = 100 # общее кол-во очков

while gain >0: # окончание игры при израсходовании всех очков
    
    user_number = input ("ваше число") # студент может не приводить str к int сразу

    '''  не обязательное условие, для первой части'''
    if int(user_number)<2 or int(user_number)>12:
        print("число вне диапазона")
        continue

    bet = int(input ("ваша ставка"))  
    
    '''  не обязательное условие, для первой части  '''
##    if bet<1 or bet>gain:
##        print("ставка не допустима")
##        continue

    ''' старт, бросаем кубики'''

    '''
    total_score - сумма выпавших кубиков

    Студент может любым способом реализовать бросок кубиков(получение случайного числа)

    Для первой части подойдет решение с двумя переменными и повторяющимися строками кода.

    НО, для второй части, надо обратить внимание студента, на повторение одинаковых строк кода 
    
    '''
    '''1 вариант'''
##    score1 = random.randint(1,6) # to 0 do 6
##    score2 = random.randint(1,6)
##    print("score1",score1)
##    print("score2",score2)
##    total_score = score1+score2
    '''2 вариант'''
##    total_score = random.randint(1,6) + random.randint(1,6)
    '''3 вариант'''
##    total_score=0
##    for i in range (2):
##        total_score += random.randint(1,6)
    '''4 вариант'''
##    total_score = random.randint(1,12)

    ''' конец, бросаем кубик '''
        
    print(f"Сумма выповших чисел: {total_score}")

    ''' Блок проверки'''    
    '''
        В первом варианте, есть логическая ошибка
        , так как условие total_score==int(user_number) не выполняется
        Но оно подойдет для зачета первой части.

        Для зачета по первой части достаточно реализовать
        все четыре ситуаций из условия к задаче.

        Несвязанные условия не засчитываются
        
    '''
##    if total_score < 7 and int(user_number)<7:
##        gain += bet
##        print(f"Вы выйграли: {total_score}, ваш счет {gain}")
##    elif total_score > 7 and int(user_number)>7:
##        gain += bet
##        print(f"Вы выйграли: {total_score}, ваш счет {gain}")
##    elif total_score==int(user_number):
##        gain += 4 * bet
##        print(f"Вы выйграли: {total_score}, ваш счет {gain}")
##    else:
##        gain -= bet
##        print(f"Ставка проиграна, ваш счет {gain}")

    '''
        Второй вариант, логически верный

        Таково же эффекта можно добиться случайно расставив условия
        ,но несвязанные условия не засчитываются
        
    '''

    if total_score==int(user_number):
        gain += 4 * bet
        print(f"Вы выйграли : {total_score}х4, ваш счет {gain}")
    elif total_score < 7 and int(user_number)<7:
        gain += bet
        print(f"Вы выйграли: {total_score}, ваш счет {gain}")
    elif total_score > 7 and int(user_number)>7:
        gain += bet
        print(f"Вы выйграли: {total_score}, ваш счет {gain}")
    else:
        gain -= bet
        print(f"Ставка проиграна, ваш счет {gain}")

    '''
        Конец блока проверки

    '''

    '''
        Предложение закончить игру 

    '''    
    answer = input("Сыграем еще?")
    if answer== "нет":
        print(f"Общий выигрыш составил {gain}")
        break
    
    '''-----------------------------'''
    
print("игра окончена") # не обязательно
