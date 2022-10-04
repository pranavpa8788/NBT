import subprocess
import os
import newai

for filename in os.listdir('.') :
    if filename.endswith('.jpg') or filename.endswith('.png') :
        newai.main(filename)
