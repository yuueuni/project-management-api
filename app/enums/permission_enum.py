from enum import Enum


class PermissionTypeEnum(Enum):
    PUBLIC = 'PUBLIC'
    AUTHENTICATED = 'AUTHENTICATED'
    RESTRICTED = 'RESTRICTED'
