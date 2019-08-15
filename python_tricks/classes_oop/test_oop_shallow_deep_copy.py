## deep and shallow copy, use `copy` module
import copy

# shallow copy: only copy the 1st level class or 2nd level of primary type objects
# thus shallow-copy doesn't create an independent copy

class PCPoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'PC Point( {self.x!r}, {self.y!r}, {self.z!r})'

class Rectangle:
    def __init__(self, left_boundary, right_boundary):
        self.leftb = left_boundary
        self.rightb = right_boundary
    
    def __repr__(self):
        return (f'Rectangle({self.leftb!r}, '
                f'{self.rightb!r})' )
        

if __name__ == "__main__":
    a_simple = [[1, 2, 3], [4, 5, 6], [-1, -2, -3]]
    b_simple = a_simple
    print("a_simple: ", a_simple)
    print("b_simple: ", b_simple)

    # shallow copy by default:
    a_simple.append(['bull session'])
    print("a_simple: ", a_simple)
    print("b_simple: ", b_simple)
    print('-' * 40)
    
    # c_simple is a shallow copy of a. NOTE the differences
    # shallow-copy 'inheritate' original class contents, shallow means point-to the original contents
    # not including newly added objects
    c_simple = list(a_simple)
    print("a_simple: ", a_simple)
    print("c_simple: ", c_simple)
    c_simple.append(['under a chever'])
    print("a_simple: ", a_simple)
    print("c_simple: ", c_simple)
    c_simple[1][2] = -818
    print("a_simple: ", a_simple)
    print("c_simple: ", c_simple)
    print('-' * 40)

    a = PCPoint(23, 43,  56)
    b = copy.copy(a)
    print("PCPoint a: ", a)
    print("PCPoint b: ", b)
    print('-' * 40)

    rect = Rectangle(PCPoint(-1, -2, -3), PCPoint(3, 2, 1))
    shallow_rect = copy.copy(rect)
    deep_rect = copy.deepcopy(rect)
    print(rect)
    print(shallow_rect)
    print(rect is shallow_rect)
    shallow_rect.leftb.x = 8849
    print(rect)
    print(shallow_rect)
    print(deep_rect)

    # __copy__, __deepcopy__







