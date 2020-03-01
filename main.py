import Identitas

if __name__ == "__main__":

   listNama = ["Aizza Ilmia", "Chanda F", "Siti Badiah", "Dhewi Z", "Indah Dwi"]
   listkelas = [ 4, 4, 4, 4, 4 ]

   listIdentitas = []

   for i in range(len(listkelas)):
       listIdentitas.append(Identitas.Identitas(listNama[i], listkelas[i]))

   print("Show all {}".format(listIdentitas))

   for j in range(len(listIdentitas)):
       print(" nama: {} ".format(listIdentitas[j].show_nama()))
       print(" kelas: {} ".format(listIdentitas[j].show_kelas()))



print("Menghitung Volume Kerucut dalam Tabung")
r = int(input("Masukkan jari-jari kerucut: "))
k = int(input("Masukkan tinggi kerucut: "))

print ("volume kerucut = {}". format(Identitas.kerucut().add(r, k)))

r = int(input("Masukkan jari-jari tabung: "))
t = int(input("Masukkan tinggi tabung: "))

print ("volume tabung = {}". format(Identitas.tabung().add(r, t)))
    
