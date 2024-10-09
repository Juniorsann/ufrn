# Dados fornecidos
x_s = 0.20        # Fração molar de S
x_r = 0.25        # Fração molar de R
x_inerte = 0.15   # Fração molar de inerte
x_a = 0.40        # Fração molar de A

D_as = 0.22       # Coeficiente de difusão de A em S (cm²/s)
D_ar = 0.17       # Coeficiente de difusão de A em R (cm²/s)
D_ai = 0.36       # Coeficiente de difusão de A em inerte (cm²/s)

# Fluxos molares hipotéticos para o componente A e os outros componentes
N_a = 1.0  # Fluxo molar de A
N_r = 1.0  # Fluxo molar de R
N_s = 3.0  # Fluxo molar de S
N_inerte = 1.0  # Fluxo molar de inerte

# Numerador
numerador = N_a - x_a * (N_a + N_r + N_s + N_inerte)

# Denominador
denominador = (
    (1 / D_ar) * (N_a * x_r - N_r * x_a) +
    (1 / D_as) * (N_a * x_s - N_s * x_a) +
    (1 / D_ai) * (N_a * x_inerte - N_inerte * x_a)
)

# Cálculo do coeficiente de difusão efetivo
D_ae = numerador / denominador

# Exibe o resultado
print(f"O coeficiente de difusão efetivo D_i,m é: {D_ae:.3f} cm²/s")
