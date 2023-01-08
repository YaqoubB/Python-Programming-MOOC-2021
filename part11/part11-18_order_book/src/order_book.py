
# Write your solution here:

class Task:
    id = 0
    def __init__(self, description: str, programmer: str, workload: int, state = False):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.state = state
        self.id = self.set_id()
    
    def set_id(self):
        Task.id += 1
        return int(Task.id)

    def is_finished(self):
        return self.state

    def mark_finished(self):
        self.state = True
    
    def __str__(self):
        state = "NOT FINISHED"
        if self.state:
            state = "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {state}"

class OrderBook:
    def __init__(self):
        self.total_tasks = []
        
    def add_order(self, description: str, programmer: str, workload: int):
            self.total_tasks.append(Task(description, programmer, workload))

    def all_orders(self):
        if len(self.total_tasks) == 0:
            return None
        return self.total_tasks

    def programmers(self):
        return list(set([task.programmer for task in self.total_tasks]))

    def mark_finished(self, id: int):
        task = [ task for task in self.total_tasks if task.id == id]
        if len(task) == 0:
            raise ValueError
        task = task[0].mark_finished()
        

    def finished_orders(self):
        return [task for task in self.total_tasks if task.state is True]

    def unfinished_orders(self):
        return [task for task in self.total_tasks if task.state is False]

    def status_of_programmer(self, programmer: str):
        if len([task for task in self.total_tasks if task.programmer == programmer]) == 0:
            raise ValueError
        finished = [task for task in self.total_tasks if task.programmer == programmer and task.state is True]
        fin_hours = sum([task.workload for task in finished ])
        unfinished = [task for task in self.total_tasks if task.programmer == programmer and task.state is False]
        unfin_hours = sum([task.workload for task in unfinished])
        return (len(finished), len(unfinished), fin_hours, unfin_hours)

if __name__ == "__main__":
    t1 = Task("program hello world", "Eric", 3)
    print(t1.id, t1.description, t1.programmer, t1.workload)
    print(t1)
    print(t1.is_finished())
    t1.mark_finished()
    print(t1)
    print(t1.is_finished())
    t2 = Task("program webstore", "Adele", 10)
    t3 = Task("program mobile app for workload accounting", "Eric", 25)
    print(t2)
    print(t3)

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    for order in orders.all_orders():
        print(order)

    print()

    for programmer in orders.programmers():
        print(programmer)

    t = OrderBook()
    t.add_order("program web store", "Andy", 10)
    t.add_order("program mobile game", "Eric", 5)
    t.all_orders()

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    orders.mark_finished(1)
    orders.mark_finished(2)

    for order in orders.all_orders():
        print(order)

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)