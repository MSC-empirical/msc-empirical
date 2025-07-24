import csv
import json

input_csv_file = "../../data/model_relation/batch_all_0625.csv"
output_json_file = "../../data/modelsChain_by_base_0625.json"
root_models_file = "../../data/root_models_0625.json"

model_data = {}
with open(input_csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        model_id = row["Model ID"]
        model_type = row["Type"] if row["Type"] != "N/A" else None
        base_model = row["Base Model"] if row["Base Model"] != "N/A" else None
        model_data[model_id] = {"type": model_type, "base_model": base_model}

organized_data = {}
for model_id, attributes in model_data.items():
    base_model = attributes["base_model"]
    model_type = attributes["type"]

    if model_type == "merge" and base_model: 
        merged_models = [m.strip() for m in base_model.split(",")] 
        for merged_model in merged_models:
            if merged_model not in organized_data:
                organized_data[merged_model] = {
                    "base_model": merged_model,
                    "finetune": [],
                    "adapter": [],
                    "merge": [],
                    "quantized":[]
                }
           
            organized_data[merged_model]["merge"].append(model_id)

        if model_id not in organized_data:
            organized_data[model_id] = {
                "base_model": model_id,
                "finetune": [],
                "adapter": [],
                "merge": [],
                "quantized":[]

            }

    elif base_model: 
        if base_model not in organized_data:
            organized_data[base_model] = {
                "base_model": base_model,
                "finetune": [],
                "adapter": [],
                "merge": [],
                "quantized":[]
            }
        
        if model_type == "finetune":
            organized_data[base_model]["finetune"].append(model_id)
        elif model_type == "adapter":
            organized_data[base_model]["adapter"].append(model_id)
        elif model_type == "quantized":
            organized_data[base_model]["quantized"].append(model_id)

filtered_data = {
    key: value
    for key, value in organized_data.items()
    if value["finetune"] or value["adapter"] or value["merge"] or value["quantized"]
}

keys_to_delete = []

for key, value in filtered_data.items():
    base_model = value.get("base_model", "")
    if not base_model:
        continue
    for field in ["finetune", "adapter", "merge", "quantized"]:
        if field in value:
            duplicates = [item for item in value[field] if item == base_model]
            if duplicates:
                keys_to_delete.append(key)
                break 

for key in keys_to_delete:
    del filtered_data[key]


root_models = []
for base_model in filtered_data.keys():
    if base_model in model_data and model_data[base_model]["base_model"] is None:
        root_models.append(base_model)


with open(root_models_file, mode="w", encoding="utf-8") as file:
    json.dump(root_models, file, indent=4, ensure_ascii=False)

with open(output_json_file, mode="w", encoding="utf-8") as file:
    json.dump(filtered_data, file, indent=4, ensure_ascii=False)
