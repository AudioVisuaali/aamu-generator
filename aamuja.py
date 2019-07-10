from itertools import product

A = ['A', 'À', 'Á', 'Â', 'Α', 'Ά']  # ǞÄÅǠȀĂÃĀ
a = ['a', 'à', 'á', 'â', 'ă', 'ȃ']  # åãǟǡάäȁ
m = ['m']
u = ['u', 'ù', 'ú', 'ü', 'ŭ']  # ůűûūũ
j = ['j', 'ĵ']

# total_combinations = len(a)
# for x in [A, a, m, u, j]:
#     total_combinations = total_combinations * len(x)

# print(total_combinations)

for A_, a_, m_, u_, j_, a__ in product(A, a, m, u, j, a):
    print(f"{A_}{a_}{m_}{u_}{j_}{a__} 2/19")
