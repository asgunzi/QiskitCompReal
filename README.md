# QiskitCompReal
Rodar o qiskit num computador quântico real


Rodando um computador quântico real

A IBM disponibiliza alguns computadores quânticos para serem rodados, via cloud.

Vamos rodar um exemplo, utilizando a linguagem Qiskit.

Primeiramente vamos criar um circuito comum.

Circuito terá dois qubits, e será um estado emaranhado.

from qiskit import *

from qiskit.visualization import plot_histogram

circuit = QuantumCircuit(2,2)

circuit.h(0)

circuit.cx(0,1)

circuit.measure(qr,cr)

print(circuit)

Note que é utilizada uma porta Hadamard no qubit 0, e um X controlado de 0 para 1, chegando ao estado

![](https://informacaoquantica.files.wordpress.com/2020/08/entangledstate.png)

#Vamos rodar num simulador de computador quântico. Qasm vem de “quantum assembly simulator”.

simulator = Aer.get_backend('qasm_simulator')

results = execute(circuit,simulator).result().get_counts()

plot_histogram(results)

Num simulador clássico, dá o seguinte resultado: 50% de chance de chegar em |00> e 50% de chance de chegar em |11>.

![](https://informacaoquantica.files.wordpress.com/2020/08/result01.png?w=403)

Agora, vamos rodar no computador real.

A IBM disponibiliza o acesso a um computador real via cloud. Primeiro temos que abrir uma conta na IBM, na página a seguir.

https://quantum-computing.ibm.com/login

Ao obter a conta, você ganha um número de registro, para identificação quando acessar a plataforma.

Para salvar a conta no computador, o comando a seguir:

IBMQ.save_account('APIKEY', overwrite=True)

O código a seguir carrega a conta, especifica qual o computador que queremos utilizar e manda rodar.

IBMQ.load_account()

provider = IBMQ.get_provider(hub = 'ibm-q')

device = provider.get_backend('ibmq_16_melbourne')

job = execute(circuit,backend = device,shots = 1024)

print(job.job_id())

Há uma série de comandos para monitoramento do job no computador. Ele pode ficar em fila por um tempo. Depois do computador rodar ele dá o resultado e retorna para o nosso processo.

No caso, foi rodado 1024 vezes. Nós temos sempre que rodar isso mais uma vez por conta de efeito de erro – ainda não há correção de erros.

from qiskit.tools.monitor import job_monitor

job_monitor(job)

device_result = job.result()

plot_histogram(device_result.get_counts(circuit))

Display: o job está em sexto na fila:

![](https://informacaoquantica.files.wordpress.com/2020/08/display01.png)


Após rodar:

![](https://informacaoquantica.files.wordpress.com/2020/08/display02.png)

O resultado:

![](https://informacaoquantica.files.wordpress.com/2020/08/result02.png)

Valores como |01> e |10> são completamente errados, o que mostra o efeito de vários erros que ainda ocorrem computadores quânticos.

Para verificar os backends disponíveis: providers.backends()


Cada máquina tem sua especificação particular: número de qubits, arquitetura, comportamento quanto a erros, etc…

Portanto, este tutorial mostrou um computador quântico de verdade em ação.

Estamos ainda no jardim da infância desta tecnologia. Vamos continuar acompanhando a sua evolução.

Vide:

https://informacaoquantica.wordpress.com/roadmap-computacao-quantica/

A natureza probabilística, Heisenberg e o Eterno Retorno:
https://ideiasesquecidas.com/2020/08/16/a-natureza-probabilistica-heisenberg-e-o-eterno-retorno/
