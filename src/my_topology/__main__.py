"""
Example empty topology. See Heron docs on building python topologies.

"""
from heronpy.api.topology import TopologyBuilder

builder = TopologyBuilder("MyTopology")
# TODO: add spouts and bolts

# this is the what produces output about the topology
builder.build_and_submit()
