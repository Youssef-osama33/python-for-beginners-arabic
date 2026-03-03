# مشروع: آلة حاسبة بسيطة 🧮

def calculator():
    print("مرحباً بك في الآلة الحاسبة البسيطة!")
    print("العمليات المتاحة: +, -, *, /")

    while True:
        try:
            # طلب الأرقام والعملية من المستخدم
            num1 = float(input("أدخل الرقم الأول: "))
            operator = input("أدخل العملية (+, -, *, /): ")
            num2 = float(input("أدخل الرقم الثاني: "))

            # تنفيذ العملية الحسابية
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("خطأ: لا يمكن القسمة على صفر!")
                    continue
                result = num1 / num2
            else:
                print("خطأ: عملية غير صالحة!")
                continue

            print(f"النتيجة: {num1} {operator} {num2} = {result}")

            # سؤال المستخدم إذا كان يريد الاستمرار
            choice = input("هل تريد إجراء عملية أخرى؟ (نعم/لا): ")
            if choice.lower() != "نعم":
                print("شكراً لاستخدامك الآلة الحاسبة!")
                break
        except ValueError:
            print("خطأ: يرجى إدخال أرقام صحيحة!")

if __name__ == "__main__":
    calculator()
