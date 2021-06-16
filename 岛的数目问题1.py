from typing import List
def count_islands(mat: List[List[int]]) -> int:
    d1 = {}
    d2 = {}
    if not mat:
      return 0
    rows = len(mat)
    cols = len(mat[0])
    index = 1
    for i in range(rows):
      for j in  range(cols):
        if mat[i][j] == 1:
          if i-1>=0 and mat[i-1][j] == 1 and mat[i][j-1] != 1:
            d1[(i,j)] = d1[(i-1,j)]
            d2[ d1[(i-1,j)] ].append( (i,j) )
          elif j-1 >=0 and mat[i][j-1] == 1 and mat[i-1][j] != 1:
            d1[(i,j)] = d1[(i,j-1)]
            d2[ d1[(i,j-1)] ].append( (i,j) )
          elif i-1>=0 and j-1 >=0 and mat[i-1][j] == 1 and mat[i][j-1] == 1:
            if  d1[(i,j-1)]  ==  d1[(i-1,j)] :
              d1[(i,j)] = d1[(i-1,j)]
              d2[ d1[(i-1,j)] ].append( (i,j) )
            else:
              for position in d2 [ d1[(i,j-1)] ]:
                d1[position] = d1[(i-1,j)] 
              d2[ d1[(i-1,j)]  ] += d2[ d1[(i,j-1)]  ]
              del d2[ d1[(i,j-1)]  ]
          else:
            d1[(i,j)] = 'set'+ str(index)
            d2['set'+ str(index)] = [(i,j)]
            index += 1
    print(d1)
    print(d2)
    return len(list(d2.keys()))
            
print( count_islands([
  [0,0,1,1,0,1],
  [0,0,1,1,1,0],
  [1,1,0,0,0,0],
]) )

              
          
        