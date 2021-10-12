from abc import ABC, abstractmethod
from dataclasses import dataclass
import datetime


@dataclass
class PersonalInfo:
    id: int
    name: str
    address: str
    phone_number: str
    email: str
    position: str
    rank: str
    salary: float


class Employee(ABC):
    def __init__(self, personal_info: PersonalInfo) -> None:
        self._personal_info = personal_info
        self.assignments = []

    @property
    def personal_info(self) -> PersonalInfo:
        return self._personal_info

    @personal_info.setter
    def personal_info(self, personal_info: PersonalInfo) -> None:
        if isinstance(personal_info, PersonalInfo):
            self._personal_info = personal_info
        else:
            raise AttributeError('Cannot set non PersonalInfo object')

    @staticmethod
    def assign_possibility(self, project) -> bool:
        if project.ENGINEERS_LIMIT > len(project.developers):
            return True
        else:
            return False

    def assigned_project(self) -> list:
        assigned_project = [assignment.project
                            for assignment in self.assignments]
        return assigned_project

    def assign(self, project_to_assign) -> None:
        project_to_assign.developers.append(self._personal_info.id)
        assignment = Assignment(project_to_assign)
        self.assignments.append(assignment)
        print(f"{project_to_assign.title} has been assigned to Employee with"
              f" id {self._personal_info.id}")

    def unassign(self, project_to_assign) -> None:
        for i in range(len(self.assignments)):
            if self.assignments[i].project == project_to_assign:
                del self.assignments[i]
                print(f"Assignment with project {project_to_assign.title}"
                      f" has been removed!")
                return


class Developer(Employee):
    def __init__(self, personal_info: PersonalInfo) -> None:
        super().__init__(personal_info)
        self.tasks = []
        self.salary = 0.0

    def calculate_tax(self) -> float:
        return 0.2

    def calculate_salary(self) -> None:
        self.salary += self.personal_info.salary * len(self.tasks) * (1 - self.calculate_tax())
        print("Salary of developer {0}: {1}".format(self.personal_info.name, self.salary))

    def set_task(self, task) -> None:
        self.tasks.append(task)


class Task:
    def __init__(self, id: int, title: str, deadline: datetime,
                 related_project: str) -> None:
        self.id = id
        self.title = title
        self.deadline = deadline
        self.items = []
        self.status = 0.0
        self.related_project = related_project
        self.comment = None

    def implement_item(self, item_name: str) -> float:
        implemented_items = 0
        for i in range(len(self.items)):
            if self.items == item_name:
                implemented_items += 1
        return implemented_items / len(self.items)

    def add_comment(self, comment: str) -> None:
        self.comment = comment


class Assignment:
    def __init__(self, project) -> None:
        self.project = project
        self.received_tasks = {}

    def get_task_to_date(self, date_by: datetime) -> list[Task]:
        list_of_projects = []
        for date, project in self.received_tasks.items():
            if date_by <= date:
                list_of_projects.append(project)
        return list_of_projects


class Project:
    def __init__(self, title: str, start_date: datetime) -> None:
        self.title = title
        self.start_date = start_date
        self.task_list = []
        self.developers = []

    def add_developer(self, developer: Developer) -> None:
        if developer not in self.developers:
            self.developers.append(developer)
            print(f"{developer.personal_info.name} has added successfully!")

    def remove_developer(self, developer: Developer) -> None:
        for i in range(len(self.developers)):
            if self.developers[i] == developer:
                del self.developers[i]
                print(f"{developer.personal_info.name} has removed successfully!")
                return


class QualityAssurance(Employee):
    def __init__(self, personal_info: PersonalInfo) -> None:
        super().__init__(personal_info)
        self.tasks = []
        self.salary = 0.0

    def calculate_tax(self) -> float:
        return 0.2

    def calculate_salary(self) -> None:
        self.salary += self.personal_info.salary * len(self.tasks) * (1 - self.calculate_tax())
        print("Salary of QA {0}: {1}".format(self.personal_info.name, self.salary))

    def set_task(self, task: Task) -> None:
        self.tasks.append(task)

    def add_ticket(self) -> None:
        pass


class ProjectManager(Employee):
    def __init__(self, personal_info: PersonalInfo) -> None:
        super().__init__(personal_info)
        self.tasks = []
        self.salary = 0.0

    def calculate_tax(self) -> float:
        return 0.1

    def calculate_salary(self) -> None:
        self.salary += self.personal_info.salary * len(self.tasks) * (1 - self.calculate_tax())
        print("Salary of PM {0}: {1}".format(self.personal_info.name, self.salary))

    def set_task(self, task: Task) -> None:
        self.tasks.append(task)

    def discuss_progress(self, engineer: Employee) -> None:
        pass
