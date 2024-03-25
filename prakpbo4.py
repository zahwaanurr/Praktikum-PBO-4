class Student:
    data_pribadi = {}

    def __init__(self, nama):
        self.nama = nama
        self.nim = None  

    def set_nim(self, nim):
        self.nim = nim  

    @staticmethod
    def set_nilai(nilai):
        Student.data_pribadi['Nilai'] = nilai

    def set_nilai_teman(self, nilai):
        self.data_pribadi['Nilai'] = nilai

    def get_nama(self):
        return self.nama

    def get_nim(self):
        return self.nim 

    @staticmethod
    def get_nilai():
        return Student.data_pribadi.get('Nilai', "Nilai belum diatur")

    def print_data(self):
        print("---Data Pribadi---")
        print("Nama:", self.nama)
        print("NIM:", self.get_nim())
        print("Nilai:", self.get_nilai())

    @staticmethod
    def print_data_teman(nomor_teman, teman):
        print("---Data Teman", nomor_teman, "---")
        print("Nama:", teman.get_nama())
        print("NIM:", teman.get_nim())
        print("Nilai:", teman.get_nilai())


if __name__ == "__main__":
    praktikan = Student("Zahwa Nur Azkia Putri")

    praktikan.set_nim("064002300038")
    praktikan.set_nilai("100")

    praktikan.print_data()

    teman1 = Student("Calista Azzahra")
    teman2 = Student("Fairuz Maulidya")
    teman3 = Student("Siapa aja")

    teman1.set_nim("064002300008")
    teman2.set_nim("064002300018")
    teman3.set_nim("064002300000")  
    
    teman1.set_nilai_teman("90")
    teman2.set_nilai_teman("85")
    teman3.set_nilai_teman("95")

    Student.print_data_teman(1, teman1)
    Student.print_data_teman(2, teman2)
    Student.print_data_teman(3, teman3)
