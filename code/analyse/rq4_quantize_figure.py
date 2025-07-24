import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.font_manager as fm

# 添加字体
fm.fontManager.addfont('../../Font/times.ttf')
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "mathtext.fontset": "stix",
    "font.size": 20,
    "figure.figsize": (18, 5),
    "lines.linewidth": 1,
    "lines.markersize": 4,
    "axes.linewidth": 0.8,
    "axes.titlesize": 28,
    "axes.labelsize": 28,
    "axes.grid": True,
    "grid.linestyle": "--",
    "grid.linewidth": 0.5,
    "grid.alpha": 0.7,
    "xtick.labelsize": 28,
    "ytick.labelsize": 26,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.top": True,
    "ytick.right": True,
    "legend.fontsize": 20,
    "legend.frameon": False,
    "savefig.dpi": 3600,
    "savefig.bbox": "tight"
})

data = np.array([
    [68.29, 14.62, 10.56],
    [15.61, 70.00, 28.41],
    [8.92,  70.38, 26.75],
    [9.00,  83.46, 23.03],
    [9.95,  58.46, 21.69],
    [4.26,  79.81, 36.29],
    [4.50,  79.42, 34.54],
    [5.32,  83.08, 34.16],
    [1.85,  71.92, 49.94],
    [1.18,  69.04, 48.28],
    [1.99,  69.62, 48.85],
    [1.44,  67.50, 48.79],
    [2.65,  86.73, 29.55],
    [3.05,  85.58, 34.93],
    [2.07,  86.73, 34.22],
    [1.86,  83.26, 34.02],
]) / 100

risk_labels = ['HR', 'JSR', 'PSR']
model_types = ['Q2', 'Q4', 'Q8', 'Base']
num_groups = 4

fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharey=False)
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
names = [
    "sail/Sailor-0.5B-Chat-gguf",
    "sail/Sailor-1.8B-Chat-gguf",
    "MaziyarPanahi/Qwen2.5-7B-Instruct-GGUF",
    "mradermacher/Deepseek-R1-Distill-NSFW-RPv1-GGUF"
]

legend_lines = []
legend_labels = []

for risk_idx, label in enumerate(risk_labels):
    ax = axes[risk_idx]
    for group_idx in range(num_groups):
        row_start = group_idx * 4
        y_values = data[row_start:row_start+4, risk_idx]
        line, = ax.plot(model_types, y_values, marker='o', color=colors[group_idx], label=names[group_idx])
        if risk_idx == 0:
            legend_lines.append(line)
            legend_labels.append(names[group_idx])

    ax.set_title(label, fontsize=20)
    ax.set_ylabel('Risk Value')
    ax.grid(True)

fig.legend(
    legend_lines, legend_labels,
    loc='lower center',
    bbox_to_anchor=(0.5, -0.25),
    ncol=2,
    fontsize=24
)

plt.tight_layout(rect=[0, 0.00, 1, 1])
plt.savefig('./Quantize.pdf')
plt.show()
