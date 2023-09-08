from heuristicas import Heuristicas

def solvable(tiles):
    """
    Check whether a 3x3 sliding puzzle is solvable.

    Checks the number of "inversions". If this is odd then the puzzle configuration is not solvable.

    An inversion is when two tiles are in the wrong order.

    For example, the sequence 1, 3, 4, 7, 0, 2, 5, 8, 6 has six inversions:

    3 > 2
    4 > 2
    7 > 2
    7 > 5
    7 > 6
    8 > 6

    The empty tile is ignored.
    """
    count = 0

    for i in range(8):
        for j in range(i+1, 9):
            if tiles[j] and tiles[i] and tiles[i] > tiles[j]:
                count += 1

    return count % 2 == 0


# matriz = [[1, 8, 2],
#           ["X", 4, 3],
#           [7, 6, 5]]
matriz = [[2, 1, 8],
          [6, 4, 5],
          ["X", 3, 7]]

# matriz = [["X", 2, 4],
#           [8, 5, 3],
#           [1, 7, 6]]

#           [1, 2, 3]
#           [4, 5, 6]
#           [7, 8, 0]

heuristicas = Heuristicas()
conflitos = heuristicas.calcular_conflitos_lineares(matriz) / 2
print(conflitos)
