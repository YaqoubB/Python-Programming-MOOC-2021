# Write your solution here
# If you use the classes made in the previous exercise, copy them here

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
        return  [task for task in self.total_tasks if task.state is True]


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


###############################################################################################################################################

class OrderBookApplication:
    def __init__(self):
        self.orderbook = OrderBook()


    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def adding_order(self):
        description = str(input("description: "))
        prog_work = str(input("programmer and workload estimate: "))
        prog_work = prog_work.split(" ")
        programmer = str(prog_work[0])
        try:
            workload = int(prog_work[1])
            self.orderbook.add_order(description, programmer, workload)
            print("added!")
        except:
            print("erroneous input")
        
        

        
    def list_finished_tasks(self):
        finished = self.orderbook.finished_orders()
        if len(finished) == 0:
            print("no finished tasks")
        else:
            for task in finished:
                print(task)
        

    def list_unfinished_tasks(self):
        unfinished = self.orderbook.unfinished_orders()
        if len(unfinished) == 0:
            print("no unfinished tasks")
        else:
            for task in unfinished:
                print(task)

    def mark_task_as_finished(self):
        try:
            id = int(input("id: "))
            self.orderbook.mark_finished(id)
            print("marked as finished")
        except:
            print("erroneous input")

        
    def programmerz(self):
        for programmer in self.orderbook.programmers():
            print(programmer)
       

    def programmer_status(self):
        try:
            programmer = str(input("programmer: "))
            status = self.orderbook.status_of_programmer(programmer)
            print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
        except:
            print("erroneous input")
        

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.adding_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks() 
            elif command == "4":
                self.mark_task_as_finished()
            elif command == "5":
                self.programmerz() 
            elif command == "6":
                self.programmer_status()
            else:
                self.help()


application = OrderBookApplication()
application.execute()




