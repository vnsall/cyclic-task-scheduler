import json
from datetime import datetime, timedelta
import time


def proxExecucao(agora, r):
    px = agora + timedelta(minutes=r['periodicidade'])
    ds = px + timedelta(days=1)
    lt = time.strptime(r['horarioFim'], '%H:%M')
    it = time.strptime(r['horarioInicio'], '%H:%M')
    
    # agendar para inicio do dia seguinte:
    # se o proximo evento for depois da hora final, 
    if px.hour > lt.tm_hour or (px.hour == lt.tm_hour and px.minute > lt.tm_min):
        datetime_proxima_execucao = datetime(ds.year, ds.month, ds.day, it.tm_hour, it.tm_min)
    # ou se for antes da hora inicial.
    elif px.hour < it.tm_hour or (px.hour == it.tm_hour and px.minute < it.tm_min):
        datetime_proxima_execucao = datetime(px.year, px.month, px.day, it.tm_hour, it.tm_min)
    else:
        datetime_proxima_execucao = px
    return datetime_proxima_execucao.strftime('%Y-%m-%d %H:%M')


def preparaSaida(c, elem):
    agora = datetime.now()
    temp = dict()    
    temp['nome'] = elem
    temp['script'] = c['script']
    temp['horarioFim'] = c['horarioFim']    
    temp['horarioInicio'] = c['horarioInicio']    
    temp['periodicidade'] = c['periodicidade']        
    if c['executaAoIniciar']:
        temp['proximaExecucao'] = agora.strftime('%Y-%m-%d %H:%M')
    else:
        temp['proximaExecucao'] = proxExecucao(agora, c)
    temp['ultimaExecucao'] = None
    temp['sucesso'] = False
    temp['execucoes'] = 0
    temp['dataConfiguracao'] = agora.strftime('%Y-%m-%d %H:%M')
    temp['ativo'] = True
    c['configurado'] = True
    return temp


def configura(confi, execu):
    for elem in confi:
        c = confi[elem]    
        if not c['configurado']:
            temp = preparaSaida(c, elem)
            execu['rodar'].append(temp)
    return confi, execu


def carrega(tipo):
    if tipo == 'e':
        arq = json.load(open('executa.json', 'r'))
    if tipo == 'c':
        arq = json.load(open('configura.json', 'r'))
    return arq


def gravaConfi(d):
    json.dump(d, open('configura.json', 'w'))


def gravaExecu(d):
    json.dump(d, open('executa.json', 'w'))
     

def rodaAgenda():
    confi = carrega('c')
    execu = carrega('e')    
    confi, execu = configura(confi, execu)
    gravaConfi(confi)
    gravaExecu(execu)


if __name__ == '__main__':
    rodaAgenda()

