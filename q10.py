# Dados fornecidos no exercício para o item 10
x_s = 0.20        # Fração molar de S
x_r = 0.25        # Fração molar de R
x_inerte = 0.15   # Fração molar de inerte

D_as = 0.22       # Coeficiente de difusão de A em S (cm²/s)
D_ar = 0.17       # Coeficiente de difusão de A em R (cm²/s)
D_ai = 0.36       # Coeficiente de difusão de A em inerte (cm²/s)

# Cálculo do coeficiente de difusão efetivo (D_Ae) para o item 10
D_ae_inv_10 = (x_s / D_as) + (x_r / D_ar) + (x_inerte / D_ai)
D_ae_10 = 1 / D_ae_inv_10

# Exibe o resultado do item 10
print(f"Coeficiente de difusão efetivo de A para o item 10 (D_Ae) é: {D_ae_10:.3f} cm²/s")


# Novas frações molares para o item 11
x_s_new = 3 / 6  # 3 moles de S
x_r_new = 1 / 6  # 1 mole de R
x_inerte_new = 1 / 6  # 1 mole de Inerte

# Cálculo do coeficiente de difusão efetivo (D_Ae) para o item 11
D_ae_inv_11 = (x_s_new / D_as) + (x_r_new / D_ar) + (x_inerte_new / D_ai)
D_ae_11 = 1 / D_ae_inv_11

# Exibe o resultado do item 11
print(f"Coeficiente de difusão efetivo de A para o item 11 (D_Ae) é: {D_ae_11:.3f} cm²/s")
