
def checkstrength(password):
    from CommonWords import Common
    from PasswordComplexity import Complexity
    from PasswordLength import PasswordLen
    return PasswordLen(password) + Common(password) + Complexity(password)

def main():
    password = input("Enter a password ")
    points = checkstrength(password)
    if points <= 0:
        print("Weak password") 
    elif 1 <= points <= 3:
        print("Moderate password")
    else:
        print("Strong password")

if __name__ == '__main__':
    main()