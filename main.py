#!/usr/bin/env python3

import os

bash_command = ["cd ~/4", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
dir = os.popen("cd").read()
print(dir)
#is_change = False
prepare_result = []
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result.append(result.replace('\tmodified:   ', ''))
for name in prepare_result:
    print(name)