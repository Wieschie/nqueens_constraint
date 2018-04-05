python -m cProfile -o nqueens.profile nqueens_constraint.py && pyprof2calltree -i nqueens.profile -o nqueens.calltree
