def Hanoi(n,A,B,C):
    if n==1:
        C.append(A[-1])
        A.remove(A[-1])
        print('A , B, C:{}\t{}\t{}'.format(A,B,C))
    else:
        Hanoi(n-1,A,C,B)
        Hanoi(1,A,B,C)
        Hanoi(n-1,B,A,C)
n=3
A=list(range(n,0,-1))
B,C=[],[]
print('A , B, C:{}\t{}\t{}'.format(A, B, C))
Hanoi(n,A,B,C)

