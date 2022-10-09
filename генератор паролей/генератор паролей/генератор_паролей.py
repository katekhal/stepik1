import random
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
neo='il1Lo0O'
chars = ''

print("Создание умного пароля")
psw = int(input('Укажите количество паролей для генерации: '))
length = int(input('Укажите длину одного пароля: '))
print("Включать ли цифры 0123456789? (+/-)")
a = input()
print("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (+/-)")
b = input()
print("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (+/-)")
c = input()
print("Включать ли символы !#$%&*+-=?@^_?")
d = input()
print("Исключать ли неоднозначные символы il1Lo0O? (+/-)")
e = input()
if a == '+':
    chars += digits
if b == '+':
    chars += lowercase_letters
if c == '+':
    chars += uppercase_letters
if d == '+':
    chars += punctuation
if e == '+':
    for i in range(len(neo)):
        chars = chars.replace(neo[i], '')
def generate_password(length, chars):
    passw = ""
    for j in range(length):
        passw += random.choice(chars)
    return passw
for c in range(psw):
    print(generate_password(length, chars))