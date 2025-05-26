#creating a class
class Department:
    dept_count = 0  

    def __init__(self, dept_id, name, location, head_of_dept): 
        self.dept_id = dept_id
        self.name = name
        self.location = location
        self.head_of_dept = head_of_dept

        Department.dept_count += 1 

    def display_department_info(self):
        print("Department Information:")
        print(f"Dept ID       : {self.dept_id}")
        print(f"Name          : {self.name}")
        print(f"Location      : {self.location}")
        print(f"Head of Dept  : {self.head_of_dept}")
        print()

    @classmethod
    def get_total_departments(cls):
        return cls.dept_count

dept1 = Department(101, "Computer Science", "Block A", "Dr. Ram")
dept2 = Department(102, "Electronics", "Block B", "Dr. Seema")

dept1.display_department_info()
dept2.display_department_info()

print(f"Total Departments: {Department.get_total_departments()}")



###taking input from the users

class Department:

    dept_count = 0  

    def __init__(self, dept_id, name, location, head_of_dept):
      
        self.dept_id = dept_id
        self.name = name
        self.location = location
        self.head_of_dept = head_of_dept

        Department.dept_count += 1  

n = int(input("Enter the number of departments to create: "))

for i in range(n):
    print(f"\nEnter details for Department {i + 1}:")
    dept_id = input("Enter Department ID: ")
    name = input("Enter Department Name: ")
    location = input("Enter Department Location: ")
    head_of_dept = input("Enter Head of Department: ")

    dept = Department(dept_id, name, location, head_of_dept)

print(f"\nTotal Departments Created: {Department.dept_count}")

'''
###################################

'''
#storing in a list
class Department:

    dept_count = 0 

    def __init__(self, dept_id, name, location, head_of_dept):
        
        self.dept_id = dept_id
        self.name = name
        self.location = location
        self.head_of_dept = head_of_dept

        Department.dept_count += 1  

    def display_department_info(self):
        print("\nDepartment Information:")
        print("------------------------")
        print(f"Dept ID       : {self.dept_id}")
        print(f"Name          : {self.name}")
        print(f"Location      : {self.location}")
        print(f"Head of Dept  : {self.head_of_dept}")

    @classmethod
    def get_total_departments(cls):
        return cls.dept_count
n = int(input("Enter the number of departments to create: "))
department_list = []

for i in range(n):
    print(f"\nEnter details for Department {i + 1}:")
    dept_id = input("Enter Department ID: ")
    name = input("Enter Department Name: ")
    location = input("Enter Department Location: ")
    head_of_dept = input("Enter Head of Department: ")


    dept = Department(dept_id, name, location, head_of_dept)
    department_list.append(dept)

print("\n==============================")
print("     All Department Details   ")
print("==============================")
for dept in department_list:
    dept.display_department_info()
print(f"\nTotal Departments Created: {Department.get_total_departments()}")





#.performing search operation by dept_id
class Department:

    dept_count = 0  # Class variable

    def __init__(self, dept_id, name, location, head_of_dept):
        self.dept_id = dept_id
        self.name = name
        self.location = location
        self.head_of_dept = head_of_dept

        Department.dept_count += 1

    def display_department_info(self):
        print("\nDepartment Information:")
        print("------------------------")
        print(f"Dept ID       : {self.dept_id}")
        print(f"Name          : {self.name}")
        print(f"Location      : {self.location}")
        print(f"Head of Dept  : {self.head_of_dept}")

    @classmethod
    def get_total_departments(cls):
        return cls.dept_count

n = int(input("Enter the number of departments to create: "))
department_list = []

for i in range(n):
    print(f"\nEnter details for Department {i + 1}:")
    dept_id = input("Enter Department ID: ")
    name = input("Enter Department Name: ")
    location = input("Enter Department Location: ")
    head_of_dept = input("Enter Head of Department: ")

    dept = Department(dept_id, name, location, head_of_dept)
    department_list.append(dept)

# Display all departments
print("\n==============================")
print("     All Department Details   ")
print("==============================")
for dept in department_list:
    dept.display_department_info()

print(f"\nTotal Departments Created: {Department.get_total_departments()}")
search_id = input("\nEnter Department ID to search: ")

found = False
for dept in department_list:
    if dept.dept_id == search_id:
        print("\nDepartment Found:")
        dept.display_department_info()
        found = True
        break

if not found:
    print("\nDepartment with the given ID not found.")
    

# performing search operation based on dept_name

class Department:

    dept_count = 0  # Class variable

    def __init__(self, dept_id, name, location, head_of_dept):
        self.dept_id = dept_id
        self.name = name
        self.location = location
        self.head_of_dept = head_of_dept

        Department.dept_count += 1

    def display_department_info(self):
        print("\nDepartment Information:")
        print("------------------------")
        print(f"Dept ID       : {self.dept_id}")
        print(f"Name          : {self.name}")
        print(f"Location      : {self.location}")
        print(f"Head of Dept  : {self.head_of_dept}")

    @classmethod
    def get_total_departments(cls):
        return cls.dept_count

n = int(input("Enter the number of departments to create: "))
department_list = []

for i in range(n):
    print(f"\nEnter details for Department {i + 1}:")
    dept_id = input("Enter Department ID: ")
    name = input("Enter Department Name: ")
    location = input("Enter Department Location: ")
    head_of_dept = input("Enter Head of Department: ")

    dept = Department(dept_id, name, location, head_of_dept)
    department_list.append(dept)
print("     All Department Details   ")

for dept in department_list:
    dept.display_department_info()

print(f"\nTotal Departments Created: {Department.get_total_departments()}")

search_name = input("\nEnter Department name to search: ")

found = False
for dept in department_list:
    if dept.name == search_name:
        print("\nDepartment Found:")
        dept.display_department_info()
        found = True
        break

if not found:
    print("\nDepartment with the given name not found.")