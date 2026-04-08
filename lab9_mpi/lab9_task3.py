from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


#generate random number for every rank
rand_num = np.random.randint(0,1001)

#find the global max of all the rand_nums using MPI.MAX
global_max = comm.reduce(rand_num, op=MPI.MAX, root=0)

#send global max to all roots
global_max = comm.bcast(global_max, root=0)

if rand_num < global_max:
    print ("Rank", rank, "has value", rand_num, 
           "which is less than global max", global_max
           )
else:
    print ("Rank", rank, "has value", rand_num, 
           "which is the global max", global_max
           )
