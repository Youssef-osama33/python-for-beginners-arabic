# معالجة الأخطاء في بايثون 🐍

# 1. معالجة خطأ القسمة على صفر
try:
    x = 10 / 0
except ZeroDivisionError:
    print("خطأ: لا يمكن القسمة على صفر!")

# 2. معالجة خطأ القيمة (ValueError)
try:
    num = int("abc")
except ValueError:
    print("خطأ: لا يمكن تحويل النص إلى رقم!")

# 3. معالجة خطأ الملف غير الموجود (FileNotFoundError)
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("خطأ: الملف غير موجود!")

# 4. استخدام finally و else
try:
    x = 10 / 2
except ZeroDivisionError:
    print("خطأ: لا يمكن القسمة على صفر!")
else:
    print("العملية تمت بنجاح! النتيجة هي:", x)
finally:
    print("تم الانتهاء من تنفيذ الكود.")
