placas =['ZZS198', 'EHV260', 'EHT970', 'IZN958', 'IVO562', 'EHV957', 'DTN007', 'KMM011', 'DUP465', 'DTN061', 'HCQ938', 'HVY388', 'GJT363', 'IHN533', 'IIQ351', 'HMO909', 'CWO647', 'IGK512', 'HMK482', 'WJH30C', 'XRH90F', 'XTC11F', 'KUZ285', 'IVO013', 'BLB727', 'HMP860', 'GSS710', 'GEP066', 'GSY121']
carros = []
motos = []
for placa in placas:
    if placa[5].isnumeric() == True:
        carros.append(placa)
    else:
        motos.append(placa)


print(f"Carros: {carros}")

print(f"Motos: {motos}")
