"""
1. look for needed changes in driver-experiment.cpp by crtl-f "CHANGE" (comment/uncomment)
2. make all,
3. generate benchmark_72c_grown_ev.txt with generate_experiment.py,
4. execute ./src/driver-experiment < benchmark_72c_grown_ev.txt
"""

import os
import numpy as np



# name = "growk"
# dataset = "datasets/2d_2500n_growing_k/"
# params = np.arange(2, 100, 1)

# name = "8c_grown"
# dataset = os.getcwd() + "/datasets/8c_300d_growing_n_normalized/"
# params = np.arange(100, 6100, 100)

name = "72c_grown"
dataset = os.getcwd() + "/datasets/72c_300d_growing_n_normalized/"
params = np.arange(100, 6100, 100)

benchmark = open("benchmark_"+str(name)+"_ev.txt","w+")
for p in params:
    benchmark.write("dataset "+str(dataset)+str(p)+"_ev.txt "+str(p)+"\n\n")
    benchmark.write("maxiterations 1000\n\n")
    #benchmark.write("initialize "+str(p)+" kpp\n\n")
    #benchmark.write("initialize 8 kpp\n\n")
    benchmark.write("initialize 72 kpp\n\n")
    benchmark.write("threads 1\n")
    benchmark.write("hamerly\n\n")

benchmark.close()
