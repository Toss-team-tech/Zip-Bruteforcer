import zipfile

charlist = 'abcdefghijklmnopqrstuvwxyz'
complete = []

for current in range(6):
    a = [i for i in charlist]
    for x in range(current):
        a = [y + i for i in charlist for y in a]
    complete = complete + a

z = zipfile.ZipFile('secret.zip')

tries = 0

for password in complete:
    try:
        tries += 1
        z.setpassword(password.encode("ascii"))
        z.extract('secret.txt')
        print(f'password was found after {tries} tries and the password is {password}')
        break
    except:
        pass
