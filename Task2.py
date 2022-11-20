# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.

def summa(x,y):
    return x+y

def dif(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y

def get_operation(x,oper,y):
    operations = {'+':summa,'-': dif,'*': mult,'/':div}
    return_operations = operations.get(oper)
    if not return_operations:
        print('Такой операции не предусмотрено')
    return return_operations(x,y)

def get_expression(exp:str):
    result_list = []
    numbers = ''
    for s in exp:
        if s.isdigit():
            numbers += s
        elif s in ['(',')']:
            if numbers:
                result_list.append(int(numbers))
                numbers = ''
            result_list.append(s)
        else:
            if numbers:
                result_list.append(int(numbers))
                numbers = ''
            result_list.append(s)
    else:
        if numbers:
            result_list.append(int(numbers))
    return result_list

def calculate(res_list):
    result = 0
    for i in "*/+-":
        while i in res_list:
            index = res_list.index(i)
            result = get_operation(res_list[index - 1],i,res_list[index+1])
            res_list = res_list[:index - 1] + [result] + res_list[index+2:]
            # print(res_list)
    return result

# try:
expression = input('Введите, пожалуйста, числовое выражение, используя знаки +-*/: ')
new_exp = calculate(get_expression(expression))
print(f'Результат вычисления {expression} равен: {new_exp}')
# except:
    # print('Возможно, Вы неверно ввели числовое выражение, необходимо ввести выражение в формате: 2+2*2 или со скобками 2+(2*2)')




    




