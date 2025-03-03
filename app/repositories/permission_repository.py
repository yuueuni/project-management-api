from app.models import MemberRole


class PermissionRepository:
    def __init__(self, db):
        self.db = db

    def add_project_permission_member(self, project_id, member_id, role_id):
        member_role = MemberRole(
            target_id=project_id,
            member_id=member_id,
            role_id=role_id
        )
        self.db.add(member_role)
        return member_role

    def get_project_permission_member(self, project_id, member_id):
        return self.db.query(MemberRole).filter_by(target_id=project_id, member_id=member_id).first()

