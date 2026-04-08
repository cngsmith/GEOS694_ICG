from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


N = 10000
check_value = (N * (N +1)) // 2

data = None

if rank == 0:
    data = np.arange(1, N + 1, dtype="i")
    data = np.array_split(data, size)

#sending data to other processes
partial = comm.scatter(data, root=0)

#summing the partial array
rank_sum = np.sum(partial)

gathered_sums = comm.gather(rank_sum, root=0)
    

if rank == 0:
    print("The sum of 1 -",N, "is", np.sum(gathered_sums), "==", check_value)