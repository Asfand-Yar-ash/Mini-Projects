from dataclasses import dataclass
from dataclasses import field
@dataclass(init=True, repr=True, eq=True, frozen=False, slots=True)
class To_Do_list:
    task: list = field(default_factory=list, init=False, repr=True) # type: ignore
    def add_task(self, new_task: str) -> None:
        self.task.append(new_task)
    def remove_task(self, task_to_remove: str) -> None:
        self.task.remove(task_to_remove)
    def show_tasks(self) -> list:
        return self.task

class Interface:
    def Interface_title(self):
        print(" "*10+"TO do List")
    def Horizontal_Border(self):
        print("-" * 30)
    def Vertical_Border_left(self):
        print("|", end="")
    def Vertical_Border_right(self):
        print(" " * 28 + "|")

def To_Do_list_UI(work: To_Do_list):
    ui = Interface()
    ui.Horizontal_Border()
    ui.Interface_title()
    ui.Vertical_Border_left()
    print(" Tasks :", work.show_tasks())
    ui.Vertical_Border_right()
    ui.Horizontal_Border()


def main():
    work = To_Do_list()
    while True:
        To_Do_list_UI(work)
        action = input("Would you like to add or remove a task? (add/remove/quit): ").strip().lower()

        if action == "add":
            new_task = input("Enter the task to add: ").strip()
            work.add_task(new_task)

        elif action == "remove":
            task_to_remove = input("Enter the task to remove: ").strip()
            work.remove_task(task_to_remove)

        elif action == "quit":
            print("Exiting the To-Do List application.")
            break

        else:
            print("Invalid action. Please enter add, remove, or quit.")


if __name__ == "__main__":
    main()

