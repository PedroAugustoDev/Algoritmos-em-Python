# Import do modulo da area do circulo
# Essencial para calcular a área da base
import area as a

# Cálculo da area do clindo
def volume(area, altura):
    return area * altura


h = 10
r = 5
print(f'O volume do cilindro de altura {h}cm  raio {r}cm é de \u2243 {round(volume(a.calc_area(5), h),0)}cm\u00B3')