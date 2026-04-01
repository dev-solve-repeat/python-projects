import random

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+=-{|}\][:"

password_length = int(input("Enter your password length: "))

password_gen = "".join(random.sample(password, password_length))

print(f"Your password is {password_gen}")