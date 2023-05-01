def read_polys(fname: str):
    '''The input file contains two polynomials
    3x^14 + 2x^8 + 1x^0
    8x^14 - 3x^10 + 10x^6'''
    with open(fname, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    
    polys = [(line) for line in lines]
    return polys

if __name__ == '__main__':
    fname_input = 'polys.txt'
    fname_output = 'polys_result.txt'
    polys = read_polys(fname_input)
    poly_left, poly_right = polys
    print(poly_left)
    print(poly_right)
    poly_added = poly_left + poly_right
    print(poly_added)
    poly_multiplied = poly_left
    print(poly_multiplied)

    with open(fname_output, 'w') as f:
        f.writelines([poly_added, poly_multiplied])