from math import tan , pi
zele = float(input("number zele :"))
tol = float(input("tol zele :"))
masahat = (zele * (tol ** 2)) / (4 * tan(pi / zele))
print(masahat)