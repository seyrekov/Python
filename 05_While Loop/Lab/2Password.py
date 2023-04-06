name = input()
login_password = input()

password = input()

while password != login_password:
    password = input()

print(f'Wellcome {name}!')
