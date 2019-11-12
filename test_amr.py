import unittest
import AMR

input_file = "/home/stowe/Resources/amrs/abstract_meaning_representation_amr_2.0/data/alignments/split/training/amr-release-2.0-alignments-training-bolt.txt"

class TestAMR(unittest.TestCase):
    def test_loader(self):
        graphs, strings = AMR.graphs_from_file(input_file)

        for i in range(len(graphs)):
            graph = graphs[i]
            s1 = strings[i].strip()
            s2 = AMR.string_from_graph(graph).strip()

            print ("!", s1, "!")
            print ("!", s2, "!")
            self.assertEqual(s1, s2)
            
if __name__ == "__main__":
    unittest.main()
