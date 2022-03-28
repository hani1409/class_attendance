from collections import OrderedDict
from datetime import date


Grades = ['Kindergarden', 'First',
          'Second', 'Third',
          'Fourth', 'Fifth',
          'Sixest', 'Seventh',
          'eighth', 'Ninth',
          'Tenth', 'Eleventh',
          'Twelfth', 'College',
          'Working']


class Student(object):
    def __init__(self,
                 lastName,
                 firstName,
                 grade,
                 DOB,
                 address=OrderedDict(),
                 phoneNumber=OrderedDict()):

        self.phoneNumber = {}
        self.lastName = lastName
        self.firstName = firstName
        self.address = address
        self.visitation = {}

        if phoneNumber and self.validNumber(phoneNumber[1]):
            self.addPhoneNumber(phoneNumber)

        if self.isValidGrade(grade):
            self.grade = grade
        else:
            raise ValueError('%s is not a valid value, please select from the following: %s' % (self.grade, Grades))

        if self.isValidDate(DOB):
            self.DOB = DOB
        else:
            raise ValueError('%s is not a valid date.' % DOB)


    def addAddress(self, address=OrderedDict()):
        self.address = address

    def addPhoneNumber(self, phoneNumber=OrderedDict()):
        self.phoneNumber = phoneNumber

    def increaseGrade(self):

        try:
            index = Grades.index(self.grade)
            self.grade = Grades[index+1]
        except IndexError:
            if self.grade == 'Working':
                print("Student/'s grade working, they're not working.")
            else:
                print("%s is not a valid grade" % self.grade)

    def addVisitation(self, who=[], visitationDate=date.today()):
        self.isValidDate(visitationDate)
        self.visitation[visitationDate] = who

    def isValidGrade(self, grade):
        return grade in Grades

    def isValidDate(self, inputDate):
        return isinstance(inputDate, date)

    def validNumber(self, phoneNumber):
        if len(phoneNumber) != 12:
            return False
        for i in range(12):
            if i in [3, 7]:
                if phoneNumber[i] != '-':
                    return False
            elif not phoneNumber[i].isalnum():
                return False
        return True

def main():
    hani = Student('Zion', 'Hani', 'First', date(1981, 1, 24))
    hani.addPhoneNumber(9175381981)
    print(hani.phoneNumber)
    print(hani.address)
    hani.addAddress('459 Woodrow rd, Staten Island, NY 10312')
    print(hani.address)
    print(hani.grade)
    hani.increaseGrade()
    print(hani.grade)
    hani.addVisitation(['HZ', 'MS'])
    print(hani.visitation)
    hani.addVisitation(['HZ', 'MS'], date(2018, 1, 20))
    print(hani.visitation)


if __name__ == '__main__':
    main()