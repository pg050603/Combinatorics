# imports
import numpy as np


def interpolate_linear(ti, yi, tj, default=None):
    """
    TODO
    """
    pass


def integrate_composite_trapezoid(tj, yj):
    """
    TODO
    """
    pass


def spath_initialise(network, source_name):
    """
    TODO
    """
    pass


def spath_iteration(network, unvisited):
    """
    TODO
    """
    pass


def spath_extract_path(network, destination_name):
    """
    TODO
    """
    pass


def spath_algorithm(network, source_name, destination_name):
    """
    TODO
    """
    pass


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
