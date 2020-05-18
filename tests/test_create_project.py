from models.project import Project
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters
    return "".join(
        [random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_create_project(app):
    project = Project(name=random_string(20), description=random_string(20))
    app.session.login("administrator", "root")
    old_projects = app.soap.get_projects_list("administrator", "root")

    for p in old_projects:
        if p.name == project.name:
            project = Project(name=random_string(20),
                              description=random_string(20))

    app.project.create(project)
    new_projects = app.soap.get_projects_list("administrator", "root")
    assert len(old_projects) == len(new_projects) - 1
    assert project in new_projects
