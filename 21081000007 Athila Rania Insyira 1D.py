#program spuder untuk menentukan bilangan terbesar dari beberapa bilangan
#meminta user memasukkan angka

#mencetak judul program
def main():
    print ("menentukan bilangan terbesar dari 3 bilangan")
    
    #data diri
    print("nama : Athila Rania Insyira")
    print("NIM : 21081000007")
    
#mnentukan variable
a = int (input("masukkan bilangan a = "))
b = int (input("masukkan bilangan b = "))
c = int (input("masukkan bilangan c = "))

#menentukan nilai terbesar dan mencetak nilai terbesar dari 3 variable 
if a > b and a > c :
    print (a,"bilangan terbesar dari 3 bilangan yang di inputkan")
elif b > a and b > c :
    print (b,"bilangan terbesar dari 3 bilangan yang di inputkan")
elif c > a and c > b :
    print (c,"bilangan terbesar dari 3 bilangan yang di inputkan")
    