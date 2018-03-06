import time
from multiprocessing import Process, Manager, Pool, cpu_count
from sqlite3 import IntegrityError

from data.database_manager import DatabaseManager


def work_function(x, queue):
    queue.put(int(x * (5 / 3)))
    print('.', end='')
    time.sleep(0.01)


def queue_getter(queue):
    db = DatabaseManager('PC/data/test_db.sqlite')

    db.query('DROP TABLE IF EXISTS test')
    db.query('''CREATE TABLE IF NOT EXISTS test (value INTEGER NOT NULL)''')

    while not queue.empty():
        result = queue.get()
        try:
            db.query('INSERT INTO test VALUES (?)', (result,))
        except IntegrityError:
            pass

    db.commit()


def main():
    queue = Manager().Queue()

    test_list = [x * 3 for x in range(10000)]
    iterable = map(lambda e: (e, queue), test_list)

    p = Pool(processes=cpu_count() - 1)
    p.starmap(work_function, iterable)

    time.sleep(0.5)
    db_process = Process(target=queue_getter, args=(queue,))
    db_process.start()
    # db_process.join()
    while not queue.empty():
        pass
    p.close()
    time.sleep(10)


if __name__ == '__main__':
    main()
