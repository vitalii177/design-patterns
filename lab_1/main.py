import lab_1 as f
import personal_info as p
import datetime


def main():
    developer = f.Developer(p.personal_info_developer)
    team_leader = f.Developer(p.personal_info_TL)
    quality_assurance = f.QualityAssurance(p.personal_info_QA)
    project_manager = f.ProjectManager(p.personal_info_PM)

    team = f.Team(1, 'KDN23', [developer, team_leader, quality_assurance, project_manager],
                  {}, 1)

    mobile_app = f.MobileApp(title="Chess Game", start_date=datetime.date.today(), team=team)

    mobile_app.add_member(member=developer)

    task1 = f.Task(id=1, title='Add Chess Pieces',
                   deadline=datetime.date(2021, 11, 11),
                   related_project=mobile_app.title)

    task2 = f.Task(id=2, title='Add Logic To the Game',
                   deadline=datetime.date(2021, 1, 20),
                   related_project=mobile_app.title)

    task3 = f.Task(id=3, title='Test',
                   deadline=datetime.date(2021, 12, 1),
                   related_project=mobile_app.title)

    task4 = f.Task(id=4, title='Control a process',
                   deadline=datetime.date(2021, 12, 1),
                   related_project=mobile_app.title)

    task5 = f.Task(id=5, title='Make a diagram',
                   deadline=datetime.date(2021, 12, 1),
                   related_project=mobile_app.title)

    assignment = f.Assignment(project=mobile_app)

    developer.assign(project_to_assign=mobile_app)
    quality_assurance.assign(project_to_assign=mobile_app)
    project_manager.assign(project_to_assign=mobile_app)
    team_leader.assign(project_to_assign=mobile_app)

    developer.set_task(task=task1)
    developer.set_task(task=task2)
    quality_assurance.set_task(task=task3)
    project_manager.set_task(task=task4)
    team_leader.set_task(task=task5)

    print(developer.assigned_project())
    print(assignment.get_task_to_date(date_by=datetime.date(2021, 11, 1)))

    developer.calculate_salary()
    mobile_app.remove_member(member=developer)
    developer.unassign(project_to_assign=mobile_app)
    quality_assurance.calculate_salary()
    quality_assurance.unassign(project_to_assign=mobile_app)
    project_manager.calculate_salary()
    project_manager.unassign(project_to_assign=mobile_app)
    team_leader.calculate_salary()
    team_leader.unassign(project_to_assign=mobile_app)


if __name__ == '__main__':
    main()
