# COBERTURA DE 1L P CADA 3M
# LATAS DE TINTA TEM 18L, LOGO --> 3 * 18 = 54M PINTADOS 
# CADA LATA CUSTA R$ 80,00
# QUER Q RETORNE 2 VALORES EM UMA TUPLA, COM:
#1 - A QUANT DE LATAS DE TINTA A SEREM COMPRADAS E O OUTRO VALOR O PREÇO TOTAL DE ACORDO COM 
# OS METROS DA PAREDE


def paint_costs(area):
    can_price = 80
    required_liters = area / 3
    required_cans = required_liters // 18
    if required_liters % 18:
        required_cans += 1
    return required_cans, required_cans * can_price