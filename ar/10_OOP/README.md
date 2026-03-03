# 10_OOP (البرمجة الكائنية) 🐍

في هذا الدرس سنتعرف على البرمجة الكائنية (Object-Oriented Programming) في بايثون.

## 📦 الكلاسات والكائنات (Classes and Objects)
الكلاس هو عبارة عن قالب (Template) لإنشاء كائنات (Objects).

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"مرحباً بك يا {self.name}!")

p1 = Person("أحمد", 25)
p1.greet()
```

## 🧬 الوراثة (Inheritance)
تستخدم الوراثة لإنشاء كلاس جديد يرث من كلاس موجود.

```python
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

s1 = Student("سارة", 20, "A")
s1.greet()
```

---

## 🚀 التحدي العاشر
قم بتشغيل ملف `oop.py` الموجود في هذا المجلد.
