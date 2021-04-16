class BasePasswordManager:  # this class keep track of all the passwords and consist of two methods get password and iscorrect
    def __init__(self):
        self.old_passwords = list()

    def get_password(self):  # this method returns the recently added password
        return str(self.old_passwords[-1])

    # this method takes the password as an argument and checks whether it is equal to recently added password or not
    def is_correct(self, password):
        return password == self.old_passwords[-1]


# this class is derived class of base password manager class consisting of two methods set_password and get_level
class PasswordManager(BasePasswordManager):
    def __init__(self):
        super().__init__()

    # it takes a new password as an argument and checks wheather new password is valid.if valid then adds it to the list of passwords
    def set_password(self, newPassword):
        if len(self.old_passwords) == 0:
            if len(newPassword) >= 6:
                self.old_passwords.append(newPassword)
                return
            else:
                print("minimum passwrd length should be greater than or equal to 6")
                return
        if self.get_level(newPassword) > self.get_level(self.old_passwords[-1]) and len(newPassword) >= 6:
            self.old_passwords.append(newPassword)
        else:
            print("Not a secure Password")

    # it takes password as an argument and returns the level of that password following the conditions
    def get_level(self, Password):
        if len(Password) < 6:
            print("Cannot assign level as length is less than 6 ")
            return -1
        else:
            specials_char = ['@', '_', '!', '#', '$', '%',
                             '^', '&', '*', '(', ')', '<', '>', '?', ':']
            level = 0
            if Password.isalnum():
                # either digit or alphabets then level 0 password
                if Password.isdigit() == True or Password.isalpha() == True:
                    level = 0
                else:  # if both digits and alphabets are present then level 1 password
                    level = 1
                return level
            else:
                for char in specials_char:  # if secial characters along with alphabets and numbers then level 2 password
                    if char in Password:
                        level = 2
                        break
                return level


if __name__ == '__main__':
    N1 = PasswordManager()
    y = "Yes"
    while(y == "Yes" or y == "yes"):
        print("1: Set a new Password")
        print("2: Get last added Password")
        print("3: Get level of a Password")
        print("4: To Check correctness of Password")
        x = int(input("Enter your Choice: "))
        if x == 1:
            new_pas = input("Enter your new password: ")
            N1.set_password(new_pas)
            m = input(
                "wanna know level of the password you have entered Yes/No: ")
            if(m == "yes" or m == "Yes"):
                print("The password you have entered is of Level: ", end="")
                print(N1.get_level(new_pas))

        elif x == 2:
            print(N1.get_password())

        elif x == 3:
            pas = input("Enter a password to know its Level: ")
            print(N1.get_level(pas))
        elif x == 4:
            pas = input(
                "Enter a password to check whether it matches with current password: ")
            print('Matches'if N1.is_correct(pas)
                  == True else "Doesn't Matches")
        else:
            print("You have entered wrong choice ")
            print("Enter your Choice again: ")
        y = input("Wanna Continue or exit: Yes/No: ")
