import datetime

today = datetime.date.today()
tgl_ujian = today.day

print("Angka tanggal hari ini:", tgl_ujian)
hasil = 1
for i in range(1, tgl_ujian + 1):
    hasil *= i
print("Hasil kali dari 1 hingga", tgl_ujian, "adalah:", hasil)
