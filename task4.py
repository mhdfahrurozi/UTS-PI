class BMI:
    def __init__(self, weight, height): #inisialisasi Constructor
        self.weight = weight
        self.height = height

    def Kg_to_pound(self):
        return self.weight * 2.20462
    
    def m_to_feet(self):
        return self.height * 3.28084
    
    def BMI_Value(self):
        return self.weight / (self.height ** 2)

    def __eq__(self, other):
        return self.weight == other.weight and self.height == other.height

# data masuk ke Class BMI
print(" UTS Pemrograman Integratif -  Task 4 ".center(50, "="))
berat1 = float(input("Masukkan berat Orang-1 (kg): "))
tinggi1 = float(input("Masukkan tinggi Orang-1 (m): "))
person1 = BMI(berat1, tinggi1)
print("Berat Orang-1 dalam Pound =", person1.Kg_to_pound(), "\ndan Tingginya dalam satuan Kaki =", person1.m_to_feet())
print("BMI Orang-1:", person1.BMI_Value())

berat2 = float(input("\nMasukkan berat Orang-2 (kg): "))
tinggi2 = float(input("Masukkan tinggi Orang-2 (m): "))
person2 = BMI(berat2, tinggi2)
print("Berat Orang-2 dalam Pound =", person2.Kg_to_pound(), "\ndan Tingginya dalam satuan Kaki =", person2.m_to_feet())
print("BMI Orang-2:", person2.BMI_Value())

if person1 == person2:
    print("Orang ke 1 dan Orang ke 2 memiliki berat dan tinggi yang sama.")
else:
    print("Orang ke 1 dan Orang Ke 2 memiliki berat dan/atau tinggi yang berbeda.")