import json
from datetime import datetime, timedelta

def horarios(c):
    agora = datetime.now()
    proxima = agora + timedelta(minutes=c['periodicidade'])
    return agora, proxima


def next(nome):
    cfg = carrega('c')
    props = cfg[nome]    
    hi = props['horarioInicio']
    hf = cfg[temp['nome']]['horarioFim']
    #if proxima > 
    proxexec = proxima.strftime('%Y-%m-%d %H:%M')
    return proxexec


def preparaSaida(c, elem):
    agora, proxima = horarios(c)
    temp = dict()    
    temp['nome'] = elem
    temp['script'] = c['script']    
    if c['executaAoIniciar']:
        temp['proximaExecucao'] = agora.strftime('%Y-%m-%d %H:%M')
    else:
        temp['proximaExecucao'] = next(elem)
    temp['ultimaExecucao'] = None
    temp['sucesso'] = False
    temp['execucoes'] = 0
    temp['dataConfiguracao'] = agora.strftime('%Y-%m-%d %H:%M')
    c['configurado'] = True
    return temp


def configura(confi, execu):
    for elem in confi:
        c = confi[elem]    
        if not c['configurado']:
            temp = preparaSaida(c, elem)
            execu['rodar'].append(temp)


def carrega(tipo):
    if tipo == 'e':
        arq = json.load(open('executa.json', 'r'))
    if tipo == 'c':
        arq = json.load(open('configura.json', 'r'))
    return arq


def grava(tipo):
    if tipo == 'e':        
        json.dump(execu, open('executa.json', 'w'))
    if tipo == 'c':
        json.dump(confi, open('configura.json', 'w'))
    if tipo == 'ec':
        json.dump(confi, open('configura.json', 'w'))
        json.dump(execu, open('executa.json', 'w'))
     

if __name__ == '__main__':
    confi = carrega('c')
    execu = carrega('e')
    # os dicionarios e listas sao tratados pelos outros modulos como globais
    configura(confi, execu)
    grava('ec')

