# الدرس رقم 13: Strings Methods Part One

## 📚 شرح الدرس

درس بايثون رقم 13: "طرق السلاسل النصية - الجزء الأول" (Strings Methods Part One)

مرحبًا بك في درس جديد من دروس تعلم لغة بايثون! اليوم سنتعرف على مجموعة مهمة من الأدوات التي تساعدنا على التعامل مع النصوص أو ما يسمى "السلاسل النصية" (Strings) في بايثون. سنتعلم كيف نستخدم **طرق النصوص** (String Methods) التي تسهل علينا التعامل مع النصوص وتعديلها.

---

## 1. ما هي طرق السلاسل النصية (String Methods)؟

في بايثون، النصوص تُخزن على شكل سلاسل من الأحرف. يمكننا استخدام **طرق** (functions) مدمجة تساعدنا على إجراء عمليات مختلفة على النصوص، مثل تحويل الأحرف إلى كبيرة أو صغيرة، التحقق من محتويات النص، وغيرها.

الطرق هي دوال خاصة مرتبطة بالكائن (في هذه الحالة النص)، وتُستخدم عبر كتابة اسم النص متبوعًا بنقطة ثم اسم الطريقة.

**الصيغة العامة:**
```python
string_variable.method_name()
```

---

## 2. أهم طرق السلاسل النصية في الجزء الأول

### 2.1. طريقة `lower()`

- تحويل جميع أحرف النص إلى أحرف صغيرة (lowercase).
- لا تغير النص الأصلي، بل تعيد نسخة جديدة.

```python
text = "Python Is FUN"
print(text.lower())  # النتيجة: python is fun
```

### 2.2. طريقة `upper()`

- تحويل جميع الأحرف إلى أحرف كبيرة (uppercase).

```python
text = "Python Is FUN"
print(text.upper())  # النتيجة: PYTHON IS FUN
```

### 2.3. طريقة `strip()`

- إزالة المسافات البيضاء (spaces) من بداية ونهاية النص.
- مفيدة عند قراءة بيانات قد تحتوي على مسافات زائدة.

```python
text = "   Hello World!   "
print(text.strip())  # النتيجة: "Hello World!"
```

### 2.4. طريقة `replace(old, new)`

- استبدال جزء معين من النص (old) بآخر (new).

```python
text = "I like apples"
print(text.replace("apples", "oranges"))  # النتيجة: I like oranges
```

### 2.5. طريقة `split(separator)`

- تقسيم النص إلى قائمة (List) من الكلمات أو الأجزاء، بناءً على الفاصل المحدد.
- الفاصل الافتراضي هو المسافة.

```python
text = "Python is easy"
words = text.split()
print(words)  # النتيجة: ['Python', 'is', 'easy']

# مثال بفاصل مخصص
csv = "apple,banana,orange"
fruits = csv.split(",")
print(fruits)  # النتيجة: ['apple', 'banana', 'orange']
```

---

## 3. ملخص

| الطريقة        | الوصف                             | مثال الاستخدام                 |
|----------------|---------------------------------|-------------------------------|
| `lower()`      | تحويل النص إلى أحرف صغيرة       | `"Hello".lower() -> "hello"`  |
| `upper()`      | تحويل النص إلى أحرف كبيرة       | `"Hello".upper() -> "HELLO"`  |
| `strip()`      | إزالة المسافات من البداية والنهاية| `"  hi  ".strip() -> "hi"`    |
| `replace(old,new)` | استبدال جزء من النص بجزء آخر| `"cat".replace('c','b') -> "bat"` |
| `split(separator)` | تقسيم النص إلى قائمة أجزاء    | `"a,b,c".split(',') -> ['a','b','c']` |

---

## 4. أمثلة برمجية كاملة

```python
# مثال 1: تحويل نص إلى صغير وكبير
name = "Ahmed"
print(name.lower())  # ahmed
print(name.upper())  # AHMED

# مثال 2: إزالة المسافات الزائدة
message = "   Welcome to Python!   "
print(message.strip())  # Welcome to Python!

# مثال 3: استبدال كلمة في نص
sentence = "I love cats"
new_sentence = sentence.replace("cats", "dogs")
print(new_sentence)  # I love dogs

# مثال 4: تقسيم النص إلى كلمات
data = "apple orange banana"
fruits = data.split()
print(fruits)  # ['apple', 'orange', 'banana']

# مثال 5: تقسيم نص بفاصل معين
csv_line = "1,2,3,4,5"
numbers = csv_line.split(",")
print(numbers)  # ['1', '2', '3', '4', '5']
```

---

## 5
