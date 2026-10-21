tasks = []

def add_task(task_name, tags):
    task = {"task": task_name, "tags": set(tags)}
    tasks.append(task)

def display_all():
    for task in tasks:
        print(task["task"], "-", task["tags"])

def find_by_tag(tag):
    for task in tasks:
        if tag in task["tags"]:
            print(task["task"])

add_task("Finish Python assignment", ["study", "college"])
add_task("Buy notebook", ["shopping"])
add_task("Practise loops", ["study", "python"])

display_all()
print("Tasks tagged study:")
find_by_tag("study")
