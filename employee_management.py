import string

main = {
    "locations": {

    },

    "utils": {

    },

    "shifts": {

    }
}

validUses = {
    "name": str,
    "employeeID": int,

}

validSalaryDenominations = {
    "y": "year",
    "d": "day",
    "w": "week",
    "h": "hour"
}


def deepSearch(needle, haystack):
    if isinstance(haystack, dict):
        if needle in haystack:
                return True
    if isinstance(haystack, Location):
        if needle in haystack.locations or needle in haystack.employees:
            return True
    
    
    for hay in haystack:
        if isinstance(hay, dict):
            if deepSearch(needle, hay):
                return True
        elif isinstance(hay, Location):
            if deepSearch(needle, hay):
                return True

    return False
        

def isLocation(location):
    locations = main["locations"]


    result = deepSearch(location, locations)
    if result:
        return True
            


    print(f"{location} not found")

    return False


    


def isValid(key, value):
    pass
    


def countInstances(directory, instance, recursive):
    count = 0

    if isinstance(directory, dict):
        for value in directory.values():
            if isinstance(value, instance):
                count += 1

            if recursive:
                count += countInstances(value, instance, recursive)

    elif isinstance(directory, Location):
        count += countInstances(directory.employees, instance, recursive)
        count += countInstances(directory.locations, instance, recursive)

    return count

def convertDenomination(denomination):
    for key, value in validSalaryDenominations.items():
        if key == denomination or value == denomination:
            return value
    return False
    
def getNewEmployeeID():
    return countInstances(main["locations"], Employee, True) + 1

class Location:
    def __init__(self, name, directory=None):
        self.name = name
        self.employees = {}
        self.locations = {}

        if directory is None:
            main["locations"][name] = self
        else:
            directory[name] = self

    def addLocation(self, location):
        self.locations[location.name] = location
    def addEmployee(self, employee):
        self.employees[employee.employeeID] = employee




class Employee:
    def __init__(self, name, location, salary, *args):



        employeeID = getNewEmployeeID()
        employeeID = f"{employeeID:05d}"
        
        self.employeeID = employeeID
        
        
        self.location = location


        for argument in args:
                key, value = argument.split("=", 1)
                if isValid(key, value):
                    setattr(self, key, value)

        number, denomination = salary.split("/", 1)

        number = int(number)

        if number < 0:
            raise ValueError("Salary must be a positive number.")

        validDenomination = convertDenomination(denomination.lower())
        if not validDenomination:
            raise ValueError("Invalid denomination.") 
        
        self.salaryDenomination = validDenomination

        self.salary = number

        parts = name.split (" ")

        self.firstName = parts[0]
        self.lastName = parts[-1]
        self.middleNames = parts [1:-1]

        self.name = name

        location.addEmployee(self)


    def remove(self):
        del self.location.employees[self.employeeID]

    



validDataTypes = {
    "Employee": Employee
}




wood = Location("Wood")
stone = Location("Stone", wood.locations)
john = Employee("John Doe", wood, "24000/y")
jen = Employee("Jen Doe", wood, "120/d")
joe = Employee("Joe Doe", stone, "800/w")



print(wood.employees["00001"].salaryDenomination)
print(wood.employees["00002"].name)
print(stone.employees["00003"].employeeID)