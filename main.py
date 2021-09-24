import secrets
import string


def generate(length):
    allChars = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(allChars) for i in range(length))
    print(password)


if __name__ == '__main__':
    generate(int(input("Enter the Length of the required Password: ")))
