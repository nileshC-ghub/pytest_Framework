import functools
import operator

def factorial_num(n):
    try:
        if type(n)!=int:
            raise ValueError
        else:
            if n==0:
                print "1"
            else:
                lis=range(n,0,-1)
                print functools.reduce(operator.mul,lis)

    except ValueError:
        print "Invalid Input"



def even_pos_upcase(w):
    str_list=list(w)
    str_dict={(i+1) : str_list[i] for i in range(0, len(str_list) )}
    map_op=map(lambda key: str_dict[key].upper() if key%2==0 and type(str_dict[key])!=int else str_dict[key], str_dict.keys())
    print "".join(map_op)

