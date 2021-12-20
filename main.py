import numpy as np

if __name__ == '__main__':
    input_arr = np.array([])
    # читаем файл и складываем числа в массив
    # 3307.TXT
    # 3307-AK.TXT
    # 4470.TXT
    # 4470-AK.TXT
    # Swd546.pro
    # Vd546.pro
    with open("Vd546.pro") as file:
        for line in file:
            if len(line.strip()) != 0:
                input_arr = np.append(input_arr, int(line.strip()))

    # пробегаемся по n от 1 до длины массива (теоретически самого большого возможного n)
    n = 1
    while n != len(input_arr):
        checked_and_not_found = False
        found = False
        print("n =", n)
        for current_index in range(1, len(input_arr) - n):
            found = False
            # создаем массив, который будем проверять с предыдущими
            test_arr = input_arr[current_index:current_index + n]
            for window_index in range(0, current_index):
                window_arr = input_arr[window_index:window_index + n]
                if np.array_equal(window_arr, test_arr):
                    print("Arrays", window_arr, "and", test_arr, "are equal. ",
                          "Current_index =", current_index, "window_index =", window_index)
                    found = True
                    break

            if found:
                n = n + 1
                break
        else:
            if not found:
                print("Not found", n, "digit duplicates")
                checked_and_not_found = True
        if checked_and_not_found:
            print("Answer:", n - 1)
            break
