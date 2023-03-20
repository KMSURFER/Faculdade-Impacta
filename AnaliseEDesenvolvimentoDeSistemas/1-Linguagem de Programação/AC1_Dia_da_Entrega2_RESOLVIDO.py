dia = input()
tempo_de_entrega = int(input())
if dia == "domingo":
    x=1
if dia == "segunda":
    x=2
if dia == "terca":
    x=3
if dia == "quarta":
    x=4
if dia == "quinta":
    x=5
if dia == "sexta":
    x=6
if dia == "sabado":
    x=7
dia_da_entrega = x + tempo_de_entrega
if dia_da_entrega > 7:
    dia_da_entrega -= 7
if  dia_da_entrega == x:
    print ("chega hoje!")
elif dia_da_entrega == 1:
        print ("sera entregue domingo")
elif dia_da_entrega == 2:
        print ("sera entregue segunda")
elif dia_da_entrega == 3:
        print ("sera entregue terca")
elif dia_da_entrega == 4:
    print ("sera entregue quarta")
elif dia_da_entrega == 5:
    print ("sera entregue quinta")
elif dia_da_entrega == 6:
    print ("sera entregue sexta")
elif dia_da_entrega == 7:
    print ("sera entregue sabado")
