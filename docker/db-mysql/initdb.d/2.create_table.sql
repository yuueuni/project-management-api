-- 사용자 테이블
CREATE TABLE member (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    created_by INT NOT NULL,
    updated_at DATETIME NULL ON UPDATE NOW(),
    updated_by INT NULL
);

-- 역할 테이블
CREATE TABLE role (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role VARCHAR(50) NOT NULL COMMENT '역할',
    role_name VARCHAR(50) NOT NULL COMMENT '역할 이름',
    used CHAR(1) NOT NULL DEFAULT 'Y' COMMENT '사용 여부 (Y: 사용, N: 사용 안 함)'
);

-- 권한 테이블
CREATE TABLE permission (
    id INT AUTO_INCREMENT PRIMARY KEY,
    permission_name VARCHAR(100) NOT NULL UNIQUE COMMENT '권한 이름',
    endpoint VARCHAR(255) NOT NULL COMMENT 'API 엔드포인트',
    http_method VARCHAR(10) NOT NULL COMMENT 'HTTP 메서드',
    permission_type VARCHAR(20) NOT NULL COMMENT '권한 유형 (PUBLIC, AUTHENTICATED, RESTRICTED)',
    feature VARCHAR(100) NOT NULL COMMENT '기능명',
    created_at DATETIME NOT NULL DEFAULT NOW(),
    created_by INT NOT NULL,
    updated_at DATETIME NULL ON UPDATE NOW(),
    updated_by INT NULL,
    UNIQUE KEY unique_endpoint_method (endpoint, http_method)
);

-- 권한 변경 기록 테이블
CREATE TABLE permission_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    permission_id INT NOT NULL COMMENT '권한 ID',
    permission_name VARCHAR(100) NOT NULL COMMENT '권한 이름',
    endpoint VARCHAR(255) NOT NULL COMMENT 'API 엔드포인트',
    http_method VARCHAR(10) NOT NULL COMMENT 'HTTP 메서드',
    permission_type VARCHAR(20) NOT NULL COMMENT '권한 유형 (PUBLIC, AUTHENTICATED, RESTRICTED, CUSTOM)',
    feature VARCHAR(100) NOT NULL COMMENT '기능명',
    created_at DATETIME NOT NULL DEFAULT NOW(),
    created_by INT NOT NULL,
    updated_at DATETIME NULL ON UPDATE NOW(),
    updated_by INT NULL,
    FOREIGN KEY (permission_id) REFERENCES permission(id) ON DELETE CASCADE
);

-- 역할-권한 매핑 테이블
CREATE TABLE role_permission (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_id INT NOT NULL COMMENT '역할 ID',
    permission_id INT NOT NULL COMMENT '권한 ID',
    created_at DATETIME NOT NULL DEFAULT NOW(),
    created_by INT NOT NULL,
    updated_at DATETIME NULL ON UPDATE NOW(),
    updated_by INT NULL,
    FOREIGN KEY (role_id) REFERENCES role(id) ON DELETE CASCADE,
    FOREIGN KEY (permission_id) REFERENCES permission(id) ON DELETE CASCADE
);

-- `role_id`와 `permission_id`에 대한 복합 인덱스
CREATE INDEX idx_role_permission_base ON role_permission (role_id, permission_id);

-- 역할-권한 매핑 변경 기록 테이블
CREATE TABLE role_permission_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_permission_id INT NOT NULL COMMENT '역할-권한 매핑 ID',
    role_id INT NOT NULL COMMENT '역할 ID',
    permission_id INT NOT NULL COMMENT '권한 ID',
    action VARCHAR(10) NOT NULL COMMENT '부여(GRANT), 제거(REVOKE)',
    created_at DATETIME NOT NULL DEFAULT NOW(),
    created_by INT NOT NULL,
    updated_at DATETIME NULL ON UPDATE NOW(),
    updated_by INT NULL,
    FOREIGN KEY (role_permission_id) REFERENCES role_permission(id) ON DELETE CASCADE
);

-- 유저-역할 매핑 테이블
CREATE TABLE member_role (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL COMMENT '사용자 ID',
    role_id INT NOT NULL COMMENT '역할 ID',
    target_id INT NOT NULL COMMENT '대상 ID (특정 ID. 0 이면 전체 권한)',
    created_at DATETIME NOT NULL DEFAULT NOW(),
    created_by INT NOT NULL,
    updated_at DATETIME NULL ON UPDATE NOW(),
    updated_by INT NULL,
    FOREIGN KEY (member_id) REFERENCES member(id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES role(id) ON DELETE CASCADE
);

-- `member_id`와 `target_id`에 대한 복합 인덱스
CREATE INDEX idx_member_target ON member_role (member_id, target_id);

-- 유저-역할 매핑 변경 기록 테이블
CREATE TABLE member_role_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_role_id INT NOT NULL COMMENT '유저-역할 매핑 ID',
    member_id INT NOT NULL COMMENT '사용자 ID',
    role_id INT NOT NULL COMMENT '역할 ID',
    target_id INT NOT NULL COMMENT '대상 ID (특정 ID. 0 이면 전체 권한)',
    action VARCHAR(10) NOT NULL COMMENT '부여(GRANT), 제거(REVOKE)',
    created_at DATETIME NOT NULL DEFAULT NOW(),
    created_by INT NOT NULL,
    updated_at DATETIME NULL ON UPDATE NOW(),
    updated_by INT NULL,
    FOREIGN KEY (member_role_id) REFERENCES member_role(id) ON DELETE CASCADE
);

-- 이메일 인증 코드 테이블
CREATE TABLE email_verification (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL COMMENT '이메일',
    code VARCHAR(6) NOT NULL COMMENT '인증 코드',
    expired_at DATETIME NOT NULL COMMENT '만료일시',
    created_at DATETIME NOT NULL DEFAULT NOW()
);

-- `email`과 `code`에 대한 복합 인덱스
CREATE UNIQUE INDEX idx_email_code ON email_verification (email, code);


-- 프로젝트 테이블
CREATE TABLE project (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL COMMENT '프로젝트명',
    description TEXT COMMENT '프로젝트 설명',
    used CHAR(1) NOT NULL DEFAULT 'Y' COMMENT '사용 여부 (Y: 사용, N: 사용 안 함)',
    created_at DATETIME NOT NULL DEFAULT NOW(),
    created_by INT NOT NULL,
    updated_at DATETIME NULL ON UPDATE NOW(),
    updated_by INT NULL
);

-- `name`에 대한 인덱스
CREATE INDEX idx_project_name ON project (name);