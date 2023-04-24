

def clamp(x, min, max):
    if x < min:
        return min
    if x > max:
        return max
    return x


# fonction qui fait que soit un x de [min1, max1], on le transforme vers un x de [min2, max2],
# pour que x de [min1, max1] soit proportionnel à x de [min2, max2].
#
# donc si x est de [1,2] et qu'il a pour valeur 1.5, et que l'on veut le transformer vers [0, 1]
# alors cette fonction retourneras 0.5.
#
# Un autre exemple est que si x est de [0, 1] et qu'il a pour valeur 0.5, et que l'on veut le transformer
# vers [0, 255] alors cette fonction retourneras 127.5
def remap(x, min1, max1, min2, max2):
    return min2 + (x - min1) * (max2 - min2) / (max1 - min1)
