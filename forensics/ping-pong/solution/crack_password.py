import hashlib

def crack_password(challenge, target_digest):
    f = open('xato-net-10-million-passwords-100.txt', 'r')
    passwords = f.readlines()
    f.close()

    for password in passwords:
        password = password[:-1]
        sha1 = hashlib.sha1()
        sha1.update(password.encode('ascii'))
        sha1.update(challenge)
        #print(password, sha1.digest(), target_digest)
        if sha1.digest() == target_digest:
            return password
