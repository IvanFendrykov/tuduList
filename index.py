import json
from typing import Dict, Any

DATA_FILE = "task.json"
Task = Dict[str, Any]

PRIORITY = {1: "low", 2: "medium", 3: "high"}
PRIORITY_ORDER = {"low": 1, "medium": 2, "high": 3}

STATUS = {1: "new", 2: "in progress", 3: "done"}
STATUS_ORDER = {"new": 1, "in progress": 2, "done": 3}


def load_task() -> Dict[str, Task]:
    try:

        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return data
        else:
            return {}
    except FileNotFoundError:
        return {}


def save_task(tasks: Dict[str, Task]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def new_id(tasks: Dict[str, Task]) -> Any:
    if not tasks:
        return 1

    return str(max(int(k) for k in tasks.keys()) + 1)


def ask_int(prompt: str, *, min_v: int | None = None, max_v: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        if raw == "":
            print("Input number: ")
            continue
        try:
            val = int(raw)
            if min_v is not None and val < min_v:
                print(f"Number can`t be less then {min_v}")
                continue
            if max_v is not None and val > max_v:
                print(f"Number can`t be a bit then {max_v}")
                continue
            return val
        except ValueError:
            print("It`s must be number")


def ask_user(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Can`t be empty")


def priority() -> str:
    print("Choose priority: 1 - low, 2 - middle, 3 - hight")
    p = ask_int("Your chose: ", min_v=1, max_v=3)
    return PRIORITY[p]


def status() -> str:
    print("Choose status: 1 - new, 2 - in process, 3 - done")
    s = ask_int("Your chose: ", min_v=1, max_v=3)
    return STATUS[s]


def print_task(task_id: str, task: Task) -> None:
    print(f" #{task_id}")
    print(f"   Title      : {task["title"]}")
    print(f"   Description: {task["desc"]}")
    print(f"   Priority   : {task["priority"]}")
    print(f"   Status     : {task["status"]}")


def create_task(tasks: Dict[str, Task]) -> None:
    title = ask_user("Input title the task: ")
    desc = ask_user("Input description the task: ")
    prior = priority()
    stat = status()
    tid = new_id(tasks)

    tasks[tid] = {"title": title, "desc": desc, "priority": prior, "status": stat}
    save_task(tasks)
    print("Task was create.")


def vie_task(tasks: Dict[str, Task]) -> None:
    if not tasks:
        print("You don`t have tasks.")
        return

    while True:
        print("\nShow Tasks:")
        print("1 - show all tasks.")
        print("2 - show sorted task(priority).")
        print("3 - show sorted task(status).")
        print("4 - show task for input.")
        print("0 - exit.")
        choise = ask_int("Choose number: ", min_v=0, max_v=4)

        match choise:
            case 0:
                return
            case 1:
                for tid, t in tasks.items():
                    print_task(tid, t)
            case 2:
                items = sorted(
                    tasks.items(),
                    key=lambda k: (PRIORITY_ORDER.get(k[1]["priority"], 99), int(k[0])),
                )
                for tid, t in items:
                    print_task(tid, t)
            case 3:
                items = sorted(
                    tasks.items(),
                    key=lambda k: (STATUS_ORDER.get(k[1]["status"], 99), int(k[0])),
                )
                for tid, t in items:
                    print_task(tid, t)
            case 4:
                user_input = ask_user("Input search param...").lower()
                found = [
                    (tid, t)
                    for tid, t in tasks.items()
                    if user_input in t["title"].lower()
                    or user_input in t["desc"].lower()
                ]
                if not found:
                    print("Any task")
                else:
                    for tid, t in found:
                        print_task(tid, t)


def update_task(tasks: Dict[str, Task]) -> None:
    if not tasks:
        print("Nothing to change")
        return
    tid = ask_user("Input your task id: ")
    if tid not in tasks:
        print(f"You don`t have a task with this id {tid}")
        return

    t = tasks[tid]
    while True:
        print("\nWhat do you want to change: ")
        print("1 - Change title")
        print("2 - Change descriptions")
        print("3 - Change priority")
        print("4 - Change status")
        print("0 - save and exit")

        user_input = ask_int("Choose", min_v=0, max_v=4)

        match user_input:
            case 0:
                save_task(tasks)
                print("Task changed and saved")
                return
            case 1:
                t["title"] = ask_user("New title: ")
            case 2:
                t["desc"] = ask_user("New description: ")
            case 3:
                t["priority"] = priority()
            case 4:
                t["status"] = status()


def delete_task(tasks: Dict[str, Task]) -> None:
    if not tasks:
        print("Anything to delete")
        return

    tid = ask_user("Input your task id: ")

    if tid not in tasks:
        print(f"You don`t have task with this id {tid}")
        return

    confirm = ask_user("You are relly want to delete task: y/n ?").lower()

    if confirm == "y":
        tasks.pop(tid)
        save_task(tasks)
        print("Delete!")

    else:
        print("Canseled")


def main() -> None:
    tasks = load_task()
    print("\nTudu list")
    while True:

        print("\nMenu:")
        print("1 - Create new task")
        print("2 - Show your tasks")
        print("3 - Update task")
        print("4 - Delete task")
        print("0 - Exit")
        user_chose = ask_int("Coose options:", min_v=0, max_v=4)

        match user_chose:
            case 0:
                print("Bye.")
                break
            case 1:
                create_task(tasks)
            case 2:
                vie_task(tasks)
            case 3:
                update_task(tasks)
            case 4:
                delete_task(tasks)


main()
