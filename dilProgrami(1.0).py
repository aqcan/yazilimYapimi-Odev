import os
import random

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def register(user_count):
    username = input("Kullanıcı adınızı girin: ")
    password = input("Şifrenizi girin: ")
    user = User(username, password)
    with open(f"kullanici{user_count}.txt", "w") as file:
        file.write(f"{user.username}\n{user.password}")
    print(f"Yeni kullanıcı başarıyla oluşturuldu ve 'kullanici{user_count}.txt' olarak kaydedildi: {user.username}")

def login(user_count):
    username = input("Kullanıcı adınızı girin: ")
    password = input("Şifrenizi girin: ")
    for i in range(1, user_count):
        with open(f"kullanici{i}.txt", "r") as file:
            lines = file.readlines()
            if username == lines[0].strip() and password == lines[1].strip():
                print(f"Başarıyla giriş yaptınız! Hoşgeldin {username}.")
                return True
    print("Hatalı kullanıcı adı veya şifre.")
    return False

def main_screen():
    print("1. Giriş Yap")
    print("2. Kayıt Ol")
    choice = input("Seçiminizi yapın (1-2): ")
    return choice

def english_learning_module():
    print("İngilizce pratiğine hazır mısın?")
    print("1. Hazırım")
    choice = input("Seçiminizi yapın (1): ")
    if choice == "1":
        word_pairs = {}
        with open("word_pairs.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                english, turkish, count = line.strip().split(',')
                word_pairs[english] = [turkish, int(count)]

        while True:
            min_count = min(word_pairs.values(), key=lambda x: x[1])[1]
            words_with_min_count = [word for word in word_pairs if word_pairs[word][1] == min_count]
            english_word = random.choice(words_with_min_count)
            turkish_word = word_pairs[english_word][0]
            print(f"Bu İngilizce kelimenin Türkçesi nedir? {english_word}")
            for i in range(2):
                user_answer = input("Cevabınız: ")
                if user_answer == turkish_word:
                    print("Doğru cevap!")
                    word_pairs[english_word][1] += 1
                    if word_pairs[english_word][1] == 6:
                        del word_pairs[english_word]
                    break
                elif i == 0:
                    print("Yanlış cevap, tekrar dene.")
                else:
                    print(f"Üzgünüm, bilemediniz. Cevap {turkish_word} olacaktı.")
            with open("word_pairs.txt", "w") as file:
                for english, (turkish, count) in word_pairs.items():
                    file.write(f"{english},{turkish},{count}\n")

user_count = len([name for name in os.listdir() if name.startswith("kullanici") and name.endswith(".txt")]) + 1
while True:
    choice = main_screen()
    if choice == "1":
        if login(user_count):
            english_learning_module()
    elif choice == "2":
        register(user_count)
        user_count += 1
