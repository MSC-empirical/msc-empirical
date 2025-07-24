import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
fm.fontManager.addfont('../../Font/times.ttf')
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 32
# 1 Qwen2.5-7B-Matrix
# 2 model-3
# 3 Qwen2.5-7B-Gordion-v0.1-Reason
# 4 Qwen2.5-3B-Model-Stock-v3.1
# 5 Qwen2.5-3B-RP-Thinker-V2
# 6 Reyna-Mini-1.8B-v0.2-Qwen1.5-1.8B-Merged-Slerp
# 7 Beyonder-4x7B-v3
# 8 Qwen2.5-7B-Qandora-CySec
groups = ['#1', '#2', '#3', '#4', '#5' ,'#6','#7','#8']
categories = ['HR', 'JSR', 'PSR']
num_points_per_category = 10

group_positions = np.arange(len(groups))
width = 0.2 

colors = ['red', 'green', 'blue']
data = {
    '#1': {
        'HR': [44.90, 13.10],
        'JSR': [73.65, 73.08],
        'PSR': [43.44, 37.01]
    },
    '#2': {
        'HR': [44.90, 2.90],
        'JSR': [73.65, 48.08],
        'PSR': [43.44, 61.35]
    },
    '#3': {
        'HR': [44.90, 6.30],
        'JSR': [73.65, 49.23],
        'PSR': [43.44, 53.94]
    },
    '#4': {
        'HR': [2.98, 4.47],
        'JSR': [54.81, 14.42],
        'PSR': [56.71, 59.84]
    },
    '#5': {
        'HR': [4.34, 2.98, 3.09],
        'JSR': [80.58, 54.81, 55.77],
        'PSR': [33.61, 56.71, 55.86]
    },
    '#6': {
        'HR': [62.47, 9.49],
        'JSR': [80.19, 78.27],
        'PSR': [23.91, 23.33]
    },
    '#7': {
        'HR': [1.85, 4.15, 3.41],
        'JSR': [79.62, 68.08, 78.65],
        'PSR': [37.80, 58.46, 47.49]
    },
    '#8': {
        'HR': [7.12, 3.96],
        'JSR': [80.38, 81.15],
        'PSR': [39.93, 46.10]
    }
}
for group in data:
    for category in data[group]:
        data[group][category] = [x / 100 for x in data[group][category]]
special_points = {
    '#1': {'HR': 10.36, 'JSR': 76.73, 'PSR': 44.88},
    '#2': {'HR': 46.15, 'JSR': 46.15, 'PSR': 50.08},
    '#3': {'HR': 6.64, 'JSR': 83.46, 'PSR': 47.12},
    '#4': {'HR': 3.09,  'JSR': 55.77, 'PSR': 55.86},
    '#5': {'HR': 2.92,  'JSR': 56.92, 'PSR': 56.01},
    '#6': {'HR': 20.50,  'JSR': 84.81, 'PSR': 15.12},
    '#7': {'HR': 3.39,  'JSR': 66.73, 'PSR': 53.98},
    '#8': {'HR': 4.05,  'JSR': 71.54, 'PSR': 48.76},
}
group_positions = np.arange(len(groups))
width = 0.2
colors = {'HR': 'red', 'JSR': 'green', 'PSR': 'blue'}
colors2 = {'HR': 'darkred', 'JSR': 'darkgreen', 'PSR': 'darkblue'}
plt.figure(figsize=(10, 6))

for i, cat in enumerate(categories):
    for j, group in enumerate(groups):
        y_vals = data[group].get(cat, [])
        x_vals = np.full(len(y_vals), group_positions[j] + (i - 1) * width)
        plt.scatter(x_vals, y_vals, color=colors[cat],s=20, label='Base ' + cat if j == 0 else "", alpha=0.7)
for i, cat in enumerate(categories):
    for j, group in enumerate(groups):
        y = special_points[group][cat] / 100
        x = group_positions[j] + (i - 1) * width
        plt.scatter(x, y, color=colors2[cat], marker='x', s=50, label='Merged ' + cat if j == 0 else "")
for i in range(len(groups) - 1):
    midpoint = (group_positions[i] + group_positions[i + 1]) / 2
    plt.axvline(x=midpoint, color='gray', linestyle='--', linewidth=0.8, alpha=0.6)
plt.xticks(group_positions, groups, rotation=0, fontsize=32)
yticks = np.arange(0, 1.0, 0.2) 
plt.yticks(yticks)
for y in yticks:
    plt.axhline(y=y, color='gray', linestyle='--', linewidth=0.6, alpha=0.5)
plt.ylabel('Risk Value')
handles, labels = plt.gca().get_legend_handles_labels()

from collections import OrderedDict
legend_dict = OrderedDict()
for h, l in zip(handles, labels):
    if l and l not in legend_dict:
        legend_dict[l] = h

desired_order = ['Base HR','Merged HR', 'Base JSR','Merged JSR', 'Base PSR' , 'Merged PSR']
ordered_handles = [legend_dict[l] for l in desired_order]
ordered_labels = desired_order

plt.legend(
    ordered_handles,
    ordered_labels,
    loc='upper center',
    bbox_to_anchor=(0.5, -0.12),
    ncol=3,
    fontsize=20,
    columnspacing=1.5,
    handletextpad=0.8
)
plt.tight_layout()
plt.savefig('./Merge.pdf', bbox_inches='tight')
plt.show()
