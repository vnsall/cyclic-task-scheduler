import json
from datetime import datetime, timedelta
from subprocess import call

from agenda import proxExecucao

def trataErro():
    pass


def dispara():
    execu = json.load(open('executa.json', 'r'))
    #confi = json.load(open('configura.json', 'r'))

    for r in execu['rodar']:
        if not r['ativo']:
            r['proximaExecucao'] = None
        else:
            agendada = datetime.strptime(r['proximaExecucao'], '%Y-%m-%d %H:%M')
            agora = datetime.now()
            if agendada < agora:
                r['ultimaExecucao'] = agora.strftime('%Y-%m-%d %H:%M')                
                r['proximaExecucao'] = proxExecucao(agora, r)               
                try:
                    call(["python", r['script']])
                except Exception as e:
                    r['sucesso'] = str(e)
                    execu['contarErros'] += 1
                    trataErro()
                else:
                    r['sucesso'] = True
                finally:
                    r['execucoes'] += 1
            
    json.dump(execu, open('executa.json', 'w'))

