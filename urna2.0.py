# -*- coding: utf8 -*-

from modulosDaUrna import *

eleitores=recuperaEleitores()

candidatos=recuperaCandidatos()


sair=False

while(not sair):
    menu()
    
    op=int(input("Digite a opção que você deseja realizar: "))

    if(op==1):
        print("=========================================================")
        print("             CADASTRAMENTO DOS ELEITORES")
        print("=========================================================")
        matricula=input("Informe a matricula do aluno: ").strip()
        nome=input("Informe o nome do aluno: ").upper()
        print("Cursos:")
        print(" 1.BACHARELADO EM SISTEMAS DE INFORMAÇÃO")
        print(" 2.LICENCIATURA EM CIÊNCIAS DA COMPUTAÇÃO")
        opCurso=int(input("Digite o número respectivo ao do aluno: "))
        if(opCurso == 1):
            curso=("BACHARELADO EM SISTEMAS DE INFORMAÇÃO")
        else:
            curso=("LICENCIATURA EM CIÊNCIAS DA COMPUTAÇÃO")
        
        periodo=input("Informe o período de ingresso do aluno: ")
        if (verificaAMatriculaNaLista(matricula,eleitores)== False):
            eleitores.append([matricula,nome,curso,periodo,False])
            cadastraEleitor(eleitores)
            print("\nO ELEITOR FOI CADASTRADO COM SUCESSO")
        else:
            print("\nO ELEITOR JÁ ESTÁ CADASTRADO")

            
    elif(op == 2):
        print("=========================================================")
        print("                  LISTAR ELEITORES  ")
        print("=========================================================")
        listaEleitores(eleitores)

        
    elif(op == 3):
        print("=========================================================")
        print("               ATUALIZAÇÃO DOS ELEITORES  ")
        print("=========================================================")
        matricula=input("Informe a matrícula a ser atualizada: ")
        atualizaEleitor(matricula,eleitores)
        cadastraEleitor(eleitores)


    elif(op == 4):
        print("=========================================================")
        print("              CADASTRAMENTO DOS CANDIDATOS  ")
        print("=========================================================")
        numero=input("Informe a número do candidato: ").strip()
        nome=input("Informe o nome do candidato: ").upper()
        vice=input("Informe o nome do vice: ").upper()
        partido=input("Informe o nome do partido: ").upper()
        votos=int(0)
        if (verificaONumeroNaLista(numero,candidatos) == False):
            candidatos.append([numero,nome,vice,partido,votos])
            print("\nO CANDIDATO FOI CADASTRADO COM SUCESSO")
        else:
            print("\nO CANDIDATO JÁ ESTÁ CADASTRADO")
        cadastraCandidato(candidatos)


    elif(op == 5):
        print("=========================================================")
        print("                  LISTAR CANDIDATOS  ")
        print("=========================================================")
        listarCandidatos(candidatos)


    elif(op == 6):
        print("=========================================================")
        print("               ATUALIZAÇÃO DOS CANDIDATOS ")
        print("=========================================================")
        atualizaCandidato(candidatos)
        cadastraCandidato(candidatos)


    elif(op == 7):
        print("=========================================================")
        print("                      VOTAÇÃO ")
        print("=========================================================")
        matriculaVerificada=input("Informe a matrícula do eleitor: ").strip()
        for linha in eleitores:
            if (linha[0] == matriculaVerificada and linha[4]=="False"):
                voto=registraVoto(eleitores,candidatos,matriculaVerificada)
                registra=registraQueOEleitorVotou(eleitores,matriculaVerificada)
                del linha[4]
                linha.insert(4,registra)
                cadastraEleitor(eleitores)

                for linha in candidatos:
                    if (voto == linha[0]):
                        contabiliza=str(contabilizaVoto(voto,candidatos))
                        del linha[4]
                        linha.insert(4,contabiliza)
                        cadastraCandidato(candidatos)

                
    elif(op == 8):
        print("=========================================================")
        print("                     CONSULTA DE VOTOS ")
        print("=========================================================")
        print("                       Por candidato")
        print("---------------------------------------------------------")
        consultaVotosPorCandidatos(candidatos,eleitores)
        
                                  
    elif(op == 9):
        print("=========================================================")
        print("                    CONSULTA DE VOTOS ")
        print("=========================================================")
        print("                       Que já votaram")
        print("---------------------------------------------------------")
        consultaNumeroDeEleitoresQueVotaram(eleitores)
        
                                  
    elif(op == 10):
        print("=========================================================")
        print("                   CONSULTA DE VOTOS ")
        print("=========================================================")
        print("                     Que não votaram")
        print("---------------------------------------------------------")
        consultaEleitoresQueNaoVotaram(eleitores)

   
    elif(op == 11):
        sair=True
