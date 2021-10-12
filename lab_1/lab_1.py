import datetime


class Developer:
    def __init__(self, id: int, name: str, address: str, phone_number: str,
                 email: str, position: str, rank: str, salary: float) -> None:
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.position = position
        self.rank = rank
        self.salary = salary
        self.assignments = []

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
        project_to_assign.developers.append(self.id)
        assignment = Assignment(project_to_assign)
        self.assignments.append(assignment)
        print(f"{project_to_assign.title} has been assigned to Employee with"
              f" id {self.id}")

    def unassign(self, project_to_assign) -> None:
        for i in range(len(self.assignments)):
            if self.assignments[i].project == project_to_assign:
                del self.assignments[i]
                print(f"Assignment with project {project_to_assign.title}"
                      f" has been removed!")
                return


class Assignment:
    def __init__(self, project) -> None:
        self.project = project
        self.received_tasks = {}

    def get_task_to_date(self, date_by: datetime) -> list:
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
            print(f"Developer {developer.name} has added successfully!")

    def remove_developer(self, developer: Developer) -> None:
        for i in range(len(self.developers)):
            if self.developers[i] == developer:
                del self.developers[i]
                print(f"Developer {developer.name} has removed successfully!")
                return


class QualityAssurance(Developer):
    def __init__(self, id: int, name: str, address: str, phone_number: str,
                 email: str, rank: str, position: str, salary: float, project: Project):
        super().__init__(id, name, address, phone_number, email, rank, position, salary)
        self.project = project


class ProjectManager(Developer):
    def __init__(self, id: int, name: str, address: str, phone_number: str,
                 email: str, rank: str, position: str, salary: float, project: Project):
        super().__init__(id, name, address, phone_number, email, rank, position, salary)
        self.project = project

    def discuss_progress(self, developer: Developer):
        pass
