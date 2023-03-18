# Text_Checker#(Data_Double_Checker).py
# Двойная проверка данных

# https://github.com/Ozym1ndias/Data-Double-Checker

# Этот сценарий принимает файл в качестве входных данных по умолчанию: Data.txt.
# Данные должны быть расположены в строках. Каждая строка обозначает точку данных.
# Скрипт принимает каждую строку (точку данных) и добавляет ее в список по умолчанию: _Data[].
# Затем сценарий определяет, какие точки данных удваиваются в списке _Data[],
# и создает новый уникальный список под названием ___Data[] без удвоений в точках данных.
# Затем скрипт создает txt-файл с именем uData.txt и записывает содержимое списка ___Data[] в uData.txt

# ###################################################
# ############## Пересечение множеств ###############
# Имея два множества: А и В.
# Их пересечение представляет множество элементов, которые являются общими для А и для В.
# Операция пересечения во множествах может быть достигнута как при помощи оператора &, так и метода intersection().
# В обеих множествах 3 является общим элементом.

# x = {1, 2, 3}
# y = {4, 3, 6}
# print(x & y)  # Результат: 3


# То же самое может быть достигнуто при использовании метода intersection():

# z = x.intersection(y)
# print(z)  # Результат: 3
# ########################################################
# ############## Разница между множествами ###############
# Разница между А и В (А — В) — это множество со всеми элементами, которые содержатся в А, но не в В.
# Соответственно, (В — А) — это множество со всеми элементами в В, но не в А.

# Для определения разницы между множествами можно использовать функцию difference() или оператор — .
# Только первые три элемента множества set_a отсутствуют во множестве set_b, формируя выдачу.

# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# diff_set = set_a.difference(set_b)
# print(diff_set)  # Результат: {1, 2, 3}


# Оператор минус - можно также применить для нахождения разницы между двумя множествами:

# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# print(set_a - set_b)  # Результат: {1, 2, 3}
# #####################################################################
# ############## Симметричная разница между множествами ###############
# А и В — это множество с элементами, которые находятся в А и В,
# за исключением элементов, которые являются общими для обеих множеств.
# Это определяется использованием метода под названием symmetric_difference(), или оператора ^.

# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# symm_diff = set_a.symmetric_difference(set_b)
# print(symm_diff)  # Результат: {1, 2, 3, 6, 7, 8}
# #####################################################################


_Data = []  # Data1.txt
__Data = []  # Data2.txt
___Data = []  # uData.txt # Unique list


# Listing # Перечисление 1.txt
def txt2list1():
    with open('Data1.txt', 'r') as Data:
        for line in Data.readlines():
            _Data.append(line.replace('\n', ''))
        # print(_Data)
        print(f'Data1.txt # Contains rows: {len(_Data)}')  # Check for the length of the list


# Listing # Перечисление 2.txt
def txt2list2():
    with open('Data2.txt', 'r') as Data:
        for line in Data.readlines():
            __Data.append(line.replace('\n', ''))
        # print(__Data)
        print(f'Data2.txt # Contains rows: {len(__Data)}')  # Check for the length of the list


# [1] Intersection # Пересечение множеств
def removedoubles1(_Data, __Data):
    ___Data = list(set(__Data).intersection(set(_Data)))
    print(f'uData.txt # Contains rows: {len(___Data)}')  # Check length of the unique list
    return ___Data


# [2] Difference # Разница A-B
def removedoubles2(_Data, __Data):
    ___Data = list(set(_Data) - set(__Data))
    print(f'uData.txt # Contains rows: {len(___Data)}')  # Check length of the unique list
    return ___Data


# [3] Difference # Разница B-A
def removedoubles3(_Data, __Data):
    ___Data = list(set(__Data) - set(_Data))
    print(f'uData.txt # Contains rows: {len(___Data)}')  # Check length of the unique list
    return ___Data


# [4] Symmetrical Difference # Симметричная разница
def removedoubles4(_Data, __Data):
    ___Data = list(set(__Data).symmetric_difference(set(_Data)))
    print(f'uData.txt # Contains rows: {len(___Data)}')  # Check length of the unique list
    return ___Data


# Write OUT # Запись данных
def write2txtfile(___Data):
    # print(len(___Data))
    # print('This works!')
    with open('uData.txt', 'w') as uData:
        for number in ___Data:
            uData.write(str(number))
            uData.write('\n')


def main():
    global ___Data
    txt2list1()
    txt2list2()

    print("\n############### Data_Double_Checker ###############"
          "\n"
          "\n[1] Intersection # Пересечение множеств"
          "\n[2] Difference # Разница A-B"
          "\n[3] Difference # Разница B-A"
          "\n[4] Symmetrical Difference # Симметричная разница"
          "\n"
          "\n[5] Delete Output"
          "\n[q] Quit\n")

    x = input(">>> ")
    if x == "q":  # [q] Quit
        exit(0)

    # [1] Intersection # Пересечение множеств
    elif x == "1":
        # os.system('cls')
        print("\n[1] Intersection # Пересечение множеств ")
        ___Data = removedoubles1(_Data, __Data)
        print(f'The length of the unique data is: {len(___Data)}')  # Check for the length of the unique list

    # [2] Difference # Разница A-B
    elif x == "2":
        # os.system('cls')
        print("[2] Difference # Разница A-B")
        ___Data = removedoubles2(_Data, __Data)
        print(f'The length of the unique data is: {len(___Data)}')  # Check for the length of the unique list

    # [3] Difference # Разница B-A
    elif x == "3":
        # os.system('cls')
        print("[3] Difference # Разница B-A\n")
        ___Data = removedoubles3(_Data, __Data)
        print(f'The length of the unique data is: {len(___Data)}')  # Check for the length of the unique list

    # [4] Symmetrical Difference # Симметричная разница
    elif x == "4":
        # os.system('cls')
        print("[4] Symmetrical Difference # Симметричная разница")
        ___Data = removedoubles4(_Data, __Data)
        print(f'The length of the unique data is: {len(___Data)}')  # Check for the length of the unique list

    # [5] Delete Output #
    elif x == "5":
        print("[5] Delete Output")
        main()
    else:
        print("Command not Recognized")
        main()

    write2txtfile(___Data)
    # os.system('cls')


if __name__ == '__main__':
    main()
