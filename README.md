# English–Turkish Vocabulary Trainer

A console application in **Python** that helps users memorise English–Turkish word pairs using a **6-repetition rule**: a word keeps coming back until the user has answered it correctly six times, then it is considered learned. Built as an assignment for the *Software Construction* (Yazılım Yapımı) course at Manisa Celal Bayar University (2024).

## Features

- User registration and login (stored as text files)
- Admin panel to add and delete words
- **Practice mode:** asks the least-practised words first, gives a second chance on a wrong answer and tracks each word's correct-answer count
- **Exam mode:** 20 random words, 5 points each, score out of 100
- Exam report exported as a Word document (`sinavraporu.docx`) with correct answers in green and wrong ones in red (`python-docx`)

## Sample session

Real output from `dilProgrami(1.2).py`:

```text
1. Giriş Yap
2. Kayıt Ol
3. Admin Girişi
Seçiminizi yapın (1-3): 1
Kullanıcı adınızı girin: sinan
Şifrenizi girin: 1234
Başarıyla giriş yaptınız! Hoşgeldin sinan.
1. Pratik Yap
2. Sınava Gir
Ne yapmak istersiniz? (1-2): 1
Kaç kelime ile pratik yapmak istersiniz? (0-50): 4
Bu İngilizce kelimenin Türkçesi nedir? problem
Cevabınız: sorun
Doğru cevap!
Bu İngilizce kelimenin Türkçesi nedir? good
Cevabınız: kotu
Yanlış cevap, tekrar dene.
Cevabınız: iyi
Doğru cevap!
Bu İngilizce kelimenin Türkçesi nedir? try
Cevabınız: denemek
Doğru cevap!
Bu İngilizce kelimenin Türkçesi nedir? part
Cevabınız: parca
Doğru cevap!
Toplam 4 soru soruldu. 4 tanesini doğru, 0 tanesini yanlış yanıtladınız.
```

## Files

| File | Description |
|---|---|
| `dilProgrami(1.2).py` | Latest version |
| `dilProgrami(1.0).py`, `dilProgrami(1.1s).py` | Earlier iterations |
| `word_pairs.txt` | Word list: `english,turkish,correct_count` |
| `backup_words.txt` | Backup word list |
| `sinavraporu.docx` | Example exam report |

## Running

```bash
pip install python-docx
python "dilProgrami(1.2).py"
```

Admin credentials: `admin` / `admin`.

---

## TR

Kullanıcıların İngilizce-Türkçe kelime çalışmasını ve sınava girmesini sağlayan konsol programı. Bir kelime 6 kez doğru bilinene kadar tekrar sorulur. Admin kelime ekleyip silebilir. Sınav sonunda sorular, verilen cevaplar ve puanlar `sinavraporu.docx` olarak kaydedilebilir.

**Kullanım:** Ana menüde `2` ile kayıt olun, `1` ile giriş yapın. Ardından `1 – Pratik Yap` (istediğiniz sayıda kelime, yanlışta ikinci hak) veya `2 – Sınava Gir` (20 rastgele kelime, her doğru 5 puan) seçin. `3` ile admin girişi yapılır (`admin` / `admin`).
