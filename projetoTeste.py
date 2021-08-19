import pandas as pd
from glob import glob
from tika import parser
import xlwt
import re
from pymongo import MongoClient

# cluster = MongoClient("mongodb://127.0.0.1:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false") #conexao com a minha base de dados MongoDB
# db = cluster["dados_ceasa"]
# collection = db["historico_preco"]
# #

def insertBanco(listaProdutos):
    print(listaProdutos)
    cont = 0
    while cont < 5:
        meusDados = {"cidade": listaProdutos[0],
                     "data": listaProdutos[1][cont],
                     "cultura": listaProdutos[2][cont],
                     "status": listaProdutos[3][cont],
                     "valor": listaProdutos[4][cont]}
        print(meusDados)

        collection.insert_one(meusDados)
        cont += 1

def lerArquivo(pdf):

    dataClassificao = []
    dia = []
    mes = []
    ano = []
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
    cidade = ''
    if(regexCuritiba):
        cidade = regexCuritiba[0]
    elif (regexLondrina):
        cidade = regexLondrina[0]
    elif (regexMaringa):
        cidade = regexMaringa[0]

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
                if lista[pos+25] == '0,00':
                    situacaoMercado.remove(lista[pos+23])
                    valor.remove(lista[pos+25])
                    situacaoMercado.append(lista[pos+37])
                    valor.append(lista[pos+39])
                if lista[pos+39] == '0,00':
                    situacaoMercado.remove(lista[pos+37])
                    valor.remove(lista[pos+39])
                    situacaoMercado.append(lista[pos+52])
                    valor.append(lista[pos+54])
                if lista[pos+54] =='0,00':
                    valor.remove(lista[pos + 54])
                    valor.append('0,00')

            if lista[pos+6] =='kg':
                situacaoMercado.append(lista[pos + 7])
                valor.append(lista[pos + 9])
                if lista[pos + 9] == '0,00':
                    situacaoMercado.remove(lista[pos + 7])
                    valor.remove(lista[pos + 9])
                    situacaoMercado.append(lista[pos + 20])
                    valor.append(lista[pos + 22])
                if lista[pos + 22] == '0,00':
                    situacaoMercado.remove(lista[pos + 20])
                    valor.remove(lista[pos + 22])
                    situacaoMercado.append(lista[pos + 33])
                    valor.append(lista[pos + 35])
                if lista[pos + 35] == '0,00':
                    situacaoMercado.remove(lista[pos + 33])
                    valor.remove(lista[pos + 35])
                    situacaoMercado.append(lista[pos + 46])
                    valor.append(lista[pos + 48])

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

            print(lista[pos + 6])

            if lista[pos + 5] == 'a':
                situacaoMercado.append(lista[pos + 8])
                valor.append(lista[pos + 10])
                if lista[pos + 10] == '0,00':
                    situacaoMercado.remove(lista[pos + 8])
                    valor.remove(lista[pos + 10])
                    situacaoMercado.append(lista[pos + 23])
                    valor.append(lista[pos + 25])


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


    for token in lista:
        if token == 'tomate':
            pos = lista.index(token)
            nomeVerdura.append(token)
            if lista[pos +6] == '20':
                situacaoMercado.append(lista[pos + 10])
                valor.append(lista[pos + 12])
                if lista[pos + 12] == '0,00':
                    situacaoMercado.remove(lista[pos + 10])
                    valor.remove(lista[pos + 12])
                    situacaoMercado.append(lista[pos + 26])
                    valor.append(lista[pos + 28])
                if lista[pos + 28] == '0,00':
                    valor.remove(lista[pos + 28])
                    valor.append('0,00')

            if lista[pos +6] == 'caixa':
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

            if lista[pos +6] == '22':
                situacaoMercado.append(lista[pos + 8])
                valor.append(lista[pos + 10])
                if lista[pos + 10] == '0,00':
                    situacaoMercado.remove(lista[pos + 8])
                    valor.remove(lista[pos + 10])
                    situacaoMercado.append(lista[pos + 22])
                    valor.append(lista[pos + 24])


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
                if lista[pos + 26] == '0,00':
                    valor.remove(lista[pos + 26])
                    valor.append('0,00')

            if lista[pos + 6] =='kg':
                situacaoMercado.append(lista[pos + 7])
                valor.append(lista[pos + 9])
                if lista[pos + 9] == '0,00':
                    situacaoMercado.remove(lista[pos + 7])
                    valor.remove(lista[pos + 9])
                    situacaoMercado.append(lista[pos + 20])
                    valor.append(lista[pos + 22])


    meusDados = {'data': dataClassificao, 'cultura': nomeVerdura, 'situação mercado': situacaoMercado,
                 'valor': valor}

    # print(meusDados)
    listaProdutos.append(cidade)
    listaProdutos.append(dataClassificao)
    listaProdutos.append(nomeVerdura)
    listaProdutos.append(situacaoMercado)
    listaProdutos.append(valor)
    insertBanco(listaProdutos)
    listaProdutos.clear()


arquivos = sorted(glob(r'C:/Users/Leonardo Alves/Documents/Faculdade/TCC/minhaPastaTcc/Teste/.pdf'))
for pdf in arquivos:
    lerArquivo(pdf)