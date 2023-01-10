V=250
obiectele=[[120,150],[40,60],[40,80],[100,120],[150,180]]
raporturile=[]
i=0

for obiect in obiectele:
    raporturile.append([obiect[1]/obiect[0],i])
    i+=1

raporturile_sorted=[]
max=0
index_to_delete=0

while raporturile!=[]:
    for i in range(0,len(raporturile)):
        if(raporturile[i][0]>max):
            max=raporturile[i][0]
            elem_de_adaugat=raporturile[i]
            index_to_delete=i
    raporturile_sorted.append(elem_de_adaugat)
    raporturile.pop(index_to_delete)
    index_to_delete=0
    max=0
pretul_containerului=0
volumul_containerului=0
obiectele_adaugate=[]
i=0
while(volumul_containerului<V and i<=len(raporturile_sorted)):
    if(volumul_containerului+obiectele[raporturile_sorted[i][1]][0]<=V):
        pretul_containerului+=obiectele[raporturile_sorted[i][1]][1]
        volumul_containerului+=obiectele[raporturile_sorted[i][1]][0]
        obiectele_adaugate.append(obiectele[raporturile_sorted[i][1]])
        i+=1
    else:
        break
print("Volumul care va fi ocupat:",volumul_containerului)
print("Pretul obiectelor din container:",pretul_containerului)
print("Lista [volum,pret] a obiectelor adaugate:",obiectele_adaugate)
