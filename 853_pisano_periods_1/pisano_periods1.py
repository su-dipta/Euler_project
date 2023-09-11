import multiprocessing


def pisano_period_length(n):
    a, b = 0, 1
    period = 0
    for i in range(2, n * n + 1):
        a, b = b, (a + b) % n
        if a == 0 and b == 1:
            period = i - 1
            break
    return period


def calculate_periods(start, end, results):
    for n in range(start, end):
        if n % 2 == 0:
            period_length = n
        elif n % 5 == 0:
            period_length = 20 * (n // 5)
        else:
            period_length = pisano_period_length(n)

        results[n - start] = period_length


def sum_of_n_with_pisano_period(target_period, limit):
    sum_of_n = 0
    num_processes = multiprocessing.cpu_count()
    chunk_size = (limit - 2) // num_processes + 1

    with multiprocessing.Manager() as manager:
        results = manager.list([0] * (limit - 2))

        processes = []
        for i in range(num_processes):
            start = 2 + i * chunk_size
            end = min(start + chunk_size, limit)
            process = multiprocessing.Process(target=calculate_periods, args=(start, end, results))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        for n, period_length in enumerate(results):
            if period_length == target_period:
                sum_of_n += n + 2

    return sum_of_n


target_period = 120
limit = 100000
result = sum_of_n_with_pisano_period(target_period, limit)
print(result)

