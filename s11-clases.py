#
#
#
class Person:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def login(self):
        print("Welcome sr. " + self.name + "....")

    def logout(self):
        print("Bye sr. " + self.name)


emanuel = Person("Hardwell", ",sdnkdbhsddhvhsvdjvas")
juan = Person("Charls", "**********kdmkdm")

emanuel.login()
emanuel.logout()

juan.login()
juan.logout()
