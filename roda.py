#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from datetime import datetime

import dispara

CICLO_SEGUNDOS = 10

while True:
    print('--', datetime.now())
    dispara.dispara()
    sleep(CICLO_SEGUNDOS)

