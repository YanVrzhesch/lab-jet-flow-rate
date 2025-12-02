import jetFunctions as jf
import time
import numpy as np
import matplotlib.pyplot as plt

jf.initSpiAdc()
jf.initStepMotorGpio()

def get_pressure():
    sump = 0
    countp = 0
    for i in range(100):
        pm = jf.getAdc()
        if 0 <= pm < 300000:
            sump += pm
            countp += 1
        time.sleep(0.05)
    return sump/countp

filename = "150mmhighres.txt"
print("experiment begins, filename:", filename)
a = input("confirm")

N = 50
P = [] # N давлений от x
step_length = int(750/N)

for i in range(N):
    P.append( get_pressure() )
    jf.stepForward(step_length)

jf.stepBackward(step_length*N)

with open(filename, 'w') as f:
    for line in P:
        f.write(str(line) + '\n')

plt.plot(np.linspace(1, N, N), P)
plt.show()

jf.deinitSpiAdc()
jf.deinitStepMotorGpio()