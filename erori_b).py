V=250
obiectele=[[120,150],[40,60],[9,0.5],[40,80],[100,120],[150,180],[9,0.5]]
raporturile=[]
i=0
def solutie_posibila(volumul_containerului,volumul_obiectului,V):
    if(volumul_containerului+volumul_obiectului<=V):
        return True
    return False
def prelucrarea_solutiei():
    global pretul_containerului
    global volumul_containerului
    global obiectele_adaugate
    global i
    pretul_containerului+=obiectele[raporturile_sorted[i][1]][1]
    volumul_containerului+=obiectele[raporturile_sorted[i][1]][0]
    obiectele_adaugate.append(obiectele[raporturile_sorted[i][1]])
    return 0

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
print(raporturile_sorted)
while(volumul_containerului<V and i<len(raporturile_sorted)):
    print(i)
    volum=obiectele[raporturile_sorted[i][1]][0]
    if(solutie_posibila(volumul_containerului,volum,V)):
       prelucrarea_solutiei()
       i+=1
    else:
        i+=1
print("Volumul care va fi ocupat:",volumul_containerului)
print("Pretul obiectelor din container:",pretul_containerului)
print("Lista [volum,pret] a obiectelor adaugate:",obiectele_adaugate)
