from module_lab6 import *
network = Network()
network.read_network('network_waka_voyage.txt')
# TODO - your code here

source_name = 'Hokianga'
destination_name = 'Taiwan'

a,b = spath_algorithm(network, source_name, destination_name)

print(a)
print(b)

# mapping = {}
# for node in network.nodes:
#     source_name = network.get_node(node.name).name
#     for node in network.nodes:
#         destination_name = network.get_node(node.name).name
#         distance, path = spath_algorithm(network, source_name, destination_name)
#         #Figure out how to have condition to check if key exists
#         if key exists:
#             mapping[distance].append(path)
#         else:
#             mapping[distance] = [path]
#
# del mapping[None]
#
# max_value = mapping[max(mapping)]
#
# print(max_value)


# filtered_distances = filter(lambda item: item is not None, distances)
# new_lst = list(filtered_distances)
#
# longest_path = max(new_lst)
#
# print(longest_path)




# # Helper function: Returns the distance value of a node with specified name
# def get_distance(distance):
#     return distance
#
# # Return the node in unvisited with the minimum distance
# max_dist = max(distances)
#
# print(max_dist)
#
#
#
#
# print(paths)
# print(distances)
#
#
# #         print(f'The distance between {source_name} and {destination_name} is: {distance}')
# #         print(f'The path to get to {destination_name} from {source_name} is: {path}')
# #
# # Bismarck Sea and Hawaii is: 82.0
# # distance between Palau and Hawaii is: 92.0
# 103.0


