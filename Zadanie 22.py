def search(arr,target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return left

def sort_list(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
posled = input("Введите последовательность чисел ")
target_num = int(input("Введите число для поиска "))

numbers = list(map(int, posled.split()))
sort_list(numbers)

position = search(numbers, target_num)
if position < len(numbers):
    print("Позиция элемента - ", position)
    print("Найденное число - ", numbers[position])
else:
    print("Число не найдено")

