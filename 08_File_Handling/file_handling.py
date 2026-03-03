# التعامل مع الملفات في بايثون 🐍

# 1. كتابة ملف جديد
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("مرحباً بك في عالم بايثون!\n")
    f.write("هذا ملف تجريبي لتعلم كيفية التعامل مع الملفات.\n")

# 2. قراءة محتوى الملف
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("محتوى الملف:")
    print(content)

# 3. إضافة محتوى جديد للملف
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("تمت إضافة هذا السطر بنجاح.\n")

# 4. قراءة الملف سطراً بسطر
with open("test.txt", "r", encoding="utf-8") as f:
    print("قراءة الملف سطراً بسطر:")
    for line in f:
        print(line.strip())
