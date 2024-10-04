import queue

def dfs(search_node, start_node, graph):
  visited_nodes = set()
  queued_connected_nodes_of = set()
  q = queue.Queue()
  q.put(start_node)
  while q.qsize():
      node = q.get()
      if search_node == node:
          return True
      visited_nodes.add(node)
      if node in queued_connected_nodes_of:
          continue
      queued_connected_nodes_of.add(node)
      for connected_node in graph[node]:
          if connected_node not in visited_nodes:
              q.put(connected_node)
  return False

# Testing
search_node = "Z"
start_node = "A"
graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E', 'F'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'A', 'C', 'E', 'Z'},
         'Z':{'F'}}
result = dfs(search_node, start_node, graph)
print(result)
