"""
PROJECT NAME: Password Manager
MADE BY: SAYAM PRADHAN
GUIDED BY: JHILI SAHOO
"""


# import neccessary modules
from cryptography.fernet import Fernet


# function to load key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# secret key
key = load_key()

# initialisation of fernet
crypt = Fernet(key)

# necessary functions
# # secret key
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# function to view existing passwords


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            site, user, passw = data.split("|")
            print(
                "Site:", site,
                "| User: ", user,
                "| Password: ", crypt.decrypt(passw.encode()).decode()
            )


# function to add new password
def add():
    site = input('Site name: ')
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(site + "|" + name + "|" +
                crypt.encrypt(pwd.encode()).decode() + "\n")


# user choice for mode selection
while True:
    mode = input(
        """Would you like to add a new password or view existing ones?
        (a) Add new password
        (v) View existing passwords

        press q to quit...
        """
    ).lower()

    if mode == "q".lower():
        break

    if mode == "v".lower():
        view()

    elif mode == "a".lower():
        add()

    else:
        print("Invalid mode.")

    cont = input(
        """Continue?
        (y) Yes
        (n) No
    """)

    if cont == "y".lower():
        continue

    elif cont == "n".lower():
        break

    else:
        print("Invalid Input...")
        break
