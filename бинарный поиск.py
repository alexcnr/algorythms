

def binary_search(list, item):
    """ПОЛУЧАЕТ ОТСОРТИРОВАННЫЙ МАССИВ И ЗНАЧЕНИЕ,
    ЕСЛИ ЗНАЧЕНИЕ ЕСТЬ В МАССИВЕБ ТО ВОЗВРАЩАЕТ ЕГО ПОЗИЦИЮ"""
    low = 0   #диапазон поиска от
    high = len(list) - 1  # и до

    while low <= high:
        mid = int((low + high) / 2) #среднее
        guess = list[mid] #номер элемента массива, полученного среднего
        
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        
    return None
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]

print(binary_search(my_list, 13))

