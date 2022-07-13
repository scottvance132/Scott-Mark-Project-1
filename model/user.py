class User:
    def __init__(self, user_id, username, password, fn, ln, email, role):
        self.id = user_id
        self.username = username
        self.password = password
        self.fn = fn
        self.ln = ln
        self.email = email
        self.role = role

    def to_dict(self):
        return {
            'user_id': self.id,
            'username': self.username,
            'password': self.password,
            'first_name': self.fn,
            'last_name': self.ln,
            'email': self.email,
            'role': self.role
        }


u1 = User('1', 'mperez', 'H0useB0lon!', 'Mark', 'Perez', 'marcos736@revature.com', 'employee')
print(u1.to_dict())

