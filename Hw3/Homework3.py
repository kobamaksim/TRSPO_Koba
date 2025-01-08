from concurrent.futures import ThreadPoolExecutor
import time

def compute_collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def main():
    max_number = 10000
    number_of_threads = 4

    total_steps = 0
    count = 0

    start_time = time.time()

    def task(number):
        nonlocal total_steps, count
        steps = compute_collatz_steps(number)
        total_steps += steps
        count += 1

    with ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        executor.map(task, range(1, max_number + 1))

    average_steps = total_steps / count if count > 0 else 0

    end_time = time.time()
    print(f"Середня кількість кроків для виродження в 1: {average_steps}")
    print(f"Час виконання: {end_time - start_time:.2f} сек.")

if __name__ == "__main__":
    main()
