# Yüklenmesi gereken kütüphaneler;
import numpy
import sounddevice as sd # Bu modül, ses sinyallerini NumPy dizisi olarak kaydetmemizi sağlayacak.
from scipy.io.wavfile import write # Bu fonksiyon, NumPy dizisini ses dosyasına dönüştürmemizi sağlayacak.

# Fonksiyon;
def record():
    sampling_freq = 48000 # Örnekleme frekansı [Hertz]
    duration = float(input("Lütfen kaydetmek istediğiniz süreyi saniye cinsinden giriniz: "))
    print("Ses kaydediliyor...")
    recording = sd.rec(int(duration * sampling_freq), samplerate=sampling_freq, channels=2)
    sd.wait()
    print("Ses kaydı tamamlandı.")
    file_name = input("Ses dosyasına bir isim giriniz: ") + ".wav"
    write(filename=file_name, rate=sampling_freq, data=recording)
    print(f"{file_name} başarıyla kaydedildi!")

# Çalıştır;
record()