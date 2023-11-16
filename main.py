from concurrent.futures import ThreadPoolExecutor

from brute import BruteForce


def run_in_parallel(tasks):
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()


if __name__ == '__main__':
    run_in_parallel([
        lambda: BruteForce("store-1/CAT-1.log").main(),
        # lambda: BruteForce("store-1/CAT-2.log").main(),
        # lambda: BruteForce("store-1/CAT-3.log").main(),
        # lambda: BruteForce("store-1/CAT-4.log").main(),
        # lambda: BruteForce("store-1/CAT-5.log").main(),
        # lambda: BruteForce("store-1/CAT-6.log").main(),
        # lambda: BruteForce("store-1/CAT-7.log").main(),
        # lambda: BruteForce("store-1/CAT-8.log").main(),
        # lambda: BruteForce("store-1/CAT-9.log").main(),
        # lambda: BruteForce("store-1/CAT-10.log").main(),
    ])
