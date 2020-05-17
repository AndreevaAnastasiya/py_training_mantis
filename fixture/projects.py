from models.project import Project
import time


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        dw = self.app.dw
        if not dw.current_url.endswith("/manage_proj_page.php"):
            dw.find_element_by_link_text("Manage").click()
            dw.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        dw = self.app.dw
        self.open_projects_page()
        dw.find_element_by_xpath("//input[@value='Create New Project']").click()
        dw.find_element_by_name("name").send_keys(project.name)
        dw.find_element_by_xpath("//textarea[@name='description']").send_keys(
            project.description)
        dw.find_element_by_xpath("//input[@value='Add Project']").click()
        time.sleep(3)

    def get_projects_list(self):
        dw = self.app.dw
        self.open_projects_page()
        projects = []
        for element in dw.find_elements_by_xpath(
                "//table[@class='width100']//tr[contains(@class, 'row')]"):
            name = element.find_element_by_xpath(".//td[1]").text
            description = element.find_element_by_xpath(".//td[5]").text
            projects.append(Project(name=name, description=description))
        projects.pop(0)
        return projects

    def delete_by_index(self, index):
        dw = self.app.dw
        self.open_projects_page()
        dw.find_elements_by_xpath("//table[@class='width100']//tr[contains("
                                  "@class, 'row')]//td//a[contains("
                                  "@href, 'edit')]")[index].click()
        time.sleep(1)
        dw.find_element_by_xpath("//input[@value='Delete Project']").click()
        dw.find_element_by_xpath("//input[@value='Delete Project']").click()
