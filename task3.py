class Employee:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if attr == "department":
            return "Не призначено"
        raise AttributeError(f"Атрибут '{attr}' не існує")


e = Employee("Vova")

print(e.name)
print(e.department)

try:
    print(e.salary)
except AttributeError as error:
    print("Помилка:", error)