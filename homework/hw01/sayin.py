goku = 'His power level is over 1000'
greatest_warrior = True
show = 'Goku cannot be defeated'
def super_sayin(x):
    goku = 'Ultra Instinct'
    def show():
        goku = 'Normal'
        return goku
    vegeta = show()
    print(goku)
    return show()

output  = super_sayin(greatest_warrior)
print(output)
