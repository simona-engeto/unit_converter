#Conversion rates
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

kg_amount = 80
km_amount = 54
l_amount = 5

kg_result = kg_lb * kg_amount
km_result = km_mile * km_amount
l_result = l_gal * l_amount

print(str(kg_amount), 'kg is', str(kg_result), 'lb')
print(str(km_amount), 'km is', str(km_result), 'mil')
print(str(l_amount), 'l is', str(l_result), 'gal')