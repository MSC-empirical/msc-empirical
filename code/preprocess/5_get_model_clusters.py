import json
import csv
from collections import defaultdict, deque


input_file = '../../data/modelsChain_by_base_0625.json'  

with open(input_file, 'r') as f:
    data = json.load(f)

results = {}
forward_graph = defaultdict(set)
reverse_graph = defaultdict(set)

for base_model, model_data in data.items():
    for dep_type in ["finetune", "adapter", "merge", "quantized"]:
        for derived_model in model_data.get(dep_type, []):
            forward_graph[base_model].add(derived_model)
            reverse_graph[derived_model].add(base_model)

def bfs_reachable(start_node, graph):
    visited = set()
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

all_models = set(data.keys()) | set(m for v in forward_graph.values() for m in v)

impact_downstream = {}
for model in all_models:
    reachable = bfs_reachable(model, forward_graph)
    impact_downstream[model] = len(reachable)


downstream_file = '../../data/model_cluster_size_0625.csv'
with open(downstream_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Model Name", "DIS"])
    for model, degree in sorted(impact_downstream.items(), key=lambda x: x[1], reverse=True):
        writer.writerow([model, degree])
print(f"The data of model cluster size is saved to {downstream_file}")
