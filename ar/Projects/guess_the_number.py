# مشروع: لعبة تخمين الرقم 🎮

import random

def guess_the_number():
    print("مرحباً بك في لعبة تخمين الرقم!")
    print("لقد اخترت رقماً بين 1 و 100. هل يمكنك تخمينه؟")

    # اختيار رقم عشوائي بين 1 و 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # طلب التخمين من المستخدم
            guess = int(input("أدخل تخمينك: "))
            attempts += 1

            # مقارنة التخمين بالرقم السري
            if guess < secret_number:
                print("الرقم السري أكبر من ذلك!")
            elif guess > secret_number:
                print("الرقم السري أصغر من ذلك!")
            else:
                print(f"مبروك! لقد خمنت الرقم {secret_number} في {attempts} محاولات.")
                break
        except ValueError:
            print("خطأ: يرجى إدخال رقم صحيح!")

if __name__ == "__main__":
    guess_the_number()
