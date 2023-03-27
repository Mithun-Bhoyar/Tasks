'''
Topic : Designer Door Mat

refer full question : https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
'''

#Solution :

N, M = map(int, input().split())
for i in range(1, N, 2):
    print(str('.|.' * i).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N-2, -1, -2):
    print(str('.|.' * i).center(M, '-'))
