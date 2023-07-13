#!/usr/bin/python3
'''The minimum operations coding challenge.
'''

def minOperations(n):
    '''Calculates the minimum number of operations required to achieve a 
    desired outcome of precisely n occurrences of the character 'H'.
    '''
    if not isinstance(n, int):
        return 0
    operations = 0
    clip = 0
    result = 1
    # print('H', end='')
    while result < n:
        if clip == 0:
            # init (the first copy all and paste)
            clip = result
            result += clip
            operations += 2
            # print('-(11)->{}'.format('H' * result), end='')
        elif n - result > 0 and (n - result) % result == 0:
            # copy all and paste
            clip = result
            result += clip
            operations += 2
            # print('-(11)->{}'.format('H' * result), end='')
        elif clip > 0:
            # paste
            result += clip
            operations += 1
            # print('-(01)->{}'.format('H' * result), end='')
    # print('')
    return operations
