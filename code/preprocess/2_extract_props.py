import json
import csv
import os
from tqdm import tqdm
import pandas as pd

# define tasks
nlp_tasks = {
    "text-classification", "token-classification", "table-question-answering", "question-answering",
    "zero-shot-classification", "translation", "summarization", "feature-extraction",
    "text-generation", "text2text-generation", "fill-mask", "sentence-similarity"
}

cv_tasks = {
    "depth-estimation", "image-classification", "object-detection", "image-segmentation", "text-to-image",
    "image-to-text", "image-to-image", "image-to-video", "unconditional-image-generation", "video-classification",
    "text-to-video", "zero-shot-image-classification", "mask-generation", "zero-shot-object-detection",
    "text-to-3d", "image-to-3d", "image-feature-extraction", "keypoint-detection"
}

multimodal_tasks = {
    "audio-text-to-text", "image-text-to-text", "visual-question-answering", "document-question-answering",
    "video-text-to-text", "visual-document-retrieval", "any-to-any"
}

audio_tasks = {
    "text-to-speech", "text-to-audio", "automatic-speech-recognition", "audio-to-audio",
    "audio-classification", "voice-activity-detection"
}

tabular_tasks = {
    "tabular-classification", "tabular-regression", "time-series-forecasting"
}

rein_tasks = {
    "reinforcement-learning", "robotics"
}

other_tasks = {
    "graph-machine-learning"
}

def classify_model(task):
    if pd.isna(task) or not task:
        return "Unknown"
    task = task.strip()
    if task in nlp_tasks:
        return "NLP"
    elif task in cv_tasks:
        return "CV"
    elif task in multimodal_tasks:
        return "Multimodal"
    elif task in audio_tasks:
        return "Audio"
    elif task in tabular_tasks:
        return "Tabular"
    elif task in rein_tasks:
        return "Reinforcement Learning"
    elif task in other_tasks:
        return "Other"
    else:
        return "Unknown"

batch_numbers = range(0, 19)
output = []

for batch_number in tqdm(batch_numbers, desc="Processing batches"):
    file_name = f'../../data/models_0625/models_batch_{batch_number}.json'
    if not os.path.exists(file_name):
        print(f"File {file_name} is not existed.")
        continue

    with open(file_name, 'r') as f:
        data = json.load(f)

    for item in data:
        model_id = item.get('id', "N/A")
        downloads = item.get('downloads', "N/A")
        pipeline_tag = item.get('pipeline_tag', "N/A")
        library_name = item.get('library_name', "N/A")
        tags = item.get('tags', [])
        license = next((tag.split("license:")[1] for tag in tags if tag.startswith("license:")), "N/A")
        dataset_tags = [tag for tag in tags if 'dataset:' in tag]

        datasets = set()  
        if dataset_tags:
            for tag in dataset_tags:
                dataset_value = tag.split(':', 1)[1]  
                datasets.add(dataset_value)
        datasets_str = ', '.join(datasets) if datasets else 'N/A'

        category = classify_model(pipeline_tag)        
        output.append([model_id, pipeline_tag, library_name, license, downloads, category, datasets_str])

# save
output_path = '../../data/model_props_0625.csv'
with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Model ID', 'Task', 'Library', 'License', 'Download', 'Model Category', 'Datasets'])
    writer.writerows(output)