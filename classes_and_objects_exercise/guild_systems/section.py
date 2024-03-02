from project.task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        length_of_section = 0
        for task in self.tasks:
            if task.completed:
                length_of_section += 1
                self.tasks.remove(task)
        return f"Cleared {length_of_section} tasks."

    def view_section(self):
        formated_details = "\n".join(task.details() for task in self.tasks)
        return f"Section {self.name}:\n" + formated_details
