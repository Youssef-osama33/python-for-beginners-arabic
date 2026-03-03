# هياكل البيانات في بايثون 🐍

# 1. القوائم (Lists)
fruits = ["تفاح", "موز", "برتقال"]
print("القائمة الأصلية:", fruits)

# إضافة عنصر
fruits.append("عنب")
print("بعد الإضافة:", fruits)

# حذف عنصر
fruits.remove("موز")
print("بعد الحذف:", fruits)

# الوصول لعنصر
print("أول عنصر:", fruits[0])

# 2. القواميس (Dictionaries)
person = {
    "name": "أحمد",
    "age": 25,
    "city": "القاهرة"
}
print("القاموس:", person)

# الوصول لقيمة
print("الاسم:", person["name"])

# إضافة مفتاح وقيمة
person["job"] = "مبرمج"
print("بعد الإضافة:", person)

# 3. المجموعات (Sets)
numbers = {1, 2, 3, 3, 4, 5, 5}
print("المجموعة (بدون تكرار):", numbers)

# إضافة عنصر
numbers.add(6)
print("بعد الإضافة:", numbers)

# 4. الصفوف (Tuples) - غير قابلة للتعديل
coordinates = (10, 20)
print("الإحداثيات:", coordinates)
# coordinates[0] = 15 # سيؤدي لخطأ
