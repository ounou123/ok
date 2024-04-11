import multiprocessing as mp

import monte_carlo

def intagrate(v,N,f):
    m = N//v
    with mp.Pool(processes=v) as pool:
        args = [m for _ in range(v)]
        pool.map(f,args)

if __name__ == "__main__":
    integral_f_paralel = intagrate(4,10000, monte_carlo.proc)
    print(integral_f_paralel)