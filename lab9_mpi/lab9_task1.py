from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

last_rank = size - 1

if rank == 0:
    random_num=random.randint(1, 10)
    message = {"text": "hello world!", "vals": [random_num]}
    comm.send(message, dest=1, tag=1)

    #looping though next ranks, rank 0 is waiting for last_rank

    message = comm.recv(source=last_rank, tag=1)
    message["text"] = message["text"] + "... goodbye world!"
    
    
    #formatting the print statement so it looks like a list
    hello = "hello world!"
    goodbye = "goodbye world!"
    numbers = " ".join(map(str, message["vals"]))

    print(f"{hello} {numbers} {goodbye}")

elif rank == last_rank:
    message = comm.recv(source=rank-1, tag=1)

    next_value = message["vals"][-1] * rank
    message["vals"].append(next_value)

    comm.send(message, dest=0, tag=1)

else:
    message = comm.recv(source=rank-1, tag=1)

    next_value = message["vals"][-1] * rank
    message["vals"].append(next_value)

    comm.send(message, dest=rank + 1, tag=1)