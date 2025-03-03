from app.enums import UsedYseNoEnum
from app.models import Project


class ProjectRepository:
    def __init__(self, db):
        self.db = db

    def create_project(self, project):
        self.db.add(Project(
            name=project.name,
            description=project.description
        ))

    def get_project_by_id(self, project_id):
        return self.db.query(Project).filter_by(id=project_id).first()

    def update_project(self, project_id, project):
        project_to_update = self.db.query(Project).filter_by(id=project_id).first()
        project_to_update.name = project.name
        project_to_update.description = project.description

    def delete_project(self, project_id):
        project_to_delete = self.db.query(Project).filter_by(id=project_id).first()
        project_to_delete.used = UsedYseNoEnum.NO.value
