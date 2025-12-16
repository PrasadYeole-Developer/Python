"""
| Method     | Trigger         |
| ---------- | --------------- |
| `__init__` | Object creation |
| `__str__`  | `print(obj)`    |
| `__len__`  | `len(obj)`      |
| `__add__`  | `+`             |
| `__eq__`   | `==`            |

"""

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"Book has {self.pages} pages"

b = Book(100)
print(b)
