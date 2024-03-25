import datetime

print(" UTS Pemrograman Integratif -  Task 3 ".center(50, "="))
jumlah_hari = int(input("Masukkan jumlah hari: "))
tanggal = datetime.date.today() + datetime.timedelta(days=jumlah_hari)
tahun = tanggal.strftime("%Y")
hari = tanggal.strftime("%A")
bulan = tanggal.strftime("%B")
tanggal = tanggal.strftime("%d")
print(f"{hari} tanggal {tanggal} {bulan} {tahun}.")