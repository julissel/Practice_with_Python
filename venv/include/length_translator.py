# The program convert length from given measure to required measure. For example type string like = '15.5 mile in km'

value_for_convert, dimention_from, tmp_var, dimention_to = input().split()
dim_base = {"m": 1, "mile": 1609, "yard": 0.9144, "km": 1000, "cm": 0.01, "mm": 0.001, "foot": 0.3048, "inch": 0.0254}

print('{:.2e}'.format(float(value_for_convert)*dim_base[dimention_from]/dim_base[dimention_to]))

