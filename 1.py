students = []

def add_student():
    name = input("Enter name: ")
    marks = list(map(int, input("Enter marks (3 subjects): ").split()))
    students.append({"name": name, "marks": marks})

def display():
    for s in students:
        avg = sum(s["marks"]) / len(s["marks"])
        print(s["name"], "Avg:", avg)

def topper():
    top = max(students, key=lambda x: sum(x["marks"]))
    print("Topper:", top["name"])

while True:
    print("\n1.Add 2.Display 3.Topper 4.Exit")
    ch = input("Choice: ")
    if ch == '1':
        add_student()
    elif ch == '2':
        display()
    elif ch == '3':
        topper()
    else:
        break
