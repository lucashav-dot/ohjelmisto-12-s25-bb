import math

säde_str = input("Anna ympyrän säde: ")
säde = float(säde_str)
pinta_ala = (math.pi*säde**2)
pyoristys = round(pinta_ala, 2)
print("ympyrän pinta-ala: " + str(pyoristys))