import unittest
import AMR
import os

DEFAULT_INPUT = "/home/stowe/Resources/amrs/abstract_meaning_representation_amr_2.0/data/alignments/split/training/amr-release-2.0-alignments-training-bolt.txt"

class TestAMR(unittest.TestCase):
    
    # writes output files to an AMR directory: these are then used as input for the dual graph AMR preprocessor
    @unittest.skip("only for outputting dualgraph preprocessing input")
    def test_writer(self):
        default_training_input = "/home/stowe/Resources/amrs/abstract_meaning_representation_amr_2.0/data/alignments/split/training/"
        default_dev_input = "/home/stowe/Resources/amrs/abstract_meaning_representation_amr_2.0/data/alignments/split/dev/"
        default_test_input = "/home/stowe/Resources/amrs/abstract_meaning_representation_amr_2.0/data/alignments/split/test/"

        with open("/home/stowe/Resources/amrs/NewAmrs/test/data/alignments/split/training/training.txt", "w") as output_file:
            for input_file in os.listdir(default_training_input):
                graphs = AMR.graphs_from_file(default_training_input + input_file)
                print (len(graphs))
                for graph in graphs:
                    s2 = AMR.string_from_graph(graph).strip()
                    output_file.write(s2+"\n\n")

        with open("/home/stowe/Resources/amrs/NewAmrs/test/data/alignments/split/dev/dev.txt", "w") as output_file:
            for input_file in os.listdir(default_dev_input):
                graphs = AMR.graphs_from_file(default_dev_input + input_file)

                for graph in graphs:
                    s2 = AMR.string_from_graph(graph).strip()
                    output_file.write(s2+"\n\n")

        with open("/home/stowe/Resources/amrs/NewAmrs/test/data/alignments/split/test/test.txt", "w") as output_file:
            for input_file in os.listdir(default_test_input):
                graphs = AMR.graphs_from_file(default_test_input + input_file)

                for graph in graphs:
                    s2 = AMR.string_from_graph(graph).strip()
                    output_file.write(s2+"\n\n")

    @unittest.skip("basic")
    def test_loader(self):
        graphs = AMR.graphs_from_file(DEFAULT_INPUT)
        return

    def test_nodes(self):
        graphs = AMR.graphs_from_file(DEFAULT_INPUT)
        first_graph = graphs[0]
        print (first_graph)
        new_node = AMR.Node("met", parent_ids=[], attributes={"test":"testing_node"}, children_ids=[])
        first_graph.add_node(new_node)
        print (first_graph)
        return
        
if __name__ == "__main__":
    unittest.main()
