from suds.client import Client
from models.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_projects_list(self, username, password):
        projects = []
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        response = client.service.mc_projects_get_user_accessible(
            username, password)

        for element in response:
            projects.append(Project(name=element.name,
                                    description=element.description))
        return projects
