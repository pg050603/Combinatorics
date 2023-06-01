# imports
import collections

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

def interpolate_linear(ti, yi, tj, default=None):
    """
    Linear interpolation on sampled data to a desired set of measurement points

    Arguments:
    ----------
    ti 1D array: Measurement points ti of sampled data
    yi 1D array: Measurement values y(ti) of the sampled data
    tj 1D array: Measurement points, tj , of the desired linearly interpolated data
    default None or other: Optional argument, default value none, value is set for the measurement value, y(tj), when the measurement
    point is outside the sampled data

     -------
    yj 1D array: Measurement values y(tj) for the linearly interpolated data
    TODO
    """

    # Initialise interval lists
    interval_t = []
    interval_y = []

    # Get list of all sub-intervals for t and y
    for i in range(len(ti) - 1):
        sub_t = [ti[i], ti[i + 1]]
        sub_y = [yi[i], yi[i + 1]]
        interval_t.append(sub_t)
        interval_y.append(sub_y)

    # Initialise dictionary mapping for mass change and time
    yj_tj_map = {}

    # For each Measurement point, identify if it is in a sub-interval
    # Use sub-intervals parameters (t and y bounds) to calculate fi(tj)
    for j in range(len(tj)):
        for k in range(len(interval_t)):
            if interval_t[k][0] <= tj[j] <= interval_t[k][1]:
                fi_tj = interval_y[k][0] + (tj[j] - interval_t[k][0]) * (interval_y[k][1] - interval_y[k][0]) / (
                        interval_t[k][1] - interval_t[k][0])
                yj_tj_map[tj[j]] = fi_tj
            elif tj[j] not in yj_tj_map:
                yj_tj_map[tj[j]] = default

    # Get 1D array for times and injection rates
    tj = np.array(list(yj_tj_map.keys()))
    injection_rate = list(yj_tj_map.values())
    yj = np.array(injection_rate)
    return yj


def integrate_composite_trapezoid(tj, yj):
    """
    Uses the Newton-Cotes composite trapezoid rule to integrate: y(t) over the interval t0 to tn-1

    Arguements:
    ----------
    tj 1D array: Measurement points, tj. Assumes closed interval (first and last points are integral limits)
    yj 1D array: Measurement values, y(tj), of the integrand

    Returns:
    -------
    integral float: Numerical approximation of integral
    TODO
    """
    # Initialise the approximation value of integral as 0
    integral = 0

    # Get the integral areas (I) for each of the sub-intervals in the ith timespan within tj
    for i in range(len(tj) - 1):
        I_i = ((tj[i + 1] - tj[i]) / 2) * (yj[i] + yj[i + 1])
        integral = integral + I_i

    return integral

def spath_initialise(network, source_name):
    """
    Sets the initial distance and predecessor node for each node

    Arguments:
    ----------
    network object: An object belonging to the network class
    source_name str: Name of the source node

    Returns:
    --------
    unvisited set: A set containing the names of all nodes in the network
    TODO
    """

    #Initalise the dict mapping
    unvisited = set()

    # Add all nodes in the network to unvisted, initalise distance as infinity and predecessor as None
    for node in network.nodes:
        node.value = [np.inf, None]
        unvisited.add(node.name)
    # For the source node, set distance as 0
    network.get_node(source_name).value = [0, None]




    return unvisited


def spath_iteration(network, unvisited):
    """
    Performs one iteration of the shortest path algorithm

    Arguments:
    ---------
    network object: An object that belongs to the network class
    unvisited set: Set with the names of all currently unsolved nodes in the network

    Returns:
    -------
    solved name str or None: Name of the node that was solved on the current iteration
    TODO
    """
    def get_distance(name):
        node = network.get_node(name)
        return node.value[0]

    interation_name = min(unvisited, key = get_distance)

    # Remove node from unvisited set
    unvisited.remove(interation_name)

    def get_name(arc):
        return arc.from_node.name == interation_name

    # Returns list of all neighbours_arcs
    neighbours_arcs = filter(get_name, network.arcs)
    current_node = network.get_node(interation_name)

    for arc in neighbours_arcs:
        new_distance = arc.weight + current_node.value[0]
        neighbour = arc.to_node
        if neighbour.value[0] > new_distance:
            neighbour.value[0] = new_distance
            neighbour.value[1] = current_node

    return interation_name

def spath_extract_path(network, destination_name):
    """
    Uses chain of predecessors nodes to generate a list of node names for the shortest path

    Arguments:
    ----------
    network object: An object that belongs to the network class
    destination_name str: Name of the destination node

    Returns:
    --------
    path list: List of node names in shortest path, inclusive of start and end

    TODO
    """

    current_node = network.get_node(destination_name)


    predecessor_node = current_node.value[1]

    if predecessor_node == None:
        return [destination_name]

    predecessor_name = current_node.value[1].name

    path = spath_extract_path(network,predecessor_name)

    path.append(destination_name)

    return path


def spath_algorithm(network, source_name, destination_name):
    """
    Uses Dijkstra’s shortest-path algorithm to find shortest path

    Arguments:
    ----------
    network object: An object that belongs to the network class
    source_name str: Name of the source node
    destination_name str: Name of the destination node

    Returns:
    --------
    distance float: The distance (accumulated arc weight) of shortest path, if no solution, return None
    path list: List of node names in shortest path, inclusive of start and end, if no solution, return None
    TODO
    """
    unvisited = spath_initialise(network, source_name)

    while unvisited:
        spath_iteration(network, unvisited)



    path_unchecked = spath_extract_path(network, destination_name)
    distance_unchecked = network.get_node(path_unchecked[-1]).value[0]

    if distance_unchecked == np.inf:
        path = None
        distance = None
    else:
        path = path_unchecked
        distance = distance_unchecked
    return distance, path


class Node(object):
    """
    Object representing network node.

    Attributes:
    -----------
    name : str, int
        unique identifier for the node.
    value : float, int, bool, str, list, etc...
        information associated with the node.
    arcs_in : list
        Arc objects that end at this node.
    arcs_out : list
        Arc objects that begin at this node.
    """

    def __init__(self, name=None, value=None, arcs_in=None, arcs_out=None):

        self.name = name
        self.value = value
        if arcs_in is None:
            self.arcs_in = []
        if arcs_out is None:
            self.arcs_out = []

    def __repr__(self):
        return f"node:{self.name}"


class Arc(object):
    """
    Object representing network arc.

    Attributes:
    -----------
    weight : int, float
        information associated with the arc.
    to_node : Node
        Node object (defined above) at which arc ends.
    from_node : Node
        Node object at which arc begins.
    """

    def __init__(self, weight=None, from_node=None, to_node=None):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node

    def __repr__(self):
        return f"arc:({self.from_node.name})--{self.weight}-->({self.to_node.name})"


class Network(object):
    """
    Basic Implementation of a network of nodes and arcs.

    Attributes
    ----------
    nodes : list
        A list of all Node (defined above) objects in the network.
    arcs : list
        A list of all Arc (defined above) objects in the network.
    """

    def __init__(self, nodes=None, arcs=None):
        if nodes is None:
            self.nodes = []
        if arcs is None:
            self.arcs = []

    def __repr__(self):
        node_names = '\n'.join(node.__repr__() for node in self.nodes)
        arc_info = '\n'.join(arc.__repr__() for arc in self.arcs)
        return f'{node_names}\n{arc_info}'

    def get_node(self, name):
        """
        Return network node with name.

        Parameters:
        -----------
        name : str
            Name of node to return.

        Returns:
        --------
        node : Node, or None
            Node object (as defined above) with corresponding name, or None if not found.
        """
        # loop through list of nodes until node found
        for node in self.nodes:
            if node.name == name:
                return node

        # if node not found, return None
        return None

    def add_node(self, name, value=None):
        """
        Adds a node to the Network.

        Parameters
        ----------
        name : str
            Name of the node to be added.
        value : float, int, str, etc...
            Optional value to set for node.
        """
        # create node and add it to the network
        new_node = Node(name, value)
        self.nodes.append(new_node)

    def add_arc(self, node_from, node_to, weight):
        """
        Adds an arc between two nodes with a desired weight to the Network.

        Parameters
        ----------
        node_from : Node
            Node from which the arc departs.
        node_to : Node
            Node to which the arc arrives.
        weight : float
            Desired arc weight.
        """
        # create the arc and add it to the network
        new_arc = Arc(weight, node_from, node_to)
        self.arcs.append(new_arc)

        # update the connected nodes to include arc information
        node_from.arcs_out.append(new_arc)
        node_to.arcs_in.append(new_arc)

    def read_network(self, filename):
        """
        Reads a file to construct a network of nodes and arcs.

        Parameters
        ----------
        filename : str
            The name of the file (inclusive of extension) from which to read the network data.
        """
        with open(filename, 'r') as file:

            # get first line in file
            line = file.readline()

            # check for end of file, terminate if found
            while line != '':
                items = line.strip().split(',')

                # create source node if it doesn't already exist
                if self.get_node(items[0]) is None:
                    self.add_node(items[0])

                # get starting node for this line
                source_node = self.get_node(items[0])

                for item in items:

                    # initial item ignored as it has no arc
                    if item == source_node.name:
                        continue

                    # separate out to destination node name and arc weight
                    data = item.split(';')
                    destination_node = data[0]
                    arc_weight = data[1]

                    # Create destination node if not already in network, then obtain the node itself
                    if self.get_node(destination_node) is None:
                        self.add_node(destination_node)
                    destination_node = self.get_node(destination_node)

                    # Add arc from source to destination node, with associated weight
                    self.add_arc(source_node, destination_node, float(arc_weight))

                # get next line in file
                line = file.readline()
