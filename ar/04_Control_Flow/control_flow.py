# الشروط والحلقات في بايثون 🐍

# 1. الشروط (If Statements)
age = 18
if age >= 18:
    print("أنت بالغ")
elif age >= 13:
    print("أنت مراهق")
else:
    print("أنت طفل")

# 2. الحلقات (Loops)
# حلقة for
print("حلقة for:")
for i in range(5):
    print(i)

# حلقة while
print("حلقة while:")
count = 0
while count < 5:
    print(count)
    count += 1

# 3. استخدام break و continue
print("استخدام break و continue:")
for i in range(10):
    if i == 5:
        break # توقف عند 5
    if i % 2 == 0:
        continue # تخطى الأرقام الزوجية
    print(i)
