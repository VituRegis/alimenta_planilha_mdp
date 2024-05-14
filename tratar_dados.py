import pandas as pd
import datetime
import calendar
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8') # Usado para pegar o nome do mês em PT-BR

CAMPOS = {
    "MN": "MEDIDAS NOVAS",
    "PR": "PRORROGAÇÕES",
    "MR": "MEDIDAS REVOGADAS",
    "DF": "DILIGÊNCIAS A PEDIDO DO FÓRUM",
    "MP": "MANDADO DE PRISÃO",
    "OV": "OCORRÊNCIAS VIA 153"
}

def getCampo(sigla):
    return CAMPOS.get(sigla.upper(), "Campo Desconhecido")

##### VERIFICA SE OS DADOS FORAM INSERIDO DE FORMA CORRETA #####

def verificaAno(var_ano):
    try:
        ano_retorno = int(var_ano)
        if ano_retorno < 2000 or ano_retorno > datetime.datetime.now().year:
            print("\n [ERRO] O ano inserido não é válido.")
            novo_ano = input("\n Insira novamente o ano: ")
            ano_retorno = verificaAno(novo_ano)

        return ano_retorno
    except ValueError:
        print("\n [ERRO] O valor inserido não é um número.")
        novo_ano = input("\n Insira novamente o ano: ")
        ano_retorno = verificaAno(novo_ano)

    return ano_retorno

def verificaMes(var_mes):
    try:
        mes_retorno = int(var_mes)

        if mes_retorno < 1 or mes_retorno > 12:
            print("\n [ERRO] O mês inserido é inválido.")
            novo_mes = input("\n Insira novamente o mês: ")
            mes_retorno = verificaMes(novo_mes)

        return mes_retorno
    except ValueError:
        print("\n [ERRO] O valor inserido não é um número.")
        novo_mes = input("\n Insira novamente o mês: ")
        mes_retorno = verificaMes(novo_mes)

    return mes_retorno

def verificaCampo(var_campo):
    if var_campo.upper() in CAMPOS:
       campo_retorno = getCampo(var_campo)
    else:
       print("\n [ERRO] O valor inserido não é um campo válido.")
       novo_campo = input("\n Insira novamente o CAMPO: ")
       campo_retorno = verificaCampo(novo_campo)
    
    return campo_retorno

def verificaQuant(var_quant):
    try:
        quant_retorno = int(var_quant)
        if quant_retorno <= 0:
            print("\n [ERRO] O valor inserido é inválido.")
            nova_quant = input("\n Insira novamente a quantidade de campos: ")
            quant_retorno = verificaQuant(nova_quant)
        return quant_retorno
    except ValueError: 
        print("\n [ERRO] O valor inserido é inválido.")
        nova_quant = input("\n Insira novamente a quantidade de campos: ")
        quant_retorno = verificaQuant(nova_quant)
    return quant_retorno

##### ALIMENTA E SALVA O CSV #####
def alimentaCsv(ano , mes , campo , quant):
    df = pd.read_csv("arquivo.csv")

    mes = calendar.month_name[mes].lower()

    i = 0

    nova_linha = pd.DataFrame([[mes, campo, ano, f"1 de {mes} de {ano}"]], columns=['mes','natureza','ano','data'])

    while i < quant:
        df = pd.concat([df, nova_linha], ignore_index=True)
        i += 1

    nome_arquivo = "arquivo.csv"
    df.to_csv(nome_arquivo, index=False)

    print(f'\n O CÓDIGO FOI EXECUTADO {i} LINHAS FORAM INSERIDAS.')
    return

#### MAIN ####

print("\n" * 10 + "_" * 15 + " BEM-VINDO AO CONTROLE DE PLANILHA " + "_" * 15 + "\n")

var_ano = input("\nDigite o ANO que deseja inserir na planilha: ")
ano = verificaAno(var_ano)

var_mes = input("\nDigite o MÊS que deseja inserir na planilha (número de 1 à 12): ")
mes = verificaMes(var_mes)

print("\nInsira dessa forma os Campos: \n\n \
      [MN] Medidas Novas [PR] Prorrogações de Medidas [MR] Medidas Revogadas \n \
      [DF] Diligência a pedido do fórum [MP] Mandados de Prisão [OV] Ocorrências Via 153")

var_campo = input("\n\nDigite o CAMPO que deseja inserir na planilha: ")
campo = verificaCampo(var_campo)

var_quant = input("\nDigite a QUANTIDADE que deseja inserir na planilha: ")
quant = verificaQuant(var_quant)

alimentaCsv(ano , mes , campo , quant)

print('_' * 40 + 'EXECUÇÃO OK' + '_' * 40)
