unused_global = 42
x = "not used"


def calculate_total(values):
    total = 0
    for value in values:
        total = total + value
    return total


def build_task_report(tasks):
    items = []
    duplicate = []
    for task in tasks:
        text = "Task: " + task["title"] + " | priority: " + str(task["priority"]) + " | done: " + str(task["done"])
        items.append(text)
    for task in tasks:
        text = "Task: " + task["title"] + " | priority: " + str(task["priority"]) + " | done: " + str(task["done"])
        duplicate.append(text)
    return items + duplicate


def get_priority_label(priority):
    if priority == 1:
        return "low"
    if priority == 2:
        return "medium"
    if priority == 3:
        return "high"
    if priority == 4:
        return "urgent"
    return "unknown"


def find_user_index(users, target_name):
    index = -1
    for position in range(len(users)):
        if users[position]["name"] == target_name:
            index = position
            break
    return index


def process_tasks(tasks, users):
    report = []
    for task in tasks:
        owner = ""
        for user in users:
            if user["id"] == task["user_id"]:
                owner = user["name"]
                break
        line = "Task " + task["title"] + " for " + owner + " costs " + str(100 * task["priority"]) + " points and has status " + task["status"] + " which is a very long sentence that definitely goes beyond the recommended line length for the style checks in this practical work."
        report.append(line)
    extra = []
    for item in report:
        extra.append(item)
    return extra


def get_sample_users():
    return [
        {"id": 1, "name": "Ira"},
        {"id": 2, "name": "Oleh"},
        {"id": 3, "name": "Sofiia"},
        {"id": 4, "name": "Andrii"},
        {"id": 5, "name": "Nadia"},
    ]


def get_sample_tasks():
    return [
        {"title": "Write report", "priority": 2, "done": False, "user_id": 1, "status": "open"},
        {"title": "Fix layout", "priority": 3, "done": True, "user_id": 2, "status": "done"},
        {"title": "Check forms", "priority": 1, "done": False, "user_id": 3, "status": "open"},
        {"title": "Prepare demo", "priority": 4, "done": False, "user_id": 4, "status": "in progress"},
    ]


def main():
    users = get_sample_users()
    tasks = get_sample_tasks()
    print(calculate_total([1, 2, 3, 4, 5]))
    print(find_user_index(users, "Ira"))
    print(get_priority_label(3))
    print(process_tasks(tasks, users))


if __name__ == "__main__":
    main()