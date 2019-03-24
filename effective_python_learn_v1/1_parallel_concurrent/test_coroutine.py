##
import os, sys
import collections 
from collections import namedtuple

# do the test while reading the book 'effective python 59 specific ways to write better python'
# the author also supply the sample code on site:   https://github.com/bslatkin/effectivepython.git'


def my_coroutine():
    while True:
        recieve = yield
        print('received: ', recieve)

def minimize_coroute():
    # taken as the 1st input & minimize value
    minimize = yield
    while True:
        input_value = yield minimize
        minimize = min(input_value, minimize)
    # although U wanna return a value, the type is still 'generator'
    #return minimize

def count_neighbours(y, x):
    North = yield Query(y+1, x+0)
    West  = yield Query(y+0, x-1)
    East  = yield Query(y+0, x+1)
    South = yield Query(y-1, x+0)
    NorthWest = yield Query(y+1, x-1)
    NorthEast = yield Query(y+1, x+1)
    SouthWest = yield Query(y-1, x-1)
    SouthEast = yield Query(y-1, x+1)
    neighbourStates = [North, West, East, South, NorthWest, NorthEast, SouthWest, SouthEast]

    count = 0
    for state in neighbourStates:
        if state == ALIVE:
            count += 1
    return count
    
def step_cell(y, x):
    state = yield Query(y, x)
    neighbours = yield from count_neighbours(y, x)
    next_state = game_logic(state, neighbours)
    yield Transition(y, x, next_state)

def game_logic(state, neighbours):
    if state == ALIVE:
        if neighbours < 2:
            return DEAD
        elif neighbours > 3:
            return DEAD
        # == 2,3, keep alive
    elif state == DEAD:
        if neighbours == 3:
            return ALIVE
    return state

def simulate(height, width):
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y, x)
        yield TICK

class Grid(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([DEAD] * self.width)
   
    def __str__(self):
        # TODO
        output = ''
        for row in self.rows:
            for cell in row:
                output += cell
            output += '\n'
        return output
        
    
    def query(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def assign(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

class ColumnPrinter(object):
    def __init__(self):
        self.columns = []
  
    def append(self, data):
        self.columns.append(data)

    def __str__(self):
        row_count = 1
        for data in self.columns:
            row_count = max(row_count, len(data.splitlines()) + 1)
        rows = [''] * row_count
        for j in range(row_count):
            for i, data in enumerate(self.columns):
                line = data.splitlines()[max(0, j - 1)]
                if j == 0:
                    padding = ' ' * (len(line) // 2)
                    rows[j] += padding + str(i) + padding
                else:
                    rows[j] += line
                if (i + 1) < len(self.columns):
                    rows[j] += ' | '
        return '\n'.join(rows)

def live_a_generation(grid, sim):
    progeny = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.y, item.x)
            item = sim.send(state)
        else:
            progeny.assign(item.y, item.x, item.state)
            item = next(sim)
    return progeny

if __name__ == '__main__':
    # iterators: store all the values in memory; not memory-efficient
    #list_a = [1, 2, 3, 6]
    #for i in list_a:
    #    print(i)
    
    list_b = [x * x for x in range(3)]
    for i in list_b:
        print(i)

    # generators: NOTE the difference between tuple and generator !!
    # a = ('cc', 23) --> tuple;  b = (x * x for x in range(10)) -> generator
    # Generators are iterators, a kind of iterable you can only iterate over once. 
    # Generators do not store all the values in memory, they generate the values on the fly:
    
    it = my_coroutine()
    print('type: ', type(it))
    # mvoe forward to next yield
    next(it)
    it.send('1st')
    it.send('2nd')

    mini_it = minimize_coroute()
    print('type: ', type(mini_it))
    next(mini_it)
    print(mini_it.send(10))
    print(mini_it.send(30))
    print(mini_it.send(5))
    print(mini_it.send(1))

    # more test on coroutine:
    # order: [North, West, East, South, NorthWest, NorthEast, SouthWest, SouthEast]
    ALIVE = 'A'
    DEAD = '-'
    Query = namedtuple('Query', ('x', 'y'))
    Transition = namedtuple('Transition', ('y', 'x', 'state'))
    TICK = object()
    
    start_y = 5 
    start_x = 5

    print('\ntest count neighbours -----')
    count_it = count_neighbours(start_y, start_x)
    q_n = next(count_it)
    print('north: ', q_n)
    q_w = count_it.send(ALIVE)
    print('west: ', q_w)
    q_e = count_it.send(DEAD)
    print('east: ', q_e)
    q_s = count_it.send(ALIVE)
    print('south: ', q_s)
    q_nw = count_it.send(DEAD)
    print('northwest: ', q_nw)
    q_ne = count_it.send(DEAD)
    print('northeast: ', q_ne)
    q_sw = count_it.send(ALIVE)
    print('southwest: ', q_sw)
    q_se = count_it.send(DEAD)
    print('southeast: ', q_se)
    
    try:
        count = count_it.send(DEAD) # 9th send, to trigger the exception
    except StopIteration as e:
        print('NeightBour Count: ', e.value)
     
    print('\ntest step_cell -----')
    step_it = step_cell(start_y, start_x)
    now = next(step_it)
    print('now: ', now)
    q_n = step_it.send(DEAD)
    print('north: ', q_n)
    q_w = step_it.send(ALIVE)
    print('west: ', q_w)
    q_e = step_it.send(ALIVE)
    print('east: ', q_e)
    q_s = step_it.send(ALIVE)
    print('south: ', q_s)
    q_nw = step_it.send(DEAD)
    print('northwest: ', q_nw)
    q_ne = step_it.send(DEAD)
    print('northeast: ', q_ne)
    q_sw = step_it.send(ALIVE)
    print('southwest: ', q_sw)
    q_se = step_it.send(DEAD)
    print('southeast: ', q_se)
    out_state = step_it.send(DEAD)
    print('output: ', out_state)

    print('\ntest grid construction -----')
    grid = Grid(5, 9)
    grid.assign(0, 3, ALIVE)
    grid.assign(1, 4, ALIVE)
    grid.assign(2, 2, ALIVE)
    grid.assign(2, 3, ALIVE)
    grid.assign(2, 4, ALIVE)
    print(grid)

    print('\ntest column printer -----')
    columns = ColumnPrinter()
    sim = simulate(grid.height, grid.width)
    for i in range(5):
        columns.append(str(grid))
        #columns.append(grid)
        grid = live_a_generation(grid, sim)
    print(columns)


