import bcrypt


def hash_registering_password(pword):
    return bcrypt.hashpw(pword.encode('utf-8'), bcrypt.gensalt())


password = 'password'
print(hash_registering_password(password))


def validate_password(pword, hashed):
    return bcrypt.checkpw(pword.encode('utf-8'), hashed.encode('utf-8'))
