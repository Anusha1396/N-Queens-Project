import time
#here i am creating a board for N it will assign number dynamically .
def Backtracking(N):

    ChessBoard = [[0] * N for _ in range(N)]
    runtime = 0
    start_time = time.time()

    def is_attacking(i, j):
        #here i am checking the row
        for k in range(0,N):
            if ChessBoard[i][k]=='Q' or ChessBoard[k][j]=='Q':
                return True
    #here i am checking whether there is queen in the diagonal or not
        for k in range(0,N):
            for l in range(0,N):
                if (k+l==i+j) or (k-l==i-j):
                    if ChessBoard[k][l]=='Q':
                        return True


        return False


    def solution(n):
        start_time = time.time()
        if n==0:
            print("Solution for n=0 = 0")
            return True
        for i in range(0,N):
            for j in range(0,N):

                if (not(is_attacking(i, j))) and (ChessBoard[i][j] != 'Q'):
                    ChessBoard[i][j] = 'Q'
                #now checking if we can add other here in same arrangement
                    if solution(n - 1)==True:
                        return True
                    ChessBoard[i][j] = 0

        return False

    solution(N)
    for i in ChessBoard:
        print (i)
    print("--- Total Time is %s seconds ---" % (time.time() - start_time))