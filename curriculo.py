import os

print('=============================================================================================')
print('=====================================C U R R Í C U L O=======================================')
print('=============================================================================================')


print('Olá! sou o Henry, e quero te ajudar a montar sou currículo : )')

print('====================================DADOS PESSOAIS===========================================')

#Àrea reservada para o input da dados pessoais

nome= input('Qual seu nome meu Jovem? ')
pais=input('E sua nacionalidade? ')
civil=input('seu status civil? ')
data=input('Sua data de nascimento? ')
rua=input('Sua rua? ')
n=input('N°: ')
complemento=input('Complemento? ')
bairro=input('Qual seu bairro? ')
municipio=input('Seu municipio é? ')
cep=input('Qual seu CEP? ')
numero=input('Celular: ')
email=input('E-mail: ')
os.system("cls")
print('===========================================OBJETIVO=================================================')

#Àrea reservada para input de objetivos
des1=input('Qual área deseja seguir ? ')
des2=input('Outra área que deseja seguir? ')
os.system("cls")
print('===========================================FORMAÇÃO=================================================')

#Àrea reservada para o input da formação escolar
escola=input('Estudou em que escola? ')
ensino=input('Ensino ou nome da graduação? ')
concluido=input('Concluido? ')
if concluido=='sim':
    a=input('Concluido em? ')
else:
    b=input('Previsão de termino? ')

print('deseja adicionar alguma formação? ')
print('lembrando que cursos não são formações, essa informação será adicionada nas próximas fases')
print('sim/não')
uai=input()
if uai== 'sim':
    escola1 = input('Estudou em que escola? ')
    ensino1 = input('Ensino ou nome da graduação? ')
    concluido1=input('Concluido? ')
    if 'sim':
        c = input('Concluido em? ')
    else:
        d = input('Previsão de termino? ')

    print('deseja adicionar alguma formação? ')
    print('lembrando que cursos não são formações, essa informação será adicionada nas próximas fases')
    print('sim/não')
    eai=input()
    if eai == 'sim':
        escola2 = input('Estudou em que escola? ')
        ensino2 = input('Ensino ou nome da graduação? ')
        concluido2=input('Concluido? ')
        if 'sim':
             e = input('Concluido em? ')
        else:
             f = input('Previsão de termino?')

else:
    os.system("cls")

print('======================================EXPERIÊNCIA PROFISSIONAL====================================')
# Àrea reservada para o input de experiências profissionais?
empresa=input('Empresa? ')
cargo=input('Cargo? ')
periodo=input('Periodo? ')
atividades=input('Atividades Exercidas? ')

print('deseja adicionar alguma experiencia? ')
print('sim/não')
des=input()
if des=='sim':
    empresa1= input('Empresa? ')
    cargo1 = input('Cargo? ')
    periodo1=input('Periodo? ')
    atividade=input('Atividades exercidas? ')

    print('deseja adicionar alguma experiencia? ')
    print('sim/não')
    dwe=input()
    if dwe=='sim':
        empresa2 = input('Empresa? ')
        cargo2 = input('Cargo?')
        periodo2 = input('Periodo?')
        atividade2 = input('Atividades exercidas?')

        print('deseja adicionar alguma experiencia?')
        dwe1=input('sim/não')
        if dwe1== 'sim':
            empresa3 = input('Empresa?')
            cargo3 = input('Cargo?')
            periodo3 = input('Periodo?')
            atividade3 = input('Atividades exercidas?')
        else:
            os.system("cls")
    else:
        os.system("cls")
else:
    os.system("cls")




print('======================================================CURSOS===============================================')
# Àrea reservada para o input de cursos

curso=input('Nome do curso?')
instituicao=input('Instituição ?')
tempo=input('Periodo?')
horas=input('Carga Horária?')
habilidades=input('Habilidades Desenvolvidas? ?')

print('deseja adicionar algum curso?')
int=input('sim/não')
if int =='sim':
    curso1=input('Nome do curso?')
    instituicao1=input('Instituição ?')
    tempo1=input('Periodo?')
    horas1=input('Carga Horária?')
    habilidades1=input('Habilidades Desenvolvidas? ?')

    print('deseja adicionar algum curso?')
    int1=input('sim/não')
    if int1=='sim':
        curso2 = input('Nome do curso?')
        instituicao2 = input('Instituição ?')
        tempo2 = input('Periodo?')
        horas2 = input('Carga Horária?')
        habilidades2 = input('Habilidades Desenvolvidas? ?')

        print('deseja adicionar algum curso?')
        int2=input('sim/não')
        if int2 --'sim':
            curso3 = input('Nome do curso?')
            instituicao3 = input('Instituição ?')
            tempo3 = input('Periodo?')
            horas3 = input('Carga Horária?')
            habilidades3 = input('Habilidades Desenvolvidas? ?')

            print('deseja adicionar algum curso?')
            int3=input('sim/não')
            if int3 --'sim':
                curso2 = input('Nome do curso?')
                instituicao2 = input('Instituição ?')
                tempo2 = input('Periodo?')
                horas2 = input('Carga Horária?')
                habilidades2 = input('Habilidades Desenvolvidas? ?')
            else:
                os.system("cls")
        else:
            os.system("cls")
    else:
        os.system("cls")
else:
    os.system("cls")

print('============================================PALESTRAS===========================================')
#Área resrvada para o input de palestras

palestra=input('Nome da palestras ?')
duracao=input('carga horária ?')

print('deseja adicionar alguma palastra?')
ent=input('sim/não')
if ent=='sim':
    palestra1 = input('Nome da palestras ?')
    duracao1 = input('carga horária ?')

    print('deseja adicionar alguma palastra?')
    ent1=input('sim/não')
    if ent1=='sim':
        palestra2 = input('Nome da palestras ?')
        duracao2 = input('carga horária ?')

        print('deseja adicionar alguma palastra?')
        ent2=input('sim/não')
        if ent2== 'sim':
            palestra3 = input('Nome da palestras ?')
            duracao3 = input('carga horária ?')

            print('deseja adicionar alguma palastra?')
            ent3=input('sim/não')
            if ent3 =='sim':
                palestra4 = input('Nome da palestras ?')
                duracao4 = input('carga horária ?')

                print('deseja adicionar alguma palastra?')
                ent4=input('sim/não')
                if ent4=='sim':
                    palestra5 = input('Nome da palestras ?')
                    duracao5 = input('carga horária ?')
                else:
                    os.system("cls")
            else:
                os.system("cls")
        else:
            os.system("cls")
    else:
        os.system("cls")
else:
    os.system("cls")


print('=======================================================INFORMAÇÃO ADICIONAIS====================================')
# Àrea reservada ao input de informações adicionais
disponivel=input(" Qual horario esta disponivel? ?")

os.system("cls")


print("                                               C A R R E G A N D O . . .                   ")
print("                                               C A R R E G A N D O . . .                   ")
print("                                               C A R R E G A N D O . . .                   ")
print("                                               C A R R E G A N D O . . .                   ")
print("                                               C A R R E G A N D O . . .                   ")
print("                                               C A R R E G A N D O . . .                   ")
print("                                               C A R R E G A N D O . . .                   ")
os.system("cls")
print( nome )
print(pais), print(civil), print(data)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")