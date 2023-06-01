from module_lab6 import *

network = Network()
network.read_network('network_waka_voyage.txt')


source_name = 'Taiwan'
destination_name = 'Hokianga'

distance, path = spath_algorithm(network, source_name, destination_name)

print(distance)
print(path)

# Island = Network.get_node(network, 'Taiwan')
#
# print(Island)

# TODO - your code here
