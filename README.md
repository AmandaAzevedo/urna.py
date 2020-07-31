# urna.py
Projeto final da disciplina de Introdução à Programação.


## O que é necessário para rodar o projeto?
- Python 3
- Pygame 1.9

### Como instalar o Pygame?
Windows:

    pip install pygame
    
Unix:

    pip3 install pygame
    

## Como rodar o projeto? 

Execute o arquivo `urna2.0.py` no terminal:

    python3 urna2.0.py
    

## Observações
- Este projeto não possui conexão com banco de dados, ao invés disso os dados são salvos em arquivos `.txt`.
- Os dados são salvos seguindo os seguintes formatos:

Para eleitores que NÃO votaram ainda:

    MATRÍCULA DO ALUNO; NOME DO ALUNO; NOME DO CURSO; PERÍODO DE INGRESSO NO CURSO; `False`
    
Para eleitores que VOTARAM:

    MATRÍCULA DO ALUNO; NOME DO ALUNO; NOME DO CURSO; PERÍODO DE INGRESSO NO CURSO; `True`

Para candidatos:

    NÚMERO; NOME DO CANDIDATO; NOME DO VICE-CANDIDATO; NOME DO PARTIDO; NÚMERO DE VOTOS
