
def write(text):
    with open("data.txt", "a", encoding="utf-8") as f:
        f.writelines(text)
        f.writelines("\n")
        print("Успешно")

def read_all():
    # if "data.txt".exists():
    with open("data.txt", "r", encoding="utf-8") as f:
        # f.readlines()
        for line in f:
            print(line)

def get_by_name(name):
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            if name in line:
                print(line)

def delete(teg):
    check = False
    with open("data.txt",'r',encoding = 'utf-8') as f:
       arr = [line for line in f.readlines()]
       for i in range(len(arr)):
           if teg in arr[i]:
               check = True
               arr[i-1], arr[i], arr[i+1], arr[i+2], arr[i+3], arr[i+4] = '', '', '', '', '', ''
    if check == True:
        with open("data.txt",'w',encoding = 'utf-8') as f:
            f.writelines(arr)
            return print(f'Данные пользователя "{teg}" удалены!')
    return print(f'По pзапросу "{teg}" ничего не найдено!')

def change(teg, diction, new_teg):
    check = False
    dict = {'1': 'Фамилия:', '2': 'Имя:', '3': 'Отчество:', '4': 'Номер телефона:'}
    if diction not in dict.keys():
        return print(f'Ваше значение "{diction}" не подходит условию!')
    with open("data.txt",'r',encoding = 'utf-8') as f:
        arr = [line for line in f.readlines()]
        for i in range(len(arr)):
            if teg in arr[i]:
                check = True
                if diction == '1': arr[i] = dict[diction] + ' ' + new_teg + '\n'
                if diction == '2': arr[i+1] = dict[diction] + ' '  + new_teg + '\n'
                if diction == '3': arr[i+2] = dict[diction] + ' '  + new_teg + '\n'
                if diction == '4': arr[i+3] = dict[diction] + ' '  + new_teg + '\n'    
    if check == True:               
        with open("data.txt",'w',encoding = 'utf-8') as f:
            f.writelines(arr)
            return print(f'Данные пользователя "{teg}" изменены!')
    else: return print(f'По запросу "{teg}" ничего не найдено!')


def choose(choice):
    if choice == '1': return write(input("Введите ваши данные пример:(фамилия имя отчество номер телефона)"))
    if choice == "2": return read_all()
    if choice == "3": return get_by_name(input("Введите имя или фамилию "))
    if choice == "4": return delete(input("Введите фамилию для удаления данных "))
    if choice == "5": return change(input('Введите Фамилию для изменения данных -> '), 
                                    input('Введите что вы хотите изменить (1 - Фамилия, 2 - Имя, 3 - Отчество, 4 - Номер) -> ') , 
                                    input('Введите новые данные -> '))
    if choice == "6": exit()