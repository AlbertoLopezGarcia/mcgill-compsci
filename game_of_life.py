# NOTE: None of the functions should modify input objects.

import doctest

def is_valid_universe(a_list):
    """ (list) -> bool
    Returns True if the list is a vaalid representation of a universe,
    False otherwise. A list is a valid representation if all its
    sublists are of equal length and it contains only 1s and 0s.
    
    >>> a = [[0, 0], [1, 1], [0, 1]]
    >>> is_valid_universe(a)
    True
    >>> b = [[0, 0, 0], [1, 0], [1, 0, 1]]
    >>> is_valid_universe(b)
    False
    >>> c = [[0], [1], [1], [0]]
    >>> is_valid_universe(c)
    True
    >>> d = [[]]
    >>> is_valid_universe(d)
    False
    >>> e =  [[1, 5], [4, 1]]
    >>> is_valid_universe(e)
    False
    """
    # check if a_list is empty
    if a_list == [[]] or a_list == []:
        return False
    
    # create expected_len, to compare other sublists to
    expected_len = len(a_list[0])
       
    for sublist in a_list:
        # check if sublists are the same size
        if len(sublist) != expected_len:
            return False
 
        # check if the elements of the sublists are different than 0 or 1.
        for elem in sublist:
            if elem not in [0, 1]:
                return False
            
    return True

def universe_to_str(valid_universe):
    """ (list) -> str
    Returns the string representation of the valid_universe list,
    replacing 1 by '*' and 0 by ' '.
    The string also contains a surrounding box.
    
    >>> tub = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], \
    [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    >>> str_tub = universe_to_str(tub)
    >>> print(str_tub)
    +-----+
    |     |
    |  *  |
    | * * |
    |  *  |
    |     |
    +-----+
    
    >>> uni = [[0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 0, 1, 0],\
    [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]]
    >>> str_uni = universe_to_str(uni)
    >>> print(str_uni)
    +-----+
    |  *  |
    |*   *|
    | * * |
    | * * |
    |  *  |
    +-----+
    
    >>> duck = [[0, 0, 1, 1, 1], [0, 1, 1, 1, 0], [1, 1, 1, 0, 0],\
    [0, 1, 1, 1, 0], [0, 0, 1, 1, 1]]
    >>> str_duck = universe_to_str(duck)
    >>> print(str_duck)
    +-----+
    |  ***|
    | *** |
    |***  |
    | *** |
    |  ***|
    +-----+
    """
    # initialize variable with the first borderline
    borderline = "+" + "-" * len(valid_universe[0]) + "+"
    str_representation = borderline + '\n'
    
    # print string representation of the universe
    for line in valid_universe:
        # add initial pipe
        str_representation += '|'
        for char in line:
            if char == 0:
                str_representation += ' '
            else:
                str_representation += '*'
        # additional pipe and line break
        str_representation += '|\n'
        
    # add lower borderline
    str_representation += borderline
    
    # output
    return str_representation

def count_live_neighbors(valid_universe, x, y):
    """ (str, int, int) -> int
    Returns the number of live neighboring cells of a particular cell,
    whose position is given by row x and element y, in a given valid
    universe.
    
    >>> boo = [[1, 0, 0, 0, 0, 1], \
               [0, 1, 0, 1, 0, 0], \
               [0, 1, 1, 0, 0, 0], \
               [0, 0, 1, 0, 0, 0], \
               [1, 0, 1, 0, 0, 0]]
    >>> count_live_neighbors(boo, 2, 2)
    4
    >>> count_live_neighbors(boo, 3, 4)
    0
    >>> count_live_neighbors(boo, 0, 4)
    2
    
    >>> foo = [[1, 1, 0, 0, 0, 0], \
                [0, 1, 1, 1, 0, 0], \
                [0, 1, 1, 0, 0, 0], \
                [0, 0, 1, 0, 1, 0], \
                [1, 1, 1, 0, 1, 0]]
    >>> count_live_neighbors(foo, 1, 2)
    5
    >>> count_live_neighbors(foo, 2, 3)
    5
    >>> count_live_neighbors(foo, 4, 5)
    2
    """
    
    # create variable that will store the number of neighboring 1's
    num_live_neighbors = 0
    
    max_x = len(valid_universe)-1
    max_y = len(valid_universe[0])-1
    
    # scan through the matrix in a range of the precedent, the current and
    # the folllowing row and column.
    
    for x_ in range(x-1, x+2):
        # If the index x_ happens to fall outside the grid, ignore that case and
        # continue iterating.
        if x_ > max_x or x_ < 0:
            continue
        
        for y_ in range(y-1, y+2):
            # If the index y_ happens to fall outside the grid, ignore that case and
            # continue iterating.
            if y_ > max_y or y_ < 0:
                continue
            
            # count neighboring 1's
            if valid_universe[x_][y_] == 1:
                num_live_neighbors += 1
        
    # subtract one if valid_universe[x][y] is a 1
    # (a cell cannot be its own neighbor!)
    if valid_universe[x][y] == 1:
        num_live_neighbors -= 1
    
    # output
    return num_live_neighbors
            
def get_next_gen_cell(valid_universe, x, y):
    """ (str, int, int) -> int
    The function returns the state of the specified cell in the next generation
    of the universe, that is, after applying the rules on it.
    
    >>> spaceship = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
    >>> get_next_gen_cell(spaceship, 0, 0)
    0
    >>> get_next_gen_cell(spaceship, 0, 1)
    0
    >>> get_next_gen_cell(spaceship, 1, 0)
    1
    >>> get_next_gen_cell(spaceship, 2, 1)
    1
    
    >>> round = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
    >>> get_next_gen_cell(round, 0, 0)
    1
    >>> get_next_gen_cell(round, 1, 1)
    0
    >>> get_next_gen_cell(round, 3, 3)
    1
    """
    # determining state of given cell
    cell = valid_universe[x][y]
    
    # count neighboring alive cells
    num_live_neighbors = count_live_neighbors(valid_universe, x, y)
    
    # if num_live_neighbors is smaller than 2 or larger than 3, the cell will "die".
    # i.e. it will be equal to zero, no matter what the initial value is.
    if num_live_neighbors not in [2, 3]:
        return 0
    
    # if the cell has exactly three neighbors, it will become alive.
    if num_live_neighbors == 3:
        return 1

    # in every other case, the cell is unaltered.    
    return cell

def get_next_gen_universe(valid_universe):
    """ (str) -> str
    The function returns a two-dimensional list of integers representing the universe
    in its next generation.
    
    >>> cross = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 0], \
                 [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    >>> cross_gen2 = get_next_gen_universe(cross)
    >>> cross_gen2 == [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], \
    [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
    True
    
    >>> tub = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], \
    [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    >>> tub_gen2 = get_next_gen_universe(tub)
    >>> tub_gen2 == [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], \
    [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    True
    
    >>> heart = [[1, 0, 1], [1, 1, 1], [0, 1, 0]]
    >>> heart_gen2 = get_next_gen_universe(heart)
    >>> heart_gen2 == [[1, 0, 1], [1, 0, 1], [1, 1, 1]]
    True
    >>> heart_gen3 = get_next_gen_universe(heart_gen2)
    >>> heart_gen3 == [[0, 0, 0], [1, 0, 1], [1, 0, 1]]
    True
    
    """    
    next_gen_universe = []
        
    max_x = len(valid_universe)
    max_y = len(valid_universe[0])
    
    # apply get_next_gen_cell to every cell on the matrix
    for x in range(max_x):
        
        # fill new_row with values in row y.
        new_row = []
        
        for y in range(max_y):
            new_cell = get_next_gen_cell(valid_universe, x, y)
            
            # append every element on the column to new_row
            new_row.append(new_cell)
            #print("new row:", new_row)
            
        # for every row, append new_row to next_gen_universe
        next_gen_universe += [new_row]
        #print(next_gen_universe)
    # output
    return next_gen_universe
    
def get_n_generations(universe, n):
    """ (list, int) -> list
    Returns a list containing m strings which represent the first m generations
    of the input universe. The strings appear in order starting from the original
    seed.
    If the universe is periodic with period p, then m = min(n, p) and if it is
    not periodic, then simply m = n.
    
    >>> tub = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], \
               [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    >>> g = get_n_generations(tub, 5)
    >>> len(g)
    1
    >>> g[0] == universe_to_str(tub)
    True
    
    >>> u = get_n_generations("I am an invalid input", "Me too")
    Traceback (most recent call last):
    TypeError: list expected in position 1, int expected in position 2
    
    >>> v = []
    >>> get_n_generations(v, 4)
    Traceback (most recent call last):
    ValueError: You have not entered a valid universe. Try again.
    
    >>> blinker = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    >>> b = get_n_generations(blinker, 10)
    >>> len(b)
    2
    >>> blinker2 = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    >>> b[1] == universe_to_str(blinker2)
    True
    
    >>> beacon = [[1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1]]
    >>> b = get_n_generations(beacon, 3)
    >>> len(b)
    2
    >>> b[0] == universe_to_str(beacon)
    True
    >>> beacon2 = get_next_gen_universe(beacon)
    >>> b[1] == universe_to_str(beacon2)
    True
    """
    # checking correct type of both inputs
    if type(universe) != list or type(n) != int:
        raise TypeError("list expected in position 1, int expected in position 2")
    
    # checking validity of universe
    if not is_valid_universe(universe):
        raise ValueError("You have not entered a valid universe. Try again.")
    
    # checking number n
    if n <= 0:
        raise ValueError("n should be an integer greater than 0.")
    
    # s will store the m generations of the universe
    s = []
    m = 0
    
    # new_gen is initially equal to the universe.    
    new_gen = universe
    
    new_gen_s = universe_to_str(new_gen)
    
    # we keep on appending new generations until the cycle repeats.    
    while new_gen_s not in s:        
        # append a new generation
        s.append(new_gen_s)
        
        # reassigning new_gen to the following generation
        new_gen = get_next_gen_universe(new_gen)
        
        # transform the numbers into a string of '*' and ' '.
        new_gen_s = universe_to_str(new_gen)
        
        # m increases 1 with each loop
        m += 1
        
    p = min(m, n)
    return s[:p]

if __name__ == "__main__":
    doctest.testmod()
    
    