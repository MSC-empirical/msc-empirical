import json
import csv
import os
from tqdm import tqdm 


batch_numbers = range(0, 19)  
output = []

for batch_number in tqdm(batch_numbers, desc="Processing batches"):
    file_name = f'../../data/models_0702/models_batch_{batch_number}.json'
    if not os.path.exists(file_name):
        print(f"File {file_name} is not existed.")
        continue

   
    with open(file_name, 'r') as f:
        data = json.load(f)

    for item in data:
        model_id = item.get('id')  
        tags = item.get('tags', [])  
       
        base_model_tags = [tag for tag in tags if tag.startswith('base_model:') and ':' in tag.split(':', 1)[1]]  

        prefix = 'N/A'
        base_models = set() 

        if base_model_tags:
            for tag in base_model_tags:
                base_model_value = tag.split(':', 1)[1] 
                prefix, model_name = base_model_value.split(':', 1)  
                base_models.add(model_name)

        
        output.append([model_id, prefix, ', '.join(base_models) if base_models else 'N/A'])


print(len(output))
with open('../../data/model_relation_0702.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Model ID', 'Type', 'Base Model'])
    writer.writerows(output)