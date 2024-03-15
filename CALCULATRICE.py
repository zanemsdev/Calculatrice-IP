print("")
print(r"  ______      _             _                      ______   ______  ______  ______")
print(r" / _____)    | |           | |      _             (_____ \ / __   |/ __   |/ __   |")
print(r"| /      ____| | ____ _   _| | ____| |_  ___   ____ ____) ) | //| | | //| | | //| |")
print(r"| |     / _  | |/ ___) | | | |/ _  |  _)/ _ \ / ___)_____/| |// | | |// | | |// | |")
print(r"| \____( ( | | ( (___| |_| | ( ( | | |_| |_| | |   _______|  /__| |  /__| |  /__| |")
print(r" \______)_||_|_|\____)\____|_|\_||_|\___)___/|_|  (_______)\_____/ \_____/ \_____/ ")
print(r"Made by Etann & Rémy")
print("")
print("====================================")
print("")
#Question Poser
ip = input("Enter une ip: ")
mask = input("Enter le masque: ")

print("")
print("====================================")
print("")

#Initialisation des valeurs
listMS = mask.split(".")
listIP = ip.split(".")
bitsMS = [format(int(listMS[0]), '08b') ,format(int(listMS[1]), '08b') ,format(int(listMS[2]), '08b') ,format(int(listMS[3]), '08b')]
bitsIP = [format(int(listIP[0]), '08b') ,format(int(listIP[1]), '08b') ,format(int(listIP[2]), '08b') ,format(int(listIP[3]), '08b')]
MaskF = str(bitsMS[0]+bitsMS[1]+bitsMS[2]+bitsMS[3])
IpF = str(bitsIP[0]+bitsIP[1]+bitsIP[2]+bitsIP[3])
bitUP = MaskF.replace("0", "")
ADr = ADl = ADb = ADf = ADc = IpF[:len(bitUP)]

#Verfication de resultat
if len(ADr) <= 1 :
    exit("Masque non valide")
else:

#Option additonelle

    #Adresse Réseaux
    ADr = ADr.ljust(32, '0')
    print("Adresse reseaux : ",int(ADr[:8], 2),".",int(ADr[8:16], 2),".",int(ADr[16:24], 2),".",int(ADr[24:32], 2))
    
    #Adresse Broadcast
    ADb = ADb.ljust(32, '1')
    print("Adresse broadcast : ",int(ADb[:8], 2),".",int(ADb[8:16], 2),".",int(ADb[16:24], 2),".",int(ADb[24:32], 2))
    
    #Première Adresse
    ADf = str(ADf.ljust(31, '0')+'1')
    print("Première adresse : ",int(ADf[:8], 2),".",int(ADf[8:16], 2),".",int(ADf[16:24], 2),".",int(ADf[24:32], 2))
    
    #Dernière Adresse
    ADl = str(ADl.ljust(31, '1')+'0')
    print("Dernière adresse : ",int(ADl[:8], 2),".",int(ADl[8:16], 2),".",int(ADl[16:24], 2),".",int(ADl[24:32], 2))
    
    #CIDR Adresse
    print("Adresse CIDR : ", str(ip), "/", str(len(bitUP)))
    
    #Le Nombre d'Adresse Dispo
    print("Adresse Dispo : ", pow(2, 32-len(bitUP))-2 )