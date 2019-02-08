'''
The Dutch National Flag Problem
https://en.wikipedia.org/wiki/Dutch_national_flag_problem

I chose to implement an insertion sort algorithm considering the known scope
of the possible variables to sort.
'''


def dutch_flag(arr):
    '''
    # if the number is 'red', move it to the start of the list
    # if the number is 'blue', move it to the end of the list
    # if the number is 'white', move it to the middle
    '''
    # make a new array
    new_array = []
    # this is the index of where 'red' ends and 'white' starts
    pivot = 0
    for n in arr:
        # if the number is 'white'
        if n == 'white':
            # insert at the pivot index
            new_array.insert(pivot, n)
        # if the number is 'red'
        elif n == 'red':
            # move it to the start of the list
            new_array.insert(0, n)
            # and increment pivot point
            pivot += 1
        # if the number is 'blue'
        else:
            # move it to the end of the list
            new_array.append(n)
    return new_array


if __name__ == "__main__":
    print(dutch_flag(
        ['blue', 'blue', 'blue', 'red', 'white', 'blue', 'red', 'white',
         'white', 'white', 'red', 'red', 'white', 'blue', 'white', 'red',
         'white', 'blue', 'white', 'red', 'red']))
