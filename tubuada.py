num = int(input("Digite um numero: "))
i=0
while(i < 16):
    print("{} x {:2} = {}".format(num,i,num*i))
    i+=1
print("{:=^20}".format("Demais"))