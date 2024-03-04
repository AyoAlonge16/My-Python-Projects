def get_a_lot(x):
    y0 = x + 1
    y1 = x * 3
    y2 = y0 ** y1
    return (y0, y1, y2)
 
things = get_a_lot(5)

print(things)
  
