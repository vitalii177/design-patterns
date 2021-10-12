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


@dataclass
class Team:
    id: int
    name: str
    member_list: list
    supplementary_materials: dict
    project_id: int


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
        project_to_assign.members.append(self._personal_info.id)
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
            if self.items[i] == item_name:
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


class Project(ABC):
    def __init__(self, title: str, start_date: datetime, team: Team) -> None:
        self.title = title
        self.start_date = start_date
        self._team = team
        self.task_list = []
        self.members = []

    @property
    def team(self) -> Team:
        return self._team

    @team.setter
    def team(self, team: Team) -> None:
        if isinstance(team, Team):
            self._team = team
        else:
            raise AttributeError('Cannot set non PersonalInfo object')

    def add_member(self, member: Employee) -> None:
        if member not in self.members:
            self.members.append(member)
            self.team.member_list.append(member)
        print(f"Member has added successfully!")

    def remove_member(self, member: Employee) -> None:
        for i in range(len(self.members)):
            if self.members[i] == member:
                del self.members[i]
                break
        for i in range(len(self.team.member_list)):
            if self.team.member_list[i] == member:
                del self.team.member_list[i]
                break
        print(f"Member has removed successfully!")

    @abstractmethod
    def send_supplementary_materials(self, task_id: int, material: str) -> None:
        pass


class WebApp(Project):
    def __init__(self, title: str, start_date: datetime, team: Team) -> None:
        super().__init__(title, start_date, team)

    def send_supplementary_materials(self, task_id: int, material: str) -> None:
        self.team.supplementary_materials[task_id].append(material)


class MobileApp(Project):
    def __init__(self, title: str, start_date: datetime, team: Team) -> None:
        super().__init__(title, start_date, team)

    def send_supplementary_materials(self, task_id: int, material: str) -> None:
        self.team.supplementary_materials[task_id].append(material)


class ProjectFlow(Project):
    def __init__(self, title: str, start_date: datetime, team: Team) -> None:
        super().__init__(title, start_date, team)

    def send_supplementary_materials(self, task_id: int, material: str) -> None:
        self.team.supplementary_materials[task_id].append(material)


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


class TeamLead(Employee):
    def __init__(self, personal_info: PersonalInfo) -> None:
        super().__init__(personal_info)
        self.tasks = []
        self.salary = 0.0

    def calculate_tax(self) -> float:
        return 0.01

    def calculate_salary(self) -> None:
        self.salary += self.personal_info.salary * len(self.tasks) * (1 - self.calculate_tax())
        print("Salary of TeamLead {0}: {1}".format(self.personal_info.name, self.salary))

    def set_task(self, task: Task) -> None:
        self.tasks.append(task)


class TopManagement(ABC):
    def __init__(self, personal_info: PersonalInfo) -> None:
        self._personal_info = personal_info

    @property
    def personal_info(self) -> PersonalInfo:
        return self._personal_info

    @personal_info.setter
    def personal_info(self, personal_info: PersonalInfo) -> None:
        if isinstance(personal_info, PersonalInfo):
            self._personal_info = personal_info
        else:
            raise AttributeError('Cannot set non PersonalInfo object')

    def fill_project(self, team_lead: TeamLead, team: Team) -> None:
        projects_to_fill = self.attach_project(team)
        for p in projects_to_fill:
            p.add_member(team_lead)

    @abstractmethod
    def attach_project(self, *args) -> list[Project]:
        pass


class ChiefTechnicalOfficer(TopManagement):
    def attach_project(self, *args) -> list[ProjectFlow]:
        title, start_date, team = args
        return [ProjectFlow(title, start_date, team)]


class SolutionArchitect(TopManagement):
    def attach_project(self, *args) -> list[WebApp, MobileApp]:
        title, start_date, team = args
        return [WebApp(title, start_date, team),
                MobileApp(title, start_date, team)]