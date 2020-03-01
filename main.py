import function
if __name__ == "__main__":

    r = int(input("Masukkan jari-jari kerucut: "))
    k = int(input("Masukkan tinggi kerucut: "))

    print ("test calling function{}". format(function.formula().add(r, k)))

    r = int(input("Masukkan jari-jari tabung dan kerucut: "))
    t = int(input("Masukkan tinggi tabung: "))

    print ("test calling function{}". format(function.formula().add(r, t)))
    
