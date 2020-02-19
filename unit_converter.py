# Conversion rates
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

# Amount of units for conversion.
kg_amount = 80
km_amount = 54
l_amount = 5

# Results
kg_result = kg_amount * kg_lb
km_result = km_amount * km_mile
l_result = l_amount * l_gal

# Final answers
print(kg_amount, 'kg is', kg_result, 'lb' )
print(km_amount, 'km is', km_result, 'mil' )
print(l_amount, 'l is', l_result, 'gal' )