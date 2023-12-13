#!/usr/bin/env python
#importando o necessario para o codigo rodar
# Importa a classe Mininet, que e o nucleo da simulacao de rede no Mininet. Ele permite criar e gerenciar topologias de rede virtuais.
from mininet.net import Mininet
#Importa diferentes tipos de controladores que podem ser utilizados para gerenciar switches e hosts na simulacao
from mininet.node import Controller, RemoteController, OVSController
#Importa diferentes tipos de nos (hosts) que podem ser usados na simulacao. Por exemplo, Host representa um host generico, enquanto CPULimitedHost pode limitar a taxa de CPU desse host.
from mininet.node import CPULimitedHost, Host, Node
#Importa tipos de switches que podem ser usados na simulacao. OVSKernelSwitch usa o Open vSwitch no modo de kernel do sistema operacional, enquanto UserSwitch e um switch de software mais simples.
from mininet.node import OVSKernelSwitch, UserSwitch
# Importa um tipo de switch especial, o switch IVS (Indigo Virtual Switch), que e uma alternativa ao Open vSwitch.
from mininet.node import IVSSwitch
#Importa a interface de linha de comando do Mininet, que permite interagir com a topologia simulada, executar comandos nos hosts e switches, e verificar o estado da rede.
from mininet.cli import CLI
#Importa funcoes para configurar o nivel de log do Mininet e exibir informacoes de log.
from mininet.log import setLogLevel, info
# Importa tipos de links que podem ser usados para conectar nos na simulacao. TCLink representa um link com caracteristicas de atraso, largura de banda e perda configuraveis. Intf e usada para associar interfaces fisicas do sistema a simulacao.
from mininet.link import TCLink, Intf
# Importa a funcao call do modulo subprocess, que permite chamar comandos do sistema operacional a partir do Python.
from subprocess import call

def myNetwork():
    # Cria uma nova instancia da rede Mininet
    net = Mininet(topo=None, build=False, ipBase='10.0.0.0/8')

    # Adiciona um controlador a rede
    info('*** Adding controller\n')
    c0 = net.addController(name='c0', controller=Controller, protocol='tcp', port=6633)

    # Adiciona um switch a rede
    info('*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    # Adiciona hosts a rede com IPs especificos e sem rota padrao
    info('*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)

    # Conecta os hosts ao switch
    info('*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s1)

    # Inicia a construcao da rede
    info('*** Starting network\n')
    net.build()

    # Inicia os controladores
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    # Inicia os switches
    info('*** Starting switches\n')
    net.get('s1').start([c0])

    info('*** Post configure switches and hosts\n')

    # Inicia a CLI (Interface de Linha de Comando) do Mininet para interacao
    CLI(net)

    # Para a rede simulada
    net.stop()

if __name__ == '__main__':
    # Define o nivel de log para 'info'
    setLogLevel('info')
    # Chama a funcao myNetwork() se o script for executado como um programa principal
    myNetwork()
