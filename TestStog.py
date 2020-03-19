from stog.data.dataset_readers.amr_parsing import amr, io

INPUT_PATH = "/home/stowe/GitHub/jamr/test.amr"
ORIGINAL_TEST = "/home/stowe/PycharmProjects/MetaphorResources/processing/seq2seq_data/standard_test_tgt"
MET_TEST = "/home/stowe/PycharmProjects/MetaphorResources/processing/seq2seq_data/standard_test_src"


def run_test(input_path=INPUT_PATH):
    amr_data = [a for a in io.AMRIO.read(input_path)]
    test_y = open(ORIGINAL_TEST).readlines()
    test_x = open(MET_TEST).readlines()

    for i in range(len(amr_data)):
        if "::MET::" in test_x[i]:
            index = test_x[i].split().index("::MET::")
        elif "::LIT::" in test_x[i]:
            index = test_x[i].split().index("::LIT::")
        else:
            continue

        amr_graph = amr_data[i].graph
        word = test_y[i].split()[index]
        nodes = amr_graph.get_nodes()
        edges = amr_graph.get_edges()
        print (amr_graph)
        print (edges)

if __name__ == "__main__":
    run_test()