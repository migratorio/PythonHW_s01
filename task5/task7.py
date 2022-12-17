# 7. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат. НЕОБЯЗАТЕЛЬНАЯ

# Составляем таблицы истинности для обоих утверждений и выводим на печать

print('x', 'y', 'z', sep='\t|\t', end=' ')
print('\t|   ¬X⋀¬Y⋀¬Z\t|', '   ¬(X⋁Y⋁Z)')
print('-'*70)

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
	        print(x, y, z, not x and not y and not z, not (x or y or z), sep='\t|\t')
