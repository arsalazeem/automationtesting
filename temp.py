import json
import pdb

class Employee:
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin

address = Address("Alpharetta", "7258 Spring Street", "30004")
employee = Employee("John", 9000, address)
print(type(employee))
pdb.set_trace()
print("Encode into JSON formatted Data")
employeeJSONData = json.dumps(employee.toJson(), indent=4)
print(employeeJSONData)

# Let's load it using the load method to check if we can decode it or not.
print("Decode JSON formatted Data")
employeeJSON = json.loads(employeeJSONData)
print(employeeJSON)