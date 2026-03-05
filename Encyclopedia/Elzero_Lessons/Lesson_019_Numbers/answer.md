# حل تحدي الدرس 19: Numbers

## ✅ الحل

بالطبع! سنقوم بحل سؤال التحدي خطوة خطوة مع شرح مفصل لكل جزء من الكود.

---

## المطلوب

1. نأخذ عدد صحيح موجب n من المستخدم.
2. نولد قائمة بها n عددًا صحيحًا عشوائيًا ضمن النطاق [-100, 100].
3. نحسب:
   - مجموع الأعداد الزوجية.
   - متوسط الأعداد الفردية الموجبة فقط.
   - أكبر عدد سالب (أو رسالة إذا لم يوجد).
4. نطبع القائمة الأصلية بعد تحويل كل عدد إلى القيمة المطلقة له.

---

## الحل الكامل مع الشرح

```python
import random

# الخطوة 1: طلب عدد صحيح موجب من المستخدم
while True:
    try:
        n = int(input("أدخل عددًا صحيحًا موجبًا n: "))
        if n > 0:
            break  # نخرج من الحلقة إذا كان الرقم صالحًا
        else:
            print("الرجاء إدخال عدد صحيح موجب فقط.")
    except ValueError:
        print("الرجاء إدخال عدد صحيح صالح.")

# الخطوة 2: توليد قائمة أعداد عشوائية بين -100 و 100
numbers = [random.randint(-100, 100) for _ in range(n)]

# طباعة القائمة الأصلية (اختياري، لتوضيح النتائج)
print("\nالقائمة الأصلية:")
print(numbers)

# الخطوة 3: الحسابات المطلوبة

# 3.1 مجموع الأعداد الزوجية
even_numbers = [num for num in numbers if num % 2 == 0]
sum_even = sum(even_numbers)

# 3.2 متوسط الأعداد الفردية الموجبة فقط
positive_odd_numbers = [num for num in numbers if num > 0 and num % 2 != 0]

if len(positive_odd_numbers) > 0:
    avg_positive_odd = sum(positive_odd_numbers) / len(positive_odd_numbers)
else:
    avg_positive_odd = None  # لا توجد أعداد فردية موجبة

# 3.3 أكبر عدد سالب
negative_numbers = [num for num in numbers if num < 0]

if len(negative_numbers) > 0:
    max_negative = max(negative_numbers)
else:
    max_negative = None  # لا توجد أعداد سالبة

# طباعة النتائج
print("\nالنتائج:")

print(f"مجموع الأعداد الزوجية: {sum_even}")

if avg_positive_odd is not None:
    print(f"متوسط الأعداد الفردية الموجبة: {avg_positive_odd:.2f}")
else:
    print("لا توجد أعداد فردية موجبة في القائمة.")

if max_negative is not None:
    print(f"أكبر عدد سالب في القائمة: {max_negative}")
else:
    print("لا توجد أعداد سالبة في القائمة.")

# الخطوة 4: طباعة القائمة بعد تحويل كل عدد إلى القيمة المطلقة
abs_numbers = [abs(num) for num in numbers]
print("\nالقائمة بعد تحويل كل عدد إلى القيمة المطلقة:")
print(abs_numbers)
```

---

## شرح الكود خطوة بخطوة

### 1. استيراد مكتبة `random`
نحتاجها لتوليد أعداد عشوائية.

```python
import random
```

---

### 2. طلب عدد صحيح موجب من المستخدم

- نستخدم حلقة `while True` لكي نكرر الطلب حتى يحصل المستخدم على إدخال صحيح.
- نحاول تحويل الإدخال إلى عدد صحيح.
- نتأكد أن العدد أكبر من صفر.
- إذا لم يكن الإدخال صحيحًا (مثلاً حروف أو عدد سالب)، نطبع رسالة توضيحية ونطلب الإدخال مجددًا.

```python
while True:
    try:
        n = int(input("أدخل عددًا صحيحًا موجبًا n: "))
        if n > 0:
            break
        else:
            print("الرجاء إدخال عدد صحيح موجب فقط.")
    except ValueError:
        print("الرجاء إدخال عدد صحيح صالح.")
```

---

### 3. توليد القائمة العشوائية

- نستخدم تعبير قائمة (list comprehension) لتوليد n عدد عشوائي من -100 إلى 100.

```python
numbers = [random.randint(-100, 100) for _ in range(n)]
```

---

### 4. حساب مجموع الأعداد الزوجية

- نستخدم تعبير قائمة لاستخراج الأعداد الزوجية فقط `(num % 2 == 0)`.
- ثم نجمع هذه الأعداد باستخدام `sum()`.

```python
even_numbers = [num for num in numbers if num % 2 == 0]
sum_even = sum(even_numbers)
```

---

### 5. حساب متوسط الأعداد الفردية
