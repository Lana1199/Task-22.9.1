#1.Преобразование введенной последовательности в список
try:
    numbers = [float(x) for x in input("Введите целые числа в любом порядке, через пробел: ").split()]
    random_num = float(input('Введите любое целое число:'))
except ValueError:
    print("Ошибка! Повторите ввод - принимаются только числа! ")
else:
     def sort_ascending(numbers):
         for i in range(len(numbers)):  # проходим по всему массиву
             idx_min = i  # сохраняем индекс предположительно минимального элемента
             for j in range(i, len(numbers)):
                 if numbers[j] < numbers[idx_min]:
                     idx_min = j
             if i != idx_min:  # если индекс не совпадает с минимальным, меняем
                 numbers[i], numbers[idx_min] = numbers[idx_min], numbers[i]

sort_ascending(numbers)
print(f'''Список чисел отсортированый по возрастанию: {numbers}''')

#3.Устанавливается номер позиции элемента.
def binary_search(numbers, random_num, left, right):
    try:
        if left > right:  # если левая граница превысила правую,
            return False  # значит элемент отсутствует
        middle = (right + left) // 2  # находим середину
        if numbers[middle] == random_num:# если элемент в середине,
            return middle     # возвращаем этот индекс
        elif random_num < numbers[middle]:  # если элемент меньше элемента в середине
            return binary_search(numbers, random_num, left, middle - 1)  # рекурсивно ищем в левой половине
        else:  # иначе в правой
            return binary_search(numbers, random_num, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'

#4.Устанавливается номер позиции элемента,который меньше введенного пользовательского числа, а затем за ним больше или соответствует этому значению.

if not binary_search(numbers, random_num, 0, len(numbers)):
    rI = min(numbers, key=lambda x: (abs(x - random_num), x))
    ind = numbers.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < random_num:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {numbers[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {numbers.index(rI)}
В списке нет меньшего элемента''')
    elif rI > random_num:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {numbers.index(rI)}
Ближайший меньший элемент: {numbers[min_ind]} его индекс: {min_ind}''')
    elif numbers.index(rI) == 0:
        print(f'Индекс введенного элемента: {numbers.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(numbers, random_num, 0, len(numbers))}')







