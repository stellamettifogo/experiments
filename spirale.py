


def spira_ammira_v2(numbers):
  
  x_min = 0
  x_max = len(numbers[0]) # il loop va fino a x_max - 1
  width = x_max
  y_min = 0 # y_min é sopra!
  y_max = len(numbers) # y_max é sotto!
  
  # how many segments do we need?
  number_of_segments = x_max + y_max 

  result = []
  
  
  # scan each of the segments, we will change direction
  # after each segment and print the numbers we see
  for line in range(0, number_of_segments):
    y = y_min
    
    # going right
    for x in range(x_min, x_max):
      # il primo [y_max][] é il numero di array (quindi la y)
      # il secondo [][x] é la position nell'array (quindi la x)
      #n = numbers[y_min][x]
      n = y * width + x +1
      result.append(n)
      print(f"right: {n}")
    # non faremo piu la riga piu in alto...
    y_min = y_min +1

    # si va "down"
    for y in range(y_min, y_max):
      #n = numbers[y][x_max-1]
      n = y * width + x +1
      result.append(n)
      print(f"down: {n}")
    # non faremo piu la colonna piu a destra...
    x_max = x_max - 1
    y = y_max - 1
    
    # going left
    for x in range(x_max -1, x_min -1, -1):
      # il primo [y_max][] é il numero di array (quindi la y)
      # il secondo [][x] é la position nell'array (quindi la x)
      #n = numbers[y_max][x]
      n = y * width + x +1
      result.append(n)
      print(f"left: {n}")
    # TIP range(20, 10, -1) nota il terzo parametro -1, va da 20 a 10 andando indietro
    y_max = y_max -1
    x = x_min
    
    # going up
    print()
    #1 range(y_max -1, y..., -1)
    for y in range(y_max -1, y_min -1, -1):
      # il primo [y_max][] é il numero di array (quindi la y)
      # il secondo [][x] é la position nell'array (quindi la x)
      #n = numbers[y][x_min - 1]
      n = y * width + x +1
      result.append(n)
      print(f"up: {n}")
    # TIP range(20, 10, -1) va indietro -1 alla volta...
    x_min = x_min +1
    
    
    
  return result



# testing

data1 = [
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
]

result1 = [1, 2, 3, 4, 8, 12, 16, 20, 19, 18, 17, 13, 9, 5, 6, 7, 11, 15, 14, 10]

r1 = spira_ammira_v2(data1)
assert r1 == result1
print(r1 == result1)