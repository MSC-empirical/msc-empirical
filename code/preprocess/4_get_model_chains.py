import json
from tqdm import tqdm

models_chain_file = "../../data/modelsChain_by_base_0625.json"
root_models_file = "../../data/root_models_0625.json"
output_tree_stats_file = "../../data/model_depth_0625.txt"
output_chain_lengths_file = "../../data/model_chain_length_0625.txt"
output_all_chains_file = "../../data/model_chains/model_chains_0625.txt"  

with open(models_chain_file, "r", encoding="utf-8") as file:
    models_chain = json.load(file)

with open(root_models_file, "r", encoding="utf-8") as file:
    root_models = json.load(file)

def build_tree_stats(root_models, models_chain):
    stats = []
    chain_lengths = []
    all_chains = [] 

    for root_model in tqdm(root_models, desc="Processing Root Models"):
        queue = [{"name": root_model, "depth": 0, "path": [root_model]}]
        max_depth = 1
        longest_paths = []
        layer_counts = {}
        visited = set()
        total_paths = 0

        with tqdm(total=len(queue), desc=f"Building Stats for {root_model}") as pbar:
            while queue:
                current_node = queue.pop(0)
                model_name = current_node["name"]
                depth = current_node["depth"]
                path = current_node["path"]

                layer_counts[depth] = layer_counts.get(depth, 0) + 1

                if depth == max_depth:
                    longest_paths.append(path)
                elif depth > max_depth:
                    max_depth = depth
                    longest_paths = [path]

                visited.add(model_name)
                pbar.update(1)

                is_leaf = model_name not in models_chain or all(
                    not models_chain[model_name].get(t, []) for t in ["finetune", "adapter", "merge", "quantized"]
                )

                if is_leaf:
                    total_paths += 1
                    chain_lengths.append(len(path))
                    all_chains.append(path)

                if model_name in models_chain:
                    for t in ["finetune", "adapter", "merge", "quantized"]:
                        for child in models_chain[model_name].get(t, []):
                            if child not in visited:
                                queue.append({
                                    "name": child,
                                    "depth": depth + 1,
                                    "path": path + [child]
                                })
                    pbar.total = pbar.n + len(queue)

        stats.append({
            "root_model": root_model,
            "max_depth": max_depth,
            "longest_paths": longest_paths,
            "layer_counts": layer_counts,
            "total_paths": total_paths
        })

    return stats, chain_lengths, all_chains

tree_stats, chain_lengths, all_chains = build_tree_stats(root_models, models_chain)

sorted_tree_stats = sorted(tree_stats, key=lambda x: x["max_depth"], reverse=True)
with open(output_tree_stats_file, "w", encoding="utf-8") as file:
    for stat in sorted_tree_stats:
        file.write(f"Root Model: {stat['root_model']}\n")
        file.write(f"Max Depth: {stat['max_depth']}\n")
        file.write(f"Total Chains from Root: {stat['total_paths']}\n")
        file.write("Longest Paths:\n")
        for path in stat["longest_paths"]:
            file.write("  " + " -> ".join(path) + "\n")
        file.write("Layer Counts:\n")
        for depth, count in sorted(stat["layer_counts"].items()):
            file.write(f"  Depth {depth}: {count} nodes\n")
        file.write("\n")

with open(output_chain_lengths_file, "w", encoding="utf-8") as f:
    for length in chain_lengths:
        f.write(f"{length}\n")

with open(output_all_chains_file, "w", encoding="utf-8") as f:
    for chain in all_chains:
        f.write(" -> ".join(chain) + "\n")