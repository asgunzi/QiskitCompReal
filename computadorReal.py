# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19  12:24:57 2020

@author: asgunzi

"""

from qiskit import *
from qiskit.visualization import plot_histogram

qr = QuantumRegister(2)
cr = ClassicalRegister(2)

#Cria um circuito quântico, composto de um qubit e um bit
circuit = QuantumCircuit(qr,cr)

circuit.h(0)
circuit.cx(0,1)


circuit.measure(qr,cr)

print(circuit)


#Vamos rodar num simulador de computador quântico. Qasm vem de “quantum assembly simulator”.

simulator = Aer.get_backend('qasm_simulator')

results = execute(circuit,simulator).result().get_counts()
plot_histogram(results)



# # #Vamos rodar num computador real

IBMQ.load_account() #È necessário ter uma conta no Qiskit da IBM
provider = IBMQ.get_provider(hub = 'ibm-q')

device = provider.get_backend('ibmqx2')
#Ou ibmq_16_melbourne, ibmqx2   

job = execute(circuit,backend = device,shots = 1024)
print(job.job_id())

from qiskit.tools.monitor import job_monitor

job_monitor(job)
device_result = job.result()
plot_histogram(device_result.get_counts(circuit))


