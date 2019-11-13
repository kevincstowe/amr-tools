import unittest
import AMR

input_file = "/home/stowe/Resources/amrs/abstract_meaning_representation_amr_2.0/data/alignments/split/training/amr-release-2.0-alignments-training-bolt.txt"

class TestAMR(unittest.TestCase):
    # writes output files to an AMR directory: these are then used as input for the dual graph AMR preprocessor
    def test_writer(self):
        default_training_input = "/home/stowe/Resources/amrs/abstract_meaning_representation_amr_2.0/data/alignments/split/training/"
        default_dev_input = "/home/stowe/Resources/amrs/abstract_meaning_representation_amr_2.0/data/alignments/split/dev/"
        default_test_input = "/home/stowe/Resources/amrs/abstract_meaning_representation_amr_2.0/data/alignments/split/test/"

        with open("/home/stowe/Resources/amrs/NewAmrs/test/data/alignments/split/training/training.txt", "w") as output_file:
            for input_file in os.listdir(inputs[0]):
                graphs, strings = graphs_from_file(inputs[0] + input_file)
                edge_types = set()

                for graph in graphs:
                    s2 = string_from_graph(graph).strip()
                    output_file.write(s2+"\n\n")

        with open("/home/stowe/Resources/amrs/NewAmrs/test/data/alignments/split/dev/dev.txt", "w") as output_file:
            for input_file in os.listdir(inputs[1]):
                graphs, strings = graphs_from_file(inputs[1] + input_file)
                edge_types = set()

                for graph in graphs:
                    s2 = string_from_graph(graph).strip()
                    output_file.write(s2+"\n\n")

        with open("/home/stowe/Resources/amrs/NewAmrs/test/data/alignments/split/test/test.txt", "w") as output_file:
            for input_file in os.listdir(inputs[2]):
                graphs, strings = graphs_from_file(inputs[2] + input_file)
                edge_types = set()

                for graph in graphs:
                    s2 = string_from_graph(graph).strip()
                    output_file.write(s2+"\n\n")

        
    def test_loader(self):
        graphs = AMR.graphs_from_file(input_file)
            
if __name__ == "__main__":
    unittest.main()
