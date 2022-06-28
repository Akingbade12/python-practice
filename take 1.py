class xyz:
    def avexp(self,dep1exp,dep2exp,dep3exp):
        average = (dep1exp+dep2exp+dep3exp)/3
        print("The average expenditure of the department is ",average)

    babcocklamb = lambda dep1exp,dep2exp,dep3exp: (dep1exp+dep2exp+dep3exp)/3
    print("The average expenditure is ",babcocklamb(2222,22222,22222))

obj = xyz()
obj.avexp(50000,99282,2293)



class Divlist:

    Lagos = [11,22,33,44,55,66,77,88,99]

    div = lambda x: x/10

    z = list(map(div, Lagos))
    print("output", z)



class numdiv:

    Abuja = [61,62,63,64,65,66,67,68,69]

    div2 = lambda y: (y%3 == 0)

    z1 = list(map(div2, Abuja))
    print("output 2", z1)



class repeated:
    import functools
    add = [5,6,7,8,9,10,11,12,13,14]

    div3 = lambda x,y: x+y

    z2 = functools.reduce(div3, add)

    print("output 3", z2)