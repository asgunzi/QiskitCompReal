# QiskitCompReal
Running a real quantum computer — an easy introduction

IBM offers some quantum computers to be run via the cloud.

Let’s run an example, using the Qiskit language.

First, you’ll have to install Qiskit (https://qiskit.org/).

Let’s create a common circuit.

This circuit will have two qubits.

`from qiskit import *`

`from qiskit.visualization import plot_histogram`

`circuit = QuantumCircuit(2,2)`

`circuit.h(0)`

`circuit.cx(0,1)`

`circuit.measure(qr,cr)`

`print(circuit)`

Note that a Hadamard port is used in qubit 0, and a controlled-X from 0 to 1. The final state is

![](https://informacaoquantica.files.wordpress.com/2020/08/entangledstate.png)

#Let’s run on a quantum computer simulator. Qasm comes from “quantum assembly simulator”.

`simulator = Aer.get_backend('qasm_simulator')`

`results = execute(circuit,simulator).result().get_counts()`

`plot_histogram(results)`

In a simulator, it gives the following result: 50% chance of arriving at |00> and 50% chance of arriving at |11>.

![](https://informacaoquantica.files.wordpress.com/2020/08/result01.png?w=403)

Now, let’s run on the real computer.

IBM provides access to a real computer. We’ll have to open an account with IBM, on the next page.

https://quantum-computing.ibm.com/login

When you get the account, you get a registration number, for identification when accessing the platform.

To save the account on the computer, use the following command:

`IBMQ.save_account('APIKEY', overwrite=True)`

The following code loads the account, specifies which computer we want to use and run it.

`IBMQ.load_account()`

`provider = IBMQ.get_provider(hub = 'ibm-q')`

`device = provider.get_backend('ibmq_16_melbourne')`

`job = execute(circuit,backend = device,shots = 1024)`

`print(job.job_id())`

There are a number of commands for monitoring the job on the computer. He can stand in line for a while. After the computer runs it gives the result and returns to our process.

In this case, it was shot 1024 times. We always have to run this more than once because of the effect of errors — there is no error correction yet.

`from qiskit.tools.monitor import job_monitor`

`job_monitor(job)`

`device_result = job.result()`

`plot_histogram(device_result.get_counts(circuit))`

Display: the job is sixth in the queue:

![](https://informacaoquantica.files.wordpress.com/2020/08/display01.png)


After running:

![](https://informacaoquantica.files.wordpress.com/2020/08/display02.png)

The result is:

![](https://informacaoquantica.files.wordpress.com/2020/08/result02.png)

Values like |01> and |10> are completely wrong, which shows the effect of several errors that still occur in quantum computers.

The name of computer we used isibmq_16_melbourne.There are other choices.

To check the available backends: providers.backends ()


![](https://informacaoquantica.files.wordpress.com/2020/08/display03.png)


Each machine has its particular specification: number of qubits, architecture, behavior regarding errors, ...

This tutorial showed a real quantum computer in action.

We are still in the kindergarten of this technology. We will continue to follow its evolution.



See also:
https://medium.com/@arnaldogunzi/running-a-real-quantum-computer-an-easy-introduction-3ce903c887d4

https://medium.com/@arnaldogunzi/roadmap-quantum-computing-1fc1966513f
