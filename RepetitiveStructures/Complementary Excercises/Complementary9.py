'''Un censador recopila ciertos datos aplicando encuestas para el último Censo Nacional de Población y Vivienda.
Desea obtener de todas las personas que alcance a encuestar en un día, que porcentaje tiene estudios de primaria
secundaria, carrera técnica, estudios profesionales y estudios de posgrado.'''

follow = "SI"
answer= ""
amoountPeople=0
studyPrimary=0
studySecondary=0
tecnicCareer=0
studyProfesional=0
postgraduateStudy=0

while follow == 'SI':
    amoountPeople+=1
    print(f"PERSONA N°{amoountPeople}")
    answer= input("->Tiene estudios primarios? 'si' para SI, cualquier tecla para no.\nDecision: ")
    if answer.upper() == 'SI':
        studyPrimary+=1
        answer= input("->Tiene estudios secundarios? 'si' para SI, cualquier tecla para no.\nDecision: ")
        if answer.upper() == 'SI':
            studySecondary+=1
        else:
            continue
    else:
        continue

    answer= input("->Estudio en una carrera tecnica? 'si' para SI, cualquier tecla para no.\nDecision: ")
    if answer.upper() == 'SI':
            tecnicCareer+=1
    answer= input("->Tiene estudios profesionales? 'si' para SI, cualquier tecla para no.\nDecision: ")
    if answer.upper() == 'SI':
        studyProfesional+=1
    answer= input("->Estudio en un posgrado? 'si' para SI, cualquier tecla para no.\nDecision: ")
    if answer.upper() == 'SI':
        postgraduateStudy+=1
    
    follow=input("¿Desea seguir ingresando personas encuestadas? Escriba SI, para continuar... De lo contrario cualquier tecla\nDecision: ")
    follow= follow.upper()

percentStudyPrimary = (studyPrimary * 100) / amoountPeople
percentStudySecondary = (studySecondary * 100) / amoountPeople
percentStudyTecnicCareer = (tecnicCareer * 100) / amoountPeople
percentStudyProfesional = (studyProfesional * 100) / amoountPeople
percentPostgraduateStudy = (postgraduateStudy * 100) / amoountPeople

print("-------RESULTADOS------")
print(f"TOTAL Personas encuestadas: {amoountPeople}")
print(f"Porcentaje de personas con estudios primarios: %{percentStudyPrimary}")
print(f"Porcentaje de personas con estudios secundarios: %{percentStudySecondary}")
print(f"Porcentaje de personas con estudios carrera tecnica: %{percentStudyTecnicCareer}")
print(f"Porcentaje de personas con estudios profesionales: %{percentStudyProfesional}")
print(f"Porcentaje de personas con estudios de posgrado: %{percentPostgraduateStudy}")
