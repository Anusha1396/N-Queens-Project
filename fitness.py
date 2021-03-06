import time


def fitness(queens, start_time):
    length = len(queens)

    conflicts = 0                   # number of pieces attacked
    rows = [0] * length
    diag1 = [0] * length * 2
    diag2 = [0] * length * 2

    # row conflicts
    for q in queens:
        rows[q] = rows[q]+1

    # diagonal conflicts
    for i in range(0, length):
        eff = queens[i] + i
        eff2 = length - queens[i] + i
        diag1[eff] = diag1[eff] + 1
        diag2[eff2] = diag2[eff2] + 1

    for r in rows:
        conflicts = conflicts + (r * (r - 1) / 2)       # complete graph

    for i in range(0, len(diag1)):
        conflicts = conflicts + (diag1[i] * (diag1[i] - 1) / 2)  # complete graph
        conflicts = conflicts + (diag2[i] * (diag2[i] - 1) / 2)  # complete graph

    if conflicts == 0:
        print("Result found", queens)
        print("---Total Time is %s seconds---" % (time.time() - start_time))
        exit(0)
    return conflicts