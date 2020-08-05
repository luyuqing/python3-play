import bcrypt


# jon method on boost ai adminpanel user password
def hashpw(password, rounds=10):
    salt = bcrypt.gensalt(rounds=rounds, prefix=b"2a")
    hash = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hash.decode("utf-8")


print(hashpw("testingtestingtesting"))  # the password generated are different
