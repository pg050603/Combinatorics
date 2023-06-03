from module_lab6 import *

network = Network()
network.read_network('network_waka_voyage.txt')
# TODO - your code here

# Determine path of Great Pacific Migration (Taiwan to Hokianga)
source_name = 'Taiwan'
destination_name = 'Hokianga'
distance_t_h, path_t_h = spath_algorithm(network, source_name, destination_name)
print(distance_t_h)
print(path_t_h)

# For determining island pair with maximum possible shortest path:

# Initialise dictionary
mapping = {}

# Iterate through all possible source and destination node combinations
# Get the node names and run algorithm for all combinations
# Map paths as value to distances as key in dict
for node in network.nodes:
    source_name = network.get_node(node.name).name
    for node in network.nodes:
        destination_name = network.get_node(node.name).name
        distance, path = spath_algorithm(network, source_name, destination_name)
        # If paths with duplicate distances exist, store value as list of paths
        if distance in mapping:
            mapping[distance].append(path)
        else:
            mapping[distance] = [path]

# Remove all None combinations (Paths that aren't possible)
del mapping[None]

# Get path of maximum distance and maximum distance and display
max_path = mapping[max(mapping)]
max_distance = max(mapping)
print(max_path)
print(max_distance)
