# amr_tools
Python packages for quickly editing AMR graphs.


Developing easy interfaces for parsing AMR strings into graph-based classes. This will allow for quick and simple editing of AMR graphs at scale.

This project is designed to offer support for generation based on AMR graphs, particular the work of Ribiero et al (2019):
https://github.com/UKPLab/emnlp2019-dualgraph

Currently, the loader can take as input the CoNLL 2015/2017 files, convert them to graphs, convert the graphs back to strings, and input them as preprocessing input to Ribiero's system. The plan is to include additional functionlity to alter the AMRs in graph form to reflect linguistic intuitions, and then write them to strings that can be used as input to AMR systems. 
