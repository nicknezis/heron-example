"""
Example empty topology. See Heron docs on building python topologies.
"""

import sys

# Import Grouping and TopologyBuilder from heronpy
from heronpy.api.topology import TopologyBuilder
from heronpy.api.stream import Grouping
import heronpy.api.api_constants as constants

# Import the defined Bolts and Spouts
from .split_sentence_bolt import SplitSentenceBolt
from .word_count_bolt import WordCountBolt
from .random_sentence_spout import RandomSentenceSpout

if __name__ == '__main__':
    # Define the topology name
    # We don't hard code a topology name so that the name
    # can be set at submit time
    builder = TopologyBuilder(sys.argv[1])

    # Define the topology dag

    # Start with the random sentence generator, create a reference and define a parallelism hint with par attribute
    random_sentence_bolt = builder.add_spout("random_sentence_spout", RandomSentenceSpout, par=1)

    # Link the output of the random sentence generator to the split sentence bolt, the input grouping is
    # done on the field `sentence`
    split_sentence_bolt_inputs = {
        random_sentence_bolt: Grouping.fields('sentence')
    }
    # Define the split sentence bolt with the input context defined above and a parallelism hint.
    split_sentence_bolt = builder.add_bolt("split_sentence_bolt", SplitSentenceBolt, par=2,
                                           inputs=split_sentence_bolt_inputs)

    # Link the output of the split sentence bolt to the word count bolt, the input grouping is
    # done on the field `word`
    word_count_bolt_inputs = {
        split_sentence_bolt: Grouping.fields('word')
    }

    # Define emit frequency in seconds, this is used throttle word_count_bolt, log and emit output frequency
    emit_frequency = 3;

    config = {
        constants.TOPOLOGY_TICK_TUPLE_FREQ_SECS: emit_frequency
    }

    # Define the word count bolt with the input context defined above and a parallelism hint and emit frequency config
    # and
    word_count_bolt = builder.add_bolt("word_count_bolt", WordCountBolt, par=2,
                                       inputs=word_count_bolt_inputs, config=config)

    # Finalize the topology graph
    builder.build_and_submit()
