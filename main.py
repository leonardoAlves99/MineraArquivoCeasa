import pandas as pd
from glob import glob
from tika import parser
import xlwt
import re
from datetime import date, datetime
from pymongo import MongoClient

# cluster = MongoClient("mongodb://127.0.0.1:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false") #conexao com a minha base de dados MongoDB
# db = cluster["preco_ceasa"]
# collection = db["historico_precos"]

##caminho da pasta com os dados no PC

# C:/UsersLeonardo Alves\OneDrive - AP SOLUCOES DE GESTAO E TECNOLOGIA LTDA\Documentos\Faculdade\TCC\minhaPastaTcc\AbrilCuritiba2013






def insertBanco(listaProdutos):
    # cont = 0
    print(listaProdutos)
    # while cont < 5:
    #     meusDados = {"data": listaProdutos[0][cont],
    #                  "cultura": listaProdutos[1][cont],
    #                  "status": listaProdutos[2][cont],
    #                  "valor": listaProdutos[3][cont],
    #                  "cidade": listaProdutos[4]}
    #     print(meusDados)

        # collection.insert_one(meusDados)
        # cont += 1

def lerArquivo(pdf):
    dataClassificao = []
    listaProdutos = []
    nomeVerdura = []
    situacaoMercado = []
    valor = []

    arquivo = parser.from_file(pdf)  #formato usado para abrir arquivos PDF`s e extrair o txt
    arquivo = arquivo['content'].lower()  #retorna o arquivo em letras minusculas para facilitar na mineracao
    lista = arquivo.split()

    regexCuritiba = re.findall(r'CeasaCuritiba', pdf)
    regexLondrina = re.findall(r'CeasaLondrina', pdf)
    regexMaringa = re.findall(r'CeasaMaringa', pdf)
    regexCascavel = re.findall(r'CeasaCascavel', pdf)
    regexFozDoIguacu = re.findall(r'CeasaFozdoIguacu', pdf)
    cidade = ''
    if(regexCuritiba):
        cidade = regexCuritiba[0]
    elif (regexLondrina):
        cidade = regexLondrina[0]
    elif (regexMaringa):
        cidade = regexMaringa[0]
    elif(regexCascavel):
        cidade = regexCascavel[0]
    elif(regexFozDoIguacu):
        cidade = regexFozDoIguacu[0]

    filtro = re.compile('([0-9]+)')
    resp = filtro.findall(pdf)
    resp1 = list(map(int, resp))

    filtro = re.compile('([0-9]+)')
    resp = filtro.findall(pdf)

    dd = ''
    mm = ''
    yyyy = ''
    cont = 0

    for a in resp[0]:
        if (cont < 2):
            dd += a
        if (cont >= 2 and cont <= 3):
            mm += a
        if (cont >= 4 and cont <= 8):
            yyyy += a
        cont += 1

    dataTeste = dd +'/'+ mm + '/'+ yyyy
    dataClassificao.append(dataTeste)
    dataClassificao.append(dataTeste)
    dataClassificao.append(dataTeste)
    dataClassificao.append(dataTeste)
    dataClassificao.append(dataTeste)


    for token in lista:
        if token == 'abobrinha':
            pos = lista.index(token)
            nomeVerdura.append(token)
            if lista[pos+6] =='a':
                situacaoMercado.append(lista[pos+9])
                valor.append(lista[pos+11])
                if lista[pos + 11] == '0,00':
                    situacaoMercado.remove(lista[pos + 9])
                    valor.remove(lista[pos + 11])
                    situacaoMercado.append(lista[pos + 23])
                    valor.append(lista[pos + 25])
                if lista[pos+25] == '':
                    situacaoMercado.remove(lista[pos+23])
                    valor.remove(lista[pos+25])
                    situacaoMercado.append(lista[pos+37])
                    valor.append(lista[pos+39])
                if lista[pos+39] == '':
                    situacaoMercado.remove(lista[pos+37])
                    valor.remove(lista[pos+39])
                    situacaoMercado.append(lista[pos+52])
                    valor.append(lista[pos+54])
                # if lista[pos+54] =='0,00':
                #     valor.remove(lista[pos + 54])
                #     valor.append('0,00')


            if lista[pos+6] =='kg':
                situacaoMercado.append(lista[pos + 7])
                valor.append(lista[pos + 9])
                if lista[pos + 9] == '0,00':
                    situacaoMercado.remove(lista[pos + 7])
                    valor.remove(lista[pos + 9])
                    situacaoMercado.append(lista[pos + 33])
                    valor.append(lista[pos + 35])
                # if lista[pos + 22] == '0,00':
                    # situacaoMercado.remove(lista[pos + 20])
                    # valor.remove(lista[pos + 22])
                    # situacaoMercado.append(lista[pos + 33])
                    # valor.append(lista[pos + 35])
                # # if lista[pos + 22] == '0,00':
                #     situacaoMercado.remove(lista[pos + 20])
                #     valor.remove(lista[pos + 22])
                #     situacaoMercado.append(lista[pos + 33])
                #     valor.append(lista[pos + 35])

            # print(lista[pos+1])

    for token in lista:
        if token == 'pepino':
            pos = lista.index(token)
            nomeVerdura.append(token)
            if lista[pos + 6] == 'kg':
                situacaoMercado.append(lista[pos + 7])
                valor.append(lista[pos + 9])
                if lista[pos + 9] == '0,00':
                    situacaoMercado.remove(lista[pos + 7])
                    valor.remove(lista[pos + 9])
                    situacaoMercado.append(lista[pos + 20])
                    valor.append(lista[pos + 22])

            if lista[pos + 7] == 'aus':
                situacaoMercado.remove(lista[pos + 7])
                valor.remove(lista[pos + 9])
                situacaoMercado.append(lista[pos + 15])
                valor.append(lista[pos + 17])
                if lista[pos + 15] == 'kg':
                    situacaoMercado.remove(lista[pos + 15])
                    valor.remove(lista[pos + 17])
                    situacaoMercado.append(lista[pos + 16])
                    valor.append(lista[pos + 18])


            if lista[pos + 5] == 'kg':
                situacaoMercado.append(lista[pos + 6])
                valor.append(lista[pos + 8])
                if lista[pos + 8] == '0,00':
                    situacaoMercado.remove(lista[pos + 6])
                    valor.remove(lista[pos + 8])
                    situacaoMercado.append(lista[pos + 18])
                    valor.append(lista[pos + 20])

            if lista[pos + 5] == 'a':
                situacaoMercado.append(lista[pos + 8])
                valor.append(lista[pos + 10])
                if lista[pos + 10] == '0,00':
                    situacaoMercado.remove(lista[pos + 8])
                    valor.remove(lista[pos + 10])
                    situacaoMercado.append(lista[pos + 23])
                    valor.append(lista[pos + 25])

            if lista[pos + 6] == 'a':
                situacaoMercado.append(lista[pos + 9])
                valor.append(lista[pos + 11])
                if lista[pos + 11] == '0,00':
                    situacaoMercado.remove(lista[pos + 9])
                    valor.remove(lista[pos + 11])
                    situacaoMercado.append(lista[pos + 24])
                    valor.append(lista[pos + 26])

    for token in lista:
        if token == 'pimentão':
            pos = lista.index(token)
            nomeVerdura.append(token)
            if lista[pos + 6] == 'a':
                situacaoMercado.append(lista[pos + 9])
                valor.append(lista[pos + 11])
                if lista[pos + 11] == '0,00':
                    situacaoMercado.remove(lista[pos + 9])
                    valor.remove(lista[pos + 11])
                    situacaoMercado.append(lista[pos + 24])
                    valor.append(lista[pos + 26])
                if lista[pos + 26] == '0,00':
                    valor.remove(lista[pos + 26])
                    valor.append('0,00')

            if lista[pos + 6] == 'kg':
                situacaoMercado.append(lista[pos + 7])
                valor.append(lista[pos + 9])
                if lista[pos + 9] == '0,00':
                    situacaoMercado.remove(lista[pos + 7])
                    valor.remove(lista[pos + 9])
                    situacaoMercado.append(lista[pos + 20])
                    valor.append(lista[pos + 22])

            if lista[pos + 7] == 'aus':
                situacaoMercado.remove(lista[pos + 7])
                valor.remove(lista[pos + 9])
                situacaoMercado.append(lista[pos + 15])
                valor.append(lista[pos + 17])
                if lista[pos + 15] == 'kg':
                    situacaoMercado.remove(lista[pos + 15])
                    valor.remove(lista[pos + 17])
                    situacaoMercado.append(lista[pos + 16])
                    valor.append(lista[pos + 18])



    for token in lista:
        if token == 'tomate':
            pos = lista.index(token)
            nomeVerdura.append(token)
            if lista[pos +6] == '20':
                situacaoMercado.append(lista[pos + 8])
                valor.append(lista[pos + 10])
                if lista[pos + 10] == '0,00':
                    situacaoMercado.remove(lista[pos + 8])
                    valor.remove(lista[pos + 10])
                    situacaoMercado.append(lista[pos + 22])
                    valor.append(lista[pos + 24])

            if lista[pos +6] == 'caixa':
                situacaoMercado.append(lista[pos + 9])
                valor.append(lista[pos + 11])
                if lista[pos + 11] == '0,00':
                    situacaoMercado.remove(lista[pos + 9])
                    valor.remove(lista[pos + 11])
                    situacaoMercado.append(lista[pos + 24])
                    valor.append(lista[pos + 26])

            if lista[pos +3] == 'cx':
                situacaoMercado.append(lista[pos + 64])
                valor.append(lista[pos + 66])
                if lista[pos + 64] == 'aa':
                    situacaoMercado.remove(lista[pos + 64])
                    valor.remove(lista[pos + 66])
                    situacaoMercado.append(lista[pos + 68])
                    valor.append(lista[pos + 70])
                    if lista[pos + 70] == 'longa':
                        situacaoMercado.remove(lista[pos + 68])
                        valor.remove(lista[pos + 70])
                        situacaoMercado.append(lista[pos + 78])
                        valor.append(lista[pos + 80])
                if lista[pos + 64] == 'kg':
                    situacaoMercado.remove(lista[pos + 64])
                    valor.remove(lista[pos + 66])
                    situacaoMercado.append(lista[pos + 65])
                    valor.append(lista[pos + 67])
                    if lista[pos + 67] == 'pr/sp':
                        situacaoMercado.remove(lista[pos + 65])
                        valor.remove(lista[pos + 67])
                        situacaoMercado.append(lista[pos + 76])
                        valor.append(lista[pos + 78])
                if lista[pos + 64] == '22':
                    situacaoMercado.remove(lista[pos + 64])
                    valor.remove(lista[pos + 66])
                    situacaoMercado.append(lista[pos + 66])
                    valor.append(lista[pos + 68])
                    if lista[pos + 66] == 'aus':
                        valor.remove(lista[pos + 68])
                        valor.append('0,00')
                if lista[pos + 64] == 'pr/sp':
                    situacaoMercado.remove(lista[pos + 64])
                    valor.remove(lista[pos + 66])
                    situacaoMercado.append(lista[pos + 60])
                    valor.append(lista[pos + 62])
                if lista[pos + 64] == 'cx':
                    situacaoMercado.remove(lista[pos + 64])
                    valor.remove(lista[pos + 66])
                    situacaoMercado.append(lista[pos + 67])
                    valor.append(lista[pos + 69])
                    if lista[pos + 69] == 'longa':
                        situacaoMercado.remove(lista[pos + 67])
                        valor.remove(lista[pos + 69])
                        situacaoMercado.append(lista[pos + 77])
                        valor.append(lista[pos + 79])
                if lista[pos + 64] == 'local':
                    situacaoMercado.remove(lista[pos + 64])
                    valor.remove(lista[pos + 66])
                    situacaoMercado.append(lista[pos + 70])
                    valor.append(lista[pos + 72])
                if lista[pos + 64] == 'extra':
                    situacaoMercado.remove(lista[pos + 64])
                    valor.remove(lista[pos + 66])
                    situacaoMercado.append(lista[pos + 69])
                    valor.append(lista[pos + 71])
                if lista[pos + 64] == 'longa':
                    situacaoMercado.remove(lista[pos + 64])
                    valor.remove(lista[pos + 66])
                    situacaoMercado.append(lista[pos + 72])
                    valor.append(lista[pos + 74])
                if lista[pos + 64] == 'vida':
                    situacaoMercado.remove(lista[pos + 64])
                    valor.remove(lista[pos + 66])
                    situacaoMercado.append(lista[pos + 71])
                    valor.append(lista[pos + 73])
                if lista[pos + 66] == 'longa':
                    situacaoMercado.remove(lista[pos + 64])
                    valor.remove(lista[pos + 66])
                    situacaoMercado.append(lista[pos + 74])
                    valor.append(lista[pos + 76])
                if lista[pos + 66] == 'vida':
                    situacaoMercado.remove(lista[pos + 64])
                    valor.remove(lista[pos + 66])
                    situacaoMercado.append(lista[pos + 73])
                    valor.append(lista[pos + 75])
            # print(lista[pos+64])

            if lista[pos +6] == '22':
                situacaoMercado.append(lista[pos + 8])
                valor.append(lista[pos + 10])
                if lista[pos + 10] == '0,00':
                    situacaoMercado.remove(lista[pos + 8])
                    valor.remove(lista[pos + 10])
                    situacaoMercado.append(lista[pos + 22])
                    valor.append(lista[pos + 24])

            if lista[pos +7] == '22':
                situacaoMercado.append(lista[pos + 78])
                valor.append(lista[pos + 80])
                if lista[pos + 10] == '0,00':
                    situacaoMercado.remove(lista[pos + 8])
                    valor.remove(lista[pos + 10])
                    situacaoMercado.append(lista[pos + 22])
                    valor.append(lista[pos + 24])
            # print(lista[pos+66])

    for token in lista:
        if token == 'vagem':
            pos = lista.index(token)
            nomeVerdura.append(token)
            if lista[pos + 6] =='a':
                situacaoMercado.append(lista[pos + 9])
                valor.append(lista[pos + 11])
                if lista[pos + 11] == '0,00':
                    situacaoMercado.remove(lista[pos + 9])
                    valor.remove(lista[pos + 11])
                    situacaoMercado.append(lista[pos + 24])
                    valor.append(lista[pos + 26])
            # print(lista[pos+6])

            if lista[pos + 6] =='kg':
                situacaoMercado.append(lista[pos + 7])
                valor.append(lista[pos + 9])
                if lista[pos + 9] == '0,00':
                    situacaoMercado.remove(lista[pos + 7])
                    valor.remove(lista[pos + 9])
                    situacaoMercado.append(lista[pos + 20])
                    valor.append(lista[pos + 22])
                # if lista[pos + 9] == 'Macarrão':
                #     situacaoMercado.remove(lista[pos + 7])
                #     valor.remove(lista[pos + 9])
                #     situacaoMercado.append(lista[pos + 15])
                #     valor.append(lista[pos + 17])

            if lista[pos + 7] == 'aus':
                situacaoMercado.remove(lista[pos + 7])
                valor.remove(lista[pos + 9])
                situacaoMercado.append(lista[pos + 15])
                valor.append(lista[pos + 17])
                if lista[pos + 15] == 'kg':
                    situacaoMercado.remove(lista[pos + 15])
                    valor.remove(lista[pos + 17])
                    situacaoMercado.append(lista[pos + 16])
                    valor.append(lista[pos + 18])

            # print(lista[pos + 6])

            if lista[pos + 7] =='a':
                situacaoMercado.append(lista[pos + 10])
                valor.append(lista[pos + 12])
                if lista[pos + 12] == '0,00':
                    situacaoMercado.remove(lista[pos + 10])
                    valor.remove(lista[pos + 12])
                    situacaoMercado.append(lista[pos + 25])
                    valor.append(lista[pos + 27])
                if lista[pos + 27] == '0,00':
                    situacaoMercado.remove(lista[pos + 25])
                    valor.remove(lista[pos + 27])
                    situacaoMercado.append(lista[pos + 40])
                    valor.append(lista[pos + 42])


    meusDados = {'data': dataClassificao, 'cultura': nomeVerdura, 'situação mercado': situacaoMercado,
             'valor': valor, 'cidade':cidade}


    listaProdutos.append(dataClassificao)
    listaProdutos.append(nomeVerdura)
    listaProdutos.append(situacaoMercado)
    listaProdutos.append(valor)
    listaProdutos.append(cidade)
    insertBanco(listaProdutos)
    listaProdutos.clear()

cont = 0

# for alo in listaProdutos:
#     print(listaProdutos[1])
#     for teste in alo:
#         print(teste)

arquivos = sorted(glob(r'C:/Users/Leonardo Alves/OneDrive - AP SOLUCOES DE GESTAO E TECNOLOGIA LTDA/Documentos/Faculdade'
                       r'/TCC/minhaPastaTcc/CURITIBA/DOISMILEDEZESSETE/aJaneiro/*.pdf'))

for pdf in arquivos:
    # print(pdf)
    lerArquivo(pdf)
