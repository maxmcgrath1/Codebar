class Member:
    def __init__(self, full_name,):
        self.full_name = full_name

class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason

