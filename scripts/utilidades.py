import os
import collections

import fileinput #necesario para reemplazar cadenas como se hace con sed -i
import subprocess

def sustituir(fichero,cadenavieja,cadenanueva):
    subprocess.call(["sed", "-i",'s/'+cadenavieja+'/'+cadenanueva+'/g',fichero])


