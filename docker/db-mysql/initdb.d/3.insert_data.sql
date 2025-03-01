-- 사용자 (member) 샘플 데이터
INSERT INTO member (name, password, email, created_by)
VALUES
    ('시스템', 'hashed_password_1', 'system@example.com', 1),
    ('관리자회원', 'hashed_password_2', 'admin@example.com', 1),
    ('프로젝트오너회원', 'hashed_password_3', 'owner@example.com', 1),
    ('편집자회원', 'hashed_password_4', 'user@example.com', 1),
    ('조회자회원', 'hashed_password_5', 'guest@example.com', 1)
;

-- 역할 (role) 샘플 데이터
INSERT INTO role (role, role_name, used)
VALUES
    ('ADMIN', '관리자', 'Y'),
    ('PROJECT_OWNER', '프로젝트 오너', 'Y'),
    ('EDITOR', '편집자', 'Y'),
    ('VIEWER', '조회자', 'Y')
;

-- 권한 (permission) 샘플 데이터
INSERT INTO permission (permission_name, endpoint, http_method, permission_type, feature, created_by)
VALUES
    ('프로젝트 생성', '/api/project', 'POST', 'RESTRICTED', 'create-project', 1),
    ('프로젝트 수정', '/api/project', 'PUT', 'RESTRICTED', 'update-project', 1),
    ('프로젝트 삭제', '/api/project', 'DELETE', 'RESTRICTED', 'delete-project', 1),
    ('프로젝트 조회', '/api/project/{id}', 'GET', 'RESTRICTED', 'view-project', 1),
    ('팀원 초대', '/api/project/invite', 'POST', 'RESTRICTED', 'invite-member', 1),
    ('역할 부여', '/api/project/roles', 'POST', 'RESTRICTED', 'assign-role', 1),
    ('회원가입', '/api/users', 'POST', 'PUBLIC', 'sign-in', 1),
    ('로그인', '/api/auth/login', 'POST', 'PUBLIC', 'login', 1),
    ('이메일 인증 코드 발송', '/api/auth/email/code', 'POST', 'PUBLIC', 'send-email-code', 1),
    ('이메일 인증 확인', '/api/auth/email/verify', 'POST', 'PUBLIC', 'verify-email', 1),
    ('비밀번호 재설정 요청', '/api/auth/password/reset-request', 'POST', 'PUBLIC', 'request-password-reset', 1),
    ('비밀번호 갱신', '/api/auth/password/reset', 'POST', 'PUBLIC', 'reset-password', 1),
    ('계정 삭제', '/api/users', 'DELETE', 'RESTRICTED', 'withdrawal', 1)
;

-- 역할-권한 매핑 (role_permission) 샘플 데이터
INSERT INTO role_permission (role_id, permission_id, created_by)
VALUES
    (1, 1, 1), -- Admin: 프로젝트 생성
    (1, 2, 1), -- Admin: 프로젝트 수정
    (1, 3, 1), -- Admin: 프로젝트 삭제
    (1, 4, 1), -- Admin: 프로젝트 조회
    (1, 5, 1), -- Admin: 팀원 초대
    (1, 6, 1), -- Admin: 역할 부여
    (1, 13, 1), -- Admin: 계정 삭제
    (2, 1, 1), -- Project Owner: 프로젝트 생성
    (2, 2, 1), -- Project Owner: 프로젝트 수정
    (2, 3, 1), -- Project Owner: 프로젝트 삭제
    (2, 4, 1), -- Project Owner: 프로젝트 조회
    (2, 5, 1), -- Project Owner: 팀원 초대
    (2, 6, 1), -- Project Owner: 역할 부여
    (3, 2, 1), -- Editor: 프로젝트 수정
    (3, 4, 1), -- Editor: 프로젝트 조회
    (4, 4, 1) -- Viewer: 프로젝트 조회
;

-- 권한 변경 기록 (permission_history) 샘플 데이터
INSERT INTO permission_history (permission_id, permission_name, endpoint, http_method, permission_type, feature, created_at, created_by)
SELECT id, permission_name, endpoint, http_method, permission_type, feature, created_at, created_by
FROM permission
;

-- 역할-권한 변경 기록 (role_permission_history) 샘플 데이터
INSERT INTO role_permission_history (role_permission_id, role_id, permission_id, action, created_by)
SELECT id, role_id, permission_id, 'GRANT', created_by
FROM role_permission
;

-- 사용자-역할 매핑 (member_role) 샘플 데이터
INSERT INTO member_role (member_id, role_id, target_id, created_by)
VALUES
    (1, 1, 0, 1), -- Admin
    (2, 2, 1, 1), -- Project Owner
    (3, 3, 1, 1), -- Editor
    (4, 4, 1, 1) -- Viewer
;

-- 사용자-역할 변경 기록 (member_role_history) 샘플 데이터
INSERT INTO member_role_history (member_role_id, member_id, role_id, target_id, action, created_by)
SELECT id, member_id, role_id, target_id, 'GRANT', created_by
FROM member_role
;
