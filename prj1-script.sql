DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE users (
	user_id SERIAL PRIMARY KEY,
	username VARCHAR(50) UNIQUE NOT NULL,
	user_password VARCHAR NOT NULL,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,	
	user_email VARCHAR(100) UNIQUE NOT NULL,
	position_role VARCHAR(20) NOT NULL CHECK (position_role in ('employee','finance_manager'))
);

SELECT *
FROM users;

INSERT INTO users (username, user_password, first_name, last_name, user_email, position_role)
VALUES
('mperez__', '$2b$12$.fHBuoYK8Ff8FFWtHVz.M.9YdNaDvNilQCp3zBoopcYEpgtAcnB6W','Mark', 'Perez', 'marcos736@revature.com', 'employee'),
('bachy24', '$2b$12$.fHBuoYK8Ff8FFWtHVz.M.9YdNaDvNilQCp3zBoopcYEpgtAcnB6W','Bach', 'Tran', 'bach.tran@revature.com', 'finance_manager'),
('scottv', '$2b$12$.fHBuoYK8Ff8FFWtHVz.M.9YdNaDvNilQCp3zBoopcYEpgtAcnB6W','Scott', 'Vance', 'scottvan698@revature.com', 'employee'),
('hen88', '$2b$12$.fHBuoYK8Ff8FFWtHVz.M.9YdNaDvNilQCp3zBoopcYEpgtAcnB6W','Henry', 'Hsieh', 'henry.hsieh@revature.com', 'finance_manager'),
('gkim55', '$2b$12$.fHBuoYK8Ff8FFWtHVz.M.9YdNaDvNilQCp3zBoopcYEpgtAcnB6W','Grace', 'Kim', 'gkim698@revature.com', 'employee');

INSERT INTO users (username, user_password, first_name, last_name, user_email, position_role)
VALUES
('test123', '$2b$12$.fHBuoYK8Ff8FFWtHVz.M.9YdNaDvNilQCp3zBoopcYEpgtAcnB6W', 'test', 'test', 'test@test.com', 'employee');

--- #2 REIMBUSRMENT Table
DROP TABLE IF EXISTS reimbursements CASCADE;

CREATE TABLE reimbursements (
	reimb_id SERIAL PRIMARY KEY,
	reimbursement_amount NUMERIC NOT NULL,
	submitted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	resolved TIMESTAMP NULL,
	status VARCHAR(15) CHECK (status in ('pending', 'approved', 'denied')) DEFAULT 'pending',
	reimb_type VARCHAR NOT NULL CHECK (reimb_type in ('Lodging','Travel', 'Food', 'Other')),
	description VARCHAR(50) NOT NULL,
	receipt BYTEA,
	reimb_author INTEGER NOT NULL,
	reimb_resolver INTEGER,
	CONSTRAINT reimb_author FOREIGN KEY (reimb_author) REFERENCES users(user_id),
	CONSTRAINT reimb_resovler FOREIGN KEY (reimb_resolver) REFERENCES users(user_id)
);

SELECT *
FROM reimbursements;

INSERT INTO reimbursements (reimbursement_amount, reimb_type, description, reimb_author)
VALUES
(100, 'Food', 'Lobster dinner', 1),
(150, 'Lodging', 'Hotel', 1);

INSERT INTO reimbursements (reimbursement_amount, reimb_type, description, reimb_author)
VALUES
(250, 'Travel', 'Air ticket', 3)

UPDATE reimbursements
SET status = 'pending', resolved = CURRENT_TIMESTAMP
WHERE reimb_id = 1;