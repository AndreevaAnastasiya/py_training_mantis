from models.project import Project
import random


def test_delete_project(app):
    app.session.login("administrator", "root")
    if len(app.soap.get_projects_list("administrator", "root")) == 0:
        app.project.create(Project(name="Test", description="test"))

    old_projects = app.soap.get_projects_list("administrator", "root")
    index = random.randint(0, len(old_projects) - 1)

    app.project.delete_by_index(index)

    new_projects = app.soap.get_projects_list("administrator", "root")
    assert len(old_projects) == len(new_projects) + 1

    old_projects.pop(index)
    assert old_projects == new_projects
