# cyclic-task-scheduler
Um agendador de tarefas simples, usando JSON para agendamentos e controle, sem preocupação com riscos e segurança. Use at your own risk.

o programa *roda-flask.bat* aciona a GUI de agendamento (em modo desenvolvimento, localhost:5000)
o programa *roda.py* inicializa o scheduler. Neste exemplo está configurado para ciclar de 10 em 10 segundos.

TODO:
* threading, permitindo N execuções simultâneas de agendamentos
* tratamento de erro usando e-mail (código base disponível em outro repositorio meu)
* desativar processos agendados pela GUI
* agendamento pontual -> inclui refazer o roda.py e criar um novo json
* logs ficam armazenadas em json
* suporte a códigos SQL (.sql) via PyODBC


## Layout 
![image](https://raw.githubusercontent.com/ryamauti/cyclic-task-scheduler/master/images/screenshot.JPG)


## Arquitetura alvo
![image](https://raw.githubusercontent.com/ryamauti/cyclic-task-scheduler/master/images/arquitetura-alvo.JPG)