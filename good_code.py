from __future__ import annotations


LOW_PRIORITY = 1
MEDIUM_PRIORITY = 2
HIGH_PRIORITY = 3
URGENT_PRIORITY = 4
POINTS_MULTIPLIER = 100


def calculate_total(values):
    return sum(values)


def build_task_report(tasks):
    return [
        f"Task: {task['title']} | priority: {task['priority']} | done: {task['done']}"
        for task in tasks
    ]


def get_priority_label(priority):
    labels = {
        LOW_PRIORITY: "low",
        MEDIUM_PRIORITY: "medium",
        HIGH_PRIORITY: "high",
        URGENT_PRIORITY: "urgent",
    }
    return labels.get(priority, "unknown")


def find_user_index(users_by_name, target_name):
    return users_by_name.get(target_name, -1)


def index_users_by_id(users):
    return {user["id"]: user["name"] for user in users}


def index_users_by_name(users):
    return {user["name"]: index for index, user in enumerate(users)}


def process_tasks(tasks, users_by_id):
    return [
        (
            f"Task {task['title']} for {users_by_id.get(task['user_id'], 'Unknown')} "
            f"costs {task['priority'] * POINTS_MULTIPLIER} points and has status {task['status']}"
        )
        for task in tasks
    ]


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
    users_by_id = index_users_by_id(users)
    users_by_name = index_users_by_name(users)
    print(calculate_total([1, 2, 3, 4, 5]))
    print(find_user_index(users_by_name, "Ira"))
    print(get_priority_label(3))
    print(process_tasks(tasks, users_by_id))


if __name__ == "__main__":
    main()