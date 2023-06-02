from module_lab6 import *

network = Network()
network.read_network('network_waka_voyage.txt')

source_name = 'Taiwan'
destination_name = 'Hokianga'

distance, path = spath_algorithm(network, source_name, destination_name)

print(f'The distance between {source_name} and {destination_name} is: {distance}')
print(f'The path to get to {destination_name} from {source_name} is: {path}')

# Island = Network.get_node(network, 'Taiwan')
#
# print(Island)

# TODO - your code here
