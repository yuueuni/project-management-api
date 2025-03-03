from enum import Enum


class RoleTypeEnum(Enum):
    ADMIN = 'ADMIN', '관리자'
    PROJECT_OWNER = 'PROJECT_OWNER', '프로젝트 소유자'
    EDITOR = 'EDITOR', '편집자'
    VIEWER = 'VIEWER', '조회자'

