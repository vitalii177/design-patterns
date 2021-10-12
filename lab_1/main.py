import lab_1 as f
import datetime


def main():
    developer = f.Developer(id=1, name='Yurii',
                            address='Zelena Street, 2',
                            phone_number='+38 (063) 34-54-239',
                            email='yurii87@gmail.com',
                            position='Junior',
                            rank='Developer',
                            salary=1100.0)

    project = f.Project(title="Chess Game", start_date=datetime.date.today())

    quality_assurance = f.QualityAssurance(id=2, name='Alex',
                                           address='Dnisterska Street, 5',
                                           phone_number='+38 (067) 45-23-989',
                                           email='alex56@gmail.com',
                                           position='Junior',
                                           rank='QA',
                                           salary=770.0, project=project)

    project_manager = f.ProjectManager(id=3, name='Alex',
                                       address='Dnisterska Street, 5',
                                       phone_number='+38 (067) 45-23-989',
                                       email='alex56@gmail.com',
                                       position='',
                                       rank='',
                                       salary=770.0, project=project)

    project.add_developer(developer=developer)

    assignment = f.Assignment(project=project)

    developer.assign(project_to_assign=project)
    quality_assurance.assign(project_to_assign=project)
    project_manager.assign(project_to_assign=project)

    print(developer.assigned_project())
    print(assignment.get_task_to_date(date_by=datetime.date(2021, 11, 1)))

    project.remove_developer(developer=developer)

    developer.unassign(project_to_assign=project)
    quality_assurance.unassign(project_to_assign=project)
    project_manager.unassign(project_to_assign=project)


if __name__ == '__main__':
    main()