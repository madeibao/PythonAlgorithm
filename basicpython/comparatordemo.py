

from dataclasses import dataclass
from operator import attrgetter


@dataclass
class Person:
    name: str
    age: int

    def __repr__(self):
        return f"{self.name}({self.age})"

people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 30),
    Person("David", 25),
    Person("Eve", 35),
    Person("Frank", 25),
]

print("原始:      ", people)
print("age,name:  ", sorted(people, key=lambda p: (p.age, p.name)))
print("attrgetter:", sorted(people, key=attrgetter("age", "name")))
print("全降序:    ", sorted(people, key=lambda p: (p.age, p.name), reverse=True))

# age 升序 + name 降序（两趟稳定排序）
tmp = sorted(people, key=lambda p: p.name, reverse=True)
result = sorted(tmp, key=lambda p: p.age)
print("age升 name降:", result)
