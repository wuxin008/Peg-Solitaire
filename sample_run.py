import subprocess

command = "/usr/local/bin/python3.4 search.py input_files/sample04.txt {} {} "

#Tree Search with DFS
subprocess.call(command.format('tree-search', 'dfs'), shell=True)

#Tree Search with BFS
subprocess.call(command.format('tree-search', 'bfs'), shell=True)

#Graph Search with BFS
subprocess.call(command.format('graph-search', 'bfs'), shell=True)

#Graph Search with A* using max_movable_pegs
subprocess.call(command.format('graph-search', 'astar') + 'max_movable_pegs', shell=True)

#Graph Search with A* using max_moves
subprocess.call(command.format('graph-search', 'astar') + 'max_moves', shell=True)

#Graph Search with A* using min_moves
subprocess.call(command.format('graph-search', 'astar') + 'min_moves', shell=True)

#Tree Search with IDA* using any of the three heuristics
subprocess.call(command.format('tree-search', 'idastar') + 'min_moves', shell=True)
