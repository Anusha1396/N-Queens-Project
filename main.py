from Backtracking import Backtracking
from GA import GA
from HC import Solver

print ("Enter No Of Queens --")
N = int(input())
maxFitness = (N * (N - 1)) / 2  # 8*7/2 = 28

print("\n ************** N-Queen Problem With Backtracking Algorithm ****************** \n")
Backtracking(N)
print("Maximun fitness for {} queens is ".format(N), maxFitness)

print("\n ********************N-Queen Problem With HC Algorithm ********************\n")
hc = Solver(n=N, verbose=False)
hc.runHillClimbing()
aver_runtime = []
print(f"Steps climbed : {hc.getStepsClimbed()}")
print(f"Restarts required : {hc.getRestarts()}")
if hc.getHeuristics()[1] > 0.0:
    print("Stuck at Local Maximal State")
    print(f"Heuristics values : {hc.getHeuristics()[0]} "
          f" {hc.getHeuristics()[1]}")

print("\n ******************** N-Queen Problem With GA Algorithm ***********************\n")
GA(N)



