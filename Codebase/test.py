import random
import time
import tkinter
from multiprocessing import Process, Queue


class Interface():
    def __init__(self, queue):
        self.queue = queue
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=500, height=500)
        self.squares = []
        self.create_squares()

    def create_squares(self):
        coords = [(3, 0, 4, 1), (4, 0, 5, 1), (5, 0, 6, 1), (3, 1, 4, 2), (4, 1, 5, 2)]
        for j in range(5):
            self.squares.append(
                self.canvas.create_rectangle(*tuple((i * 40) + 40 for i in coords[j]), fill='red', outline='white'))
        self.canvas.pack()

    def update_square(self):
        while not self.queue.empty():
            color = self.queue.get()
            print(color)
            self.canvas.itemconfig(self.squares[0], fill=color)
            time.sleep(0.5)
            self.root.update_idletasks()
            self.root.update()


def create_data(queue):
    color_list = ['white', 'orange', 'red', 'green', 'blue', 'yellow']
    data_count = 0
    while data_count < 20:
        rand_color = random.choice(color_list)
        queue.put(rand_color)
        print('.', end='')
        data_count += 1
        time.sleep(0.25)
    print('data completed')


def main():
    position_queue = Queue()
    p = Process(target=create_data, args=(position_queue,))
    p.start()
    # p.join()

    window = Interface(position_queue)
    window.root.after(1000, window.update_square)
    window.root.mainloop()
    # window.root.update_idletasks()
    # window.root.update()

    # number_of_task = 10
    # number_of_processes = 4
    # tasks_that_are_done = Queue()
    # processes = []
    #
    # for i in range(number_of_task):
    #     tasks_to_accomplish.put("Task no " + str(i))
    #
    # # creating processes
    # for w in range(number_of_processes):
    #     p = Process(target=do_job, args=(tasks_to_accomplish, tasks_that_are_done))
    #     processes.append(p)
    #     p.start()
    #
    # # completing process
    # for p in processes:
    #     p.join()


if __name__ == '__main__':
    main()
