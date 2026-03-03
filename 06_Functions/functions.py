# الدوال في بايثون 🐍

# 1. تعريف دالة بسيطة
def say_hello():
    print("مرحباً بك في عالم بايثون!")

# استدعاء الدالة
say_hello()

# 2. دالة مع مدخلات (Arguments)
def greet(name):
    print(f"مرحباً بك يا {name}!")

greet("أحمد")
greet("سارة")

# 3. دالة مع مخرجات (Return)
def add(x, y):
    return x + y

result = add(10, 5)
print("مجموع 10 + 5 هو:", result)

# 4. دالة مع قيم افتراضية
def power(base, exponent=2):
    return base ** exponent

print("2 أس 2 هو:", power(2))
print("2 أس 3 هو:", power(2, 3))

# 5. دالة مع عدد غير محدد من المدخلات
def sum_all(*args):
    return sum(args)

print("مجموع الأرقام 1, 2, 3, 4 هو:", sum_all(1, 2, 3, 4))
