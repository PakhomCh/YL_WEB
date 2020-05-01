proc = {3:"Intel Core I3",
        5:"Intel Core I5",
        7:"Intel Core I7",
        10:"AMD Ryzen 5",
        14:"AMD Ryzen 7",
        18:"AMD Ryzen 9"}

plate = {3:"GIGABYTE H310M A 2.0",
         5:"GIGABYTE B450M GAMING",
         7:"MSI X570-A PRO",
         9:"MSI MPG X570 Gaming Plus"}

vid = {3:"GeForce GTX 1650",
        5:"GeForce GTX 1660 Ti",
        7:"GeForce RTX 2060",
        9:"GeForce RTX 2080"}



def generate (val1, val2, val3):

    vals = [val1, val2, val3]

    result = ['', '', '']

    req = [0, 0, 0]

    f = [0, 0, 0]

    code = 0

    if (val1 != 0):

        f[0] = 1

        result[0] = proc[val1]

        if (val1 % 2 == 0):

            val1 /= 2

        req [1] = val1

    if (val2 != 0):

        f[1] = 1

        result[1] = plate[val2]

        req[0] = val2
        req[2] = val2

    if (val3 != 0):

        f[2] = 1

        result[2] = vid[val3]

        req[1] = val3

        if f[0]:

            if req[1] != val3:

                return ("Невозможно подобрать", "Невозможно подобрать", "Невозможно подобрать")





    for i in range (3):

        if vals[i] != 0 and req[i] != 0:

            if (vals[i] % req[i] != 0):

                return ("Невозможно подобрать", "Невозможно подобрать", "Невозможно подобрать")

    if req == [0, 0, 0]:

        return ("Невозможно подобрать", "Невозможно подобрать", "Невозможно подобрать")

    set = 100

    for i in req:

        if i < set and i != 0:

            set = i

    print(set, "+")

    pset = set

    if set == 9:

        pset = 18



    return (proc[pset], plate[set], vid[set])

def ident(id):

    if id == '-1':

        return 'LOGIN'
