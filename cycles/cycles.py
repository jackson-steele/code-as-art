class First:
    def find_answer(self):
        second = Second()
        return second.find_answer()
    
    def answer(self):
        return 42
    
class Second:
    def find_answer(self):
        third = Third()
        return third.find_answer()
    
class Third:
    def find_answer(self):
        fourth = Fourth()
        return fourth.find_answer()

class Fourth:
    def find_answer(self):
        fifth = Fifth()
        return fifth.find_answer()
    
class Fifth:
    def find_answer(self):
        sixth = Sixth()
        return sixth.find_answer()
    
class Sixth:
    def find_answer(self):
        seventh = Seventh()
        return seventh.find_answer()
    
class Seventh:
    def find_answer(self):
        eighth = Eighth()
        return eighth.find_answer()
    
class Eighth:
    def find_answer(self):
        ninth = Ninth()
        return ninth.find_answer()
    
class Ninth:
    def find_answer(self):
        first = First()
        return first.answer()
    
first = First()
first.find_answer()