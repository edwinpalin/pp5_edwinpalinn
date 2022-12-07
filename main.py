"""
Edwin Palin
22-0178
Refinando código
En este ejercicio, se refinará un código dado y se publicará en un repositorio de Github
"""


def costs():
  with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')
  gift_costs = [int(c) for c in gift_costs]  # convierte strings a int
  return gift_costs


def total(gift_costs):
  gift_costs = costs()
  total_price = 0
  for cost in gift_costs:
    if cost > 1000:
      total_price += cost * 1.16  # agrega impuestos
    else:
      total_price += cost  # los costos menores a 1000 no se le agrega impuesto

  return total_price


def main():
  print(total(costs()))
  # llama a las dos funciones y luego imprime el resultado


main()
