import json
from datetime import datetime, timedelta
from subprocess import call

def trataErro():
    pass

def dispara():
    execu = json.load(open('executa.json', 'r'))
    confi = json.load(open('configura.json', 'r'))

    for r in execu['rodar']:
        agendada = datetime.strptime(r['proximaExecucao'], '%Y-%m-%d %H:%M')
        agora = datetime.now()
        if agendada < agora:
            r['ultimaExecucao'] = agora.strftime('%Y-%m-%d %H:%M')
            r['execucoes'] += 1
            # agenda para daqui a X min
            c = confi[r['nome']]   
            proxima = agora + timedelta(minutes=c['periodicidade'])
            r['proximaExecucao'] = proxima.strftime('%Y-%m-%d %H:%M')
            try:
                call(["python", r['script']])
            except Exception as e:
                r['sucesso'] = str(e)
                execu['contarErros'] += 1
                trataErro()
            else:
                r['sucesso'] = True
            
    json.dump(execu, open('executa.json', 'w'))

