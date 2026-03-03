# البرمجة الكائنية (OOP) في بايثون 🐍

# 1. تعريف كلاس بسيط
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"{self.name} يصدر صوت: {sound}")

# إنشاء كائن (Object)
dog = Animal("بندق", "كلب")
dog.make_sound("هوهو")

# 2. الوراثة (Inheritance)
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "قطة")
        self.color = color

    def meow(self):
        print(f"{self.name} (القطة {self.color}) تقول: مياو!")

# إنشاء كائن من الكلاس المشتق
my_cat = Cat("لولو", "بيضاء")
my_cat.meow()

# 3. استخدام الخصائص والأساليب
print(f"اسم القطة: {my_cat.name}")
print(f"نوع القطة: {my_cat.species}")
