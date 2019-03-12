import threading
import os
from subprocess import Popen, PIPE

import subprocess

# def worker0():
#     os.system('python app_v1.py')
#
# t0 = threading.Thread(target=worker0)
# t0.start()
# threading._sleep(5)
# print('========= app is running =========')


process = subprocess.Popen(["python", "app_v1.py"], stdout=subprocess.PIPE)
output = process.stdout.readline()

# while True:
#     if output == '' and process.poll() is not None:
#         break
#     if output:
#         print(output.strip())
#     rc = process.poll()

raw_input('hi')