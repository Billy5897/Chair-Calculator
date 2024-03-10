import math
#Stock with pcs per product, stock level
stock = {
    "Base": [1, 100],
    "Castor": [5, 3200],
    "Lift": [1, 72],
    "Seat": [1, 84],
    "Back": [1, 122],
    "Arms": [2, 91]
}
#Find out how many chairs are possible
min = None
mincomp = None
for component in stock:
    if min == None or min > stock[component][1]/stock[component][0]:
        min = stock[component][1]/stock[component][0]
        mincomp = component
#Share result
print(
    "You can produce", math.floor(min), "chairs.\nPurchase more",mincomp,
    "to produce more chairs.")
        
