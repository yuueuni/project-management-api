from sqlalchemy.orm import Session

from app.repositories import ProjectRepository, PermissionRepository
from app.schemas import ProjectResponse, BooleanResponse


class ProjectService:
    def __init__(self, db: Session):
        self.db = db
        self.project_repository = ProjectRepository(db)
        self.permission_repository = PermissionRepository(db)

    def create_project(self, project_create) -> ProjectResponse:
        try:
            project = self.project_repository.create_project(project_create)
            self.db.commit()
            return ProjectResponse(
                project_id=project.id,
                name=project.name,
                description=project.description,
            )
        except Exception as e:
            self.db.rollback()
            raise e

    def get_project_by_id(self, project_id) -> ProjectResponse:
        project = self.project_repository.get_project_by_id(project_id)
        if not project:
            raise Exception("Project not found")
        return ProjectResponse(
            project_id=project.id,
            name=project.name,
            description=project.description,
        )

    def update_project(self, project_id, project_update) -> ProjectResponse:
        try:
            project = self.project_repository.update_project(project_id, project_update)
            self.db.commit()
            return ProjectResponse(
                project_id=project.id,
                name=project.name,
                description=project.description,
            )
        except Exception as e:
            self.db.rollback()
            raise e

    def delete_project(self, project_id) -> BooleanResponse:
        try:
            self.project_repository.delete_project(project_id)
            self.db.commit()
            return BooleanResponse(result=True)
        except Exception as e:
            self.db.rollback()
            raise e

    def add_project_member(self, project_id, add_project_member_request) -> BooleanResponse:
        try:
            if self.permission_repository.get_project_permission_member(
                    project_id=project_id,
                    member_id=add_project_member_request.member_id):
                raise Exception("Already added member")
            self.permission_repository.add_project_permission_member(
                project_id=project_id,
                member_id=add_project_member_request.member_id,
                role_id=add_project_member_request.role_id
            )
            self.db.commit()
            return BooleanResponse(result=True)
        except Exception as e:
            self.db.rollback()
            raise e
