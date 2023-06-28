#!/bin/bash
screen  -L -Logfile webserver.log -dmS matezweb python3 webserver/main.py &
bash -c "cd chatserver && screen -L -Logfile chatserver.log -dmS matezchat swift run" &