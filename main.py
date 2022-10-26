def bubble_sort(array: list) -> None:
    for i in range(len(array)):
        swapped: bool = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    while True:
        n: int = int(input("Enter the size of sequences : "))
        input_raw_data: list = list(map(float, input("Enter the list numbers separated by space : ").strip().split()))
        if len(input_raw_data) > n:
            print("Warning: the size of sequences are too many values.")
            print(f"{len(input_raw_data) - n} ပိုများနေတယ်။")
        numList: list = input_raw_data[:n]
        print("User List: ", numList)
        print(f'Original Array : {numList}')
        bubble_sort(numList)
        print("*" * 10)
        print(f'Sorted Array in Ascending Order : {numList}\n')
