--- DATABASE 생성
CREATE DATABASE assignment_db;

--- User 생성
CREATE USER student WITH PASSWORD 'password';
ALTER ROLE student SET client_encoding TO 'utf8';
ALTER ROLE student SET default_transaction_isolation TO 'read committed';
ALTER ROLE student WITH SUPERUSER;

--- DB에 대한 User 권한 부여
GRANT ALL PRIVILEGES ON DATABASE assignment_db TO student;