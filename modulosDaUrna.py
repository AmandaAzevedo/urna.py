# -*- coding: utf8 -*-

#Módulos da urna
import os
from pygame import mixer


def menu():
    print("=========================================================")
    print("                       URNA DIGITAL")
    print("=========================================================")
    print("\n1) Cadastrar eleitor;")
    print("2) Listar eleitores;")
    print("3) Alterar dados de eleitor;")
    print("4) Cadastrar candidato;")
    print("5) Listar candidatos;")
    print("6) Alterar dados dos candidatos;")
    print("7) Registrar voto indicando a matrícula do eleitor e o \n   número do seu candidato;")
    print("8) Consultar votos obtidos por candidato;")
    print("9) Consultar número de eleitores que já votaram;")
    print("10) Consultar número de eleitores que ainda não votaram;")
    print("11)Sair\n")



def cadastraEleitor(eleitores):
    arquivo= open("dadosDosEleitores.txt",'w', encoding='utf8')
    for e in eleitores:
        arquivo.write("%s;%s;%s;%s;%s\n"%(e[0],e[1],e[2],e[3],e[4]))
    arquivo.close()



def recuperaEleitores ():
    eleitores=[]
    if (os.path.exists("dadosDosEleitores.txt")):
        arquivo=open("dadosDosEleitores.txt",'r', encoding='utf8')
        for linha in arquivo:
            eleitor=linha.strip().split(";")
            eleitores.append(eleitor)
        arquivo.close()
    return eleitores

def verificaAMatriculaNaLista(matricula,eleitores):
    for eleitor in eleitores:
        if (eleitor [0] == matricula):
            return True
    return False



def listaEleitores(eleitores):
    print("\n1) Pesquisar por nome")
    print("2) Pesquisar por matrícula")
    print("3) Listar todos os alunos")
    print("4) Listar alunos por curso")
    print("5) Voltar para ao Menu")
    op=int(input("\nSelecione uma das opcões acima: "))
    
    if (op==1):
        dadoPesquisado=input("\nInforme o nome do eleitor: ").upper()
        for linha in eleitores:
            if (linha[1] == dadoPesquisado):
                print("\nDADOS:")
                print("Nome:{}".format(linha[1]))
                print("Matrícula:{}".format(linha[0]))
                print("Curso:{}".format(linha[2]))
                print("Período de ingresso:{}".format(linha[3]))
                if(linha[4] == "True"):
                    print("Votou: Já votou\n")
                else:
                    print("Votou: Não votou\n")
    elif (op == 2):
        dadoPesquisado=input("\nInforme a matrícula do eleitor: ").strip()
        for linha in eleitores:
            if (linha [0] == dadoPesquisado):
                print("\nDADOS:")
                print("Nome:{}".format(linha[1]))
                print("Matrícula:{}".format(linha[0]))
                print("Curso:{}".format(linha[2]))
                print("Período de ingresso:{}".format(linha[3]))
                if(linha[4] == "True"):
                    print("Votou: Já votou\n")
                else:
                    print("Votou: Não votou\n")
    elif (op == 3):
        for linha in eleitores:
            print("\nDADOS:")
            print("Nome:{}".format(linha[1]))
            print("Matrícula:{}".format(linha[0]))
            print("Curso:{}".format(linha[2]))
            print("Período de ingresso:{}".format(linha[3]))
            if(linha[4] == "True"):
                print("Votou: Já votou\n")
            else:
                print("Votou: Não votou\n")

    elif (op == 4):
        print("1. BACHARELADO EM SISTEMAS DE INFORMAÇÃO")
        print("2. LICENCIATURA EM CIÊNCIAS DA COMPUTAÇÃO")
        dadoPesquisado=int(input("Digite o número correspondente ao curso que você deseja pesquisar: "))
        if(dadoPesquisado == 1):
            for linha in eleitores:
                if (linha [2] == "BACHARELADO EM SISTEMAS DE INFORMAÇÃO" ):
                    print("\nDADOS:")
                    print("Nome:{}".format(linha[1]))
                    print("Matrícula:{}".format(linha[0]))
                    print("Curso:{}".format(linha[2]))
                    print("Período de ingresso:{}".format(linha[3]))
                    if(linha[4] == "True"):
                        print("Votou: Já votou\n")
                    else:
                        print("Votou: Não votou\n")
        else:
            for linha in eleitores:
                if(linha [2] == "LICENCIATURA EM CIÊNCIAS DA COMPUTAÇÃO"):
                    print("\nDADOS:")
                    print("Nome:{}".format(linha[1]))
                    print("Matrícula:{}".format(linha[0]))
                    print("Curso:{}".format(linha[2]))
                    print("Período de ingresso:{}".format(linha[3]))
                    if(linha[4] == "True"):
                        print("Votou: Já votou\n")
                    else:
                        print("Votou: Não votou\n")
            
    else:
        print("\nVocê está de volta ao menu")



def atualizaEleitor(matricula,eleitores):
    for linha in eleitores:
        if linha [0] == matricula:
            print("\n1) Nome:{}".format(linha[1]))
            print("2) Matrícula:{}".format(linha[0]))
            print("3) Curso:{}".format(linha[2]))
            print("4) Período de ingresso:{}".format(linha[3]))
            if(linha[4] == True):
                print("5) Votou: Já votou")
            else:
                print("5) Votou: Não votou")
            print("6) Todos")
            print("7) Voltar ao Menu\n")
            dadoAlterado=int(input("Informe qual dado você deseja alterar: "))
            if (dadoAlterado == 1):
                del linha[1]
                novoNome=input("Digite um novo nome: ").upper()
                linha.insert(1,novoNome)
                print("\nAtualização realizada com sucesso!!!")

            elif (dadoAlterado == 2):
                linha.remove(linha[0])
                novaMatricula=input("Digite a nova matrícula: ").strip()
                linha.insert(0,novaMatricula)
                print("\nAtualização realizada com sucesso!!!")

            elif(dadoAlterado == 3):
                del linha[2]
                novoCurso=input("Digite o curso: ").upper()
                linha.insert(2,novoCurso)
                print("\nAtualização realizada com sucesso!!!")

            elif(dadoAlterado == 4):
                del linha[3]
                novoPeriodo=input("Digite o período: ").strip()
                linha.insert(3,novoPeriodo)
                print("\nAtualização realizada com sucesso!!!")

            elif (dadoAlterado == 5):
                del linha[4]
                linha.insert(4,"True")
                print("\nO sistema realizou a atualização com sucesso!!!")


            elif(dadoAlterado == 6):
                del linha[0]
                novaMatricula=input("Digite a nova matrícula: ").strip()
                linha.insert(0,novaMatricula)
                del linha[1]
                novoNome=input("Digite um novo nome: ").upper()
                linha.insert(1,novoNome)
                del linha[2]
                novoCurso=input("Digite o curso: ").upper()
                linha.insert(2,novoCurso)
                del linha[3]
                novoPeriodo=input("Digite o período: ").strip()
                linha.insert(3,novoPeriodo)
                del linha[4]
                linha.insert(4,"True")
                print("\nAtualização realizada com sucesso!!!")
                
            else:
                print("Você está de volta ao Menu")


                    
def cadastraCandidato(candidatos):
    arquivo= open("dadosDosCandidatos.txt",'w', encoding='utf8')
    for c in candidatos:
        arquivo.write("%s;%s;%s;%s;%s\n"%(c[0],c[1],c[2],c[3],c[4]))
    arquivo.close()



def verificaONumeroNaLista(numero,candidatos):
    for candidato in candidatos:
        if (candidato[0]==numero):
            return True
    return False



def recuperaCandidatos ():
    candidatos=[]
    if (os.path.exists("dadosDosCandidatos.txt")):
        arquivo=open ("dadosDosCandidatos.txt",'r', encoding='utf8')
        for linha in arquivo:
            candidato=linha.strip().split(";")
            candidatos.append(candidato)
        arquivo.close()
    return candidatos
        


def listarCandidatos(candidatos):
    print("\n1) Pesquisar por número")
    print("2) Pesquisar por nome")
    print("3) Listar todos os candidatos")
    print("4) Voltar ao Menu")
    op=int(input("\nDigite a opção que você deseja realizar: "))
    if (op == 1):
        dadoPesquisado=input("Digite o número a ser pesquisado: ")
        for linha in candidatos:
            if (dadoPesquisado == linha[0]):
                print("\nNome:{}".format(linha[1]))
                print("Número:{}".format(linha[0]))
                print("Partido:{}".format(linha[3]))
                print("Vice:{}\n".format(linha[2]))
            
    elif (op == 2):
        dadoPesquisado=input("\nDigite o nome do candidato que você deseja pesquisar: ").upper()
        for linha in candidatos:
            if (dadoPesquisado == linha[1]):
                print("\nNome:{}".format(linha[1]))
                print("Número:{}".format(linha[0]))
                print("Partido:{}".format(linha[3]))
                print("Vice:{}\n".format(linha[2]))

    elif (op == 3):
        for linha in candidatos:
            print("\nNome:{}".format(linha[1]))
            print("Número:{}".format(linha[0]))
            print("Partido:{}".format(linha[3]))
            print("Vice:{}\n".format(linha[2]))

    else:
        print("\nVocê está de volta ao Menu")



def atualizaCandidato(candidatos):
    numero=input("Digite o número do candidato que você deseja alterar os dados: ")
    for linha in candidatos:
        if (numero == linha[0]):
            print("\n1) Nome:{}".format(linha[1]))
            print("2) Número:{}".format(linha[0]))
            print("3) Partido:{}".format(linha[3]))
            print("4) Vice:{}".format(linha[2]))
            print("5) Todos")
            print("6) Voltar ao Menu\n")
            op=int(input("\nDigite a opção que você deseja alterar: "))
            if (op == 1):
                del linha[1]
                novoNome=input("Digite um novo nome: ")
                linha.insert(1,novoNome)
                print("\nAtualização realizada com sucesso!!!")
            elif (op == 2):
                del linha[0]
                novoNumero=input("Digite o novo número: ")
                linha.insert(0,novoNumero)
                print("\nAtualização realizada com sucesso!!!")
            elif (op == 3):
                del linha[3]
                novoPartido=input("Digite o nome do novo partido: ").upper()
                linha.insert(3,novoPartido)
                print("\nAtualização realizada com sucesso!!!")

            elif (op == 4):
                del linha[2]
                novoVice=input("Digite o nome do novo vice: ")
                linha.insert(2,novoVice)
                print("\nAtualização realizada com sucesso!!!")

            elif (op == 5):
                del linha[0]
                novoNumero=input("Digite o novo número: ").strip()
                linha.insert(0,novoNumero)
                del linha[1]
                novoNome=input("Digite um novo nome: ").upper()
                linha.insert(1,novoNome)
                del linha[2]
                novoVice=input("Digite o nome do novo vice: ").upper()
                linha.insert(2,novoVice)
                del linha[3]
                novoPartido=input("Digite o nome do novo partido: ").upper()
                linha.insert(3,novoPartido)
                print("\nAtualização realizada com sucesso!!!\n")


            else:
                print("Você está de volta ao menu")

def musiquinha():
    mixer.init()
    mixer.music.load("urnaMusic.mp3")
    mixer.music.play()
    
def registraQueOEleitorVotou(eleitores,matriculaVerificada):
    for eleitor in eleitores:
        if (eleitor[0] == matriculaVerificada):
            jaVotou="True"
            return jaVotou



def contabilizaVoto(voto,candidatos):
    for candidato in candidatos:
        if (candidato[0] == voto):
            numeroDeVotos=int(candidato[4])
            numeroDeVotos+=1
            return numeroDeVotos



def exibeInformacoesDosEleitores(eleitores,matricula):
    for eleitor in eleitores:
        if (eleitor[0] == matricula):
            print("---------------------------------------------------------")
            print("               VERIFICAÇÃO DO ELEITOR")
            print("---------------------------------------------------------")
            print("NOME: ", eleitor[1])
            print("MATRÍCULA: ",eleitor[0])
            print("CURSO: ",eleitor[2])
            print("PERÍODO: ",eleitor[3],"\n")
    

def registraVoto(eleitores,candidatos,matriculaVerificada):
    exibeInformacoesDosEleitores(eleitores,matriculaVerificada)
    voto=""
    confirmar=False
    while (not confirmar):
        print("---------------------------------------------------------")
        print("                     VOTAÇÃO")
        print("---------------------------------------------------------")
        voto=input("Digite 'B' para votar em branco ou o número do seu candidato: ").upper()
        for candidato in candidatos:
            if (candidato[0]== voto):
                print("Por favor, confirme os dados do seu candidato.\n")
                print("           Presidente")
                print("Número: {}".format(candidato[0]))
                print("Nome: {}".format(candidato[1]))
                print("Vice-presidente: {}".format(candidato[2]))
                print("\nDigite")
                print("1 - Para CONFIRMAR este voto")
                print("2 - Para REINICIAR este voto")
                confirmarVoto=int(input())
                if (confirmarVoto==2):
                    print("---------------------------------------------------------")
                    print("                   Vote novamente")
                    print("---------------------------------------------------------")

                else:
                    print("---------------------------------------------------------")
                    print("                                        Voto Registrado\n")
                    musiquinha()
                    confirmar=True
                    
    return voto



def consultaVotosPorCandidatos(candidatos,eleitores):
    for votos in candidatos:
        print("NOME: ",votos[1])
        print("NÚMERO DE VOTOS: ",votos[4])
        total=len(eleitores)
        votos=int(votos[4])
        porcentagem=(votos*100)/total
        print("CERCA DE: {}%\n".format(porcentagem))



def consultaNumeroDeEleitoresQueVotaram (eleitores):
    cont=0
    for eleitor in eleitores:
        if eleitor[4] == "True":
            cont+=1

    total=len(eleitores)
    porcentagem=(cont*100)/total
    print("O total de eleitores que já votaram é igual a: {} %".format(porcentagem))



def consultaEleitoresQueNaoVotaram (eleitores):
    cont=0
    for eleitor in eleitores:
        if eleitor[4] == "False":
            cont+=1
    total=len(eleitores)
    porcentagem=(cont*100)/total
    print("O total de eleitores que ainda não votaram é igual a: {} %".format(porcentagem))
