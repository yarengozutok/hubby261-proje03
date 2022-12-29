
from gensim.models import KeyedVectors

kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)
print(kelimeVektoru)

def benzerKelimeler():
    anahtarKelimeler = input("Anahtar Kelimeler: ").lower().split()
    print("Girilen Kelimeler : "+ str(anahtarKelimeler))
    oneriler = (kelimeVektoru.most_similar(positive=anahtarKelimeler))
    print(oneriler)


    for oneri in oneriler:
        if anahtarKelimeler not in oneri:
            print("https://www.google.com.tr/search?q=" + oneri[0])

    benzerKelimeler()

benzerKelimeler()