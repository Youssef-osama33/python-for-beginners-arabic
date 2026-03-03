# 09_Error_Handling (معالجة الأخطاء) 🐍

في هذا الدرس سنتعرف على كيفية التعامل مع الأخطاء البرمجية في بايثون.

## ⚠️ معالجة الأخطاء (Error Handling)
تستخدم كلمات `try`, `except`, `finally` للتعامل مع الأخطاء البرمجية.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("لا يمكن القسمة على صفر!")
finally:
    print("تم الانتهاء من العملية.")
```

## 📥 أنواع الأخطاء (Exceptions)
هناك عدة أنواع من الأخطاء في بايثون:
- `ZeroDivisionError` (القسمة على صفر)
- `ValueError` (قيمة غير صالحة)
- `TypeError` (نوع غير صالح)
- `FileNotFoundError` (ملف غير موجود)

---

## 🚀 التحدي التاسع
قم بتشغيل ملف `error_handling.py` الموجود في هذا المجلد.
