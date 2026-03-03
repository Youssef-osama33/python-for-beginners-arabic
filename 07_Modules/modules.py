# الموديلات والمكتبات في بايثون 🐍

# 1. استيراد موديل math
import math
print("الجذر التربيعي لـ 16 هو:", math.sqrt(16))
print("قيمة باي (Pi) هي:", math.pi)

# 2. استيراد موديل random
import random
print("رقم عشوائي بين 1 و 10 هو:", random.randint(1, 10))

# 3. استيراد موديل datetime
import datetime
print("التاريخ والوقت الحالي هو:", datetime.datetime.now())

# 4. استيراد دالة معينة من موديل
from math import factorial
print("مضروب 5 هو:", factorial(5))

# 5. استيراد موديل باسم مستعار
import statistics as stats
data = [1, 2, 3, 4, 5]
print("المتوسط الحسابي هو:", stats.mean(data))
