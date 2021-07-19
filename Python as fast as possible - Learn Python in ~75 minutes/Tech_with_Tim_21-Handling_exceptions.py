# PYTHON COURSE 21
# Carlos Terreros Sanchez
# Tech with Tim


# Handling exceptions
try:
    x = 7 / 0

except Exception as e:
    print(e)

finally:                                                                       # Ocurrira si o si, aunque encuentre una exception
    print('finally')
    
