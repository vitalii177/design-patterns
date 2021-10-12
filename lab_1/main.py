import lab_1 as f
import personal_info as p
import datetime


def main():
    developer = f.Developer(p.personal_info_developer)

    project = f.Project(title="Chess Game", start_date=datetime.date.today())

    quality_assurance = f.QualityAssurance(p.personal_info_QA)
    project_manager = f.ProjectManager(p.personal_info_PM)

    project.add_developer(developer=developer)

    task1 = f.Task(id=1, title='Add Chess Pieces',
                   deadline=datetime.date(2021, 11, 11),
                   related_project=project.title)

    task2 = f.Task(id=2, title='Add Logic To the Game',
                   deadline=datetime.date(2021, 1, 20),
                   related_project=project.title)

    task3 = f.Task(id=3, title='Test',
                   deadline=datetime.date(2021, 12, 1),
                   related_project=project.title)

    task4 = f.Task(id=4, title='Control a process',
                   deadline=datetime.date(2021, 12, 1),
                   related_project=project.title)

    assignment = f.Assignment(project=project)

    developer.assign(project_to_assign=project)
    quality_assurance.assign(project_to_assign=project)
    project_manager.assign(project_to_assign=project)

    developer.set_task(task=task1)
    developer.set_task(task=task2)
    quality_assurance.set_task(task=task3)
    project_manager.set_task(task=task4)

    task1.add_comment("Add chess board, textures, pieces, etc.")
    print("comment to task1: '{0}'".format(task1.comment))
    task2.add_comment("Program the engine to the game")
    print("comment to task2: '{0}'".format(task2.comment))
    task3.add_comment("Test project")
    print("comment to task3: '{0}'".format(task3.comment))
    task4.add_comment("Control the process of work")
    print("comment to task4: '{0}'".format(task4.comment))

    print(developer.assigned_project())
    print(assignment.get_task_to_date(date_by=datetime.date(2021, 11, 1)))

    developer.calculate_salary()
    project.remove_developer(developer=developer)
    developer.unassign(project_to_assign=project)
    quality_assurance.calculate_salary()
    quality_assurance.unassign(project_to_assign=project)
    project_manager.calculate_salary()
    project_manager.unassign(project_to_assign=project)


if __name__ == '__main__':
    main()
