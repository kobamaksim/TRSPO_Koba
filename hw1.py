import threading

def greet():
    print("Коба Максим КІ-22")

# Функція для обчислення суми чисел від 0 до 99
def calculate_summ():
    summ = 0
    for i in range(100):
        print(f"{summ} + {i} = ", end="")
        summ += i
        print(f"{summ}")

# Функція для обчислення кубів чисел від 0 до 99
def calculate_cube():
    for i in range(100):
        print(f"Cube of {i}: {i ** 3}")

if __name__ == "__main__":
    greet()

    thread1 = threading.Thread(target=calculate_summ)
    thread2 = threading.Thread(target=calculate_cube)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Обчислення завершено.")
