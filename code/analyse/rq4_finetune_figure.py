import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import json
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
fm.fontManager.addfont('../../Font/times.ttf')
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "font.size": 16,              
    "figure.figsize": (3.5, 2.5), 
    "lines.linewidth": 1,
    "lines.markersize": 4,
    "axes.linewidth": 0.8,
    "axes.titlesize": 10,
    "axes.labelsize": 20,
    "axes.grid": True,
    "grid.linestyle": "--",
    "grid.linewidth": 0.5,
    "grid.alpha": 0.7,
    "xtick.labelsize": 20,
    "ytick.labelsize": 20,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.top": True,
    "ytick.right": True,
    "legend.fontsize": 20,
    "legend.frameon": False,
    "savefig.dpi": 3600,
    "savefig.bbox": "tight"
})
data_dict = {
    'SFT': {
        'HR': [
            0.0023, 0.1564, -0.2313, 0.1355, 0.1216, -0.0249, -0.1868,
            -0.1396, -0.0394, -0.0611, 0.1355, 0.1216, -0.1236, 0.0269,
            -0.3654, -0.4727, -0.6739, -0.6283, -0.1868
        ],
        'JSR': [
            -0.1654, -0.1, -0.075, -0.1385, -0.1673, -0.2039, 0.05,
            0.489, 0.332, 0.368, -0.1385, -0.1673, -0.2692, 0.525,
            -0.0327, 0.4, 0.3539, 0.6116, 0.05
        ],  
        'PSR': [
            -0.0168, -0.01, 0.306, 0.3967, 0.179, 0.045, 0.2247,
            0.036, 0.2861, 0.1524, 0.3967, 0.179, 0.1632, 0.2241,
            0.4804, 0.3547, 0.357, 0.4915, 0.2247
        ],
    },
    'PEFT': {
        'HR': [
            -0.0355, -0.0373, -0.0373, -0.0006, -0.001, 0.0001, 0.0005,
            0.0019, -0.0061, -0.0067, -0.0017, -0.0026, -0.0015, -0.0027,
            -0.0045, -0.0015
        ],
        'JSR': [
            -0.0327, -0.0423, -0.0519, 0.025, 0.0231, 0.0115, 0.0058,
            0.0404, -0.1597, -0.1116, -0.1077, -0.0904
        ],
        'PSR': [
            0.3401, -0.0086, -0.0068, -0.0026, -0.0022, 0.0002, -0.0016,
            0.0013, -0.3482, -0.2933, -0.2928, -0.4028, 0.1164, 0.1153,
            0.0257, 0.0271
        ],
    },
    'Others': {
        'HR': [
        0.0879, 0.9121, -0.01, -0.0033, -0.0015, -0.0022, 0.0009,
        0.6493, 0.2844, -0.0033, 0.1049, -0.0611, 0.6674, -0.1524,
        -0.1551, 0.0, -0.1929, -0.2224, -0.2335, -0.2407, -0.2236,
        -0.2206, -0.2206, -0.0301, 0.1771, -0.0028, -0.1586, -0.1523,
        -0.0353, 0.0269, 0.0288, -0.0423, 0.0242, 0.1986, -0.0107,
        0.0181, -0.2399
        ],
        'JSR': [
            -0.25, 0.4231, 0.0153, 0.0211, -0.0346, -0.0057, 0.0154,
            -0.3, -0.1077, 0.1077, 0.1846, -0.3365, -0.225, -0.0231,
            -0.0212, -0.0288, 0.1096, 0.0961, -0.0481, 0.1077, 0.0885,
            -0.2404, -0.0712, 0.0019, -0.5346, -0.6115, -0.0057, 0.525,
            0.4635, -0.2866, 0.0365, -0.0943, -0.0327, -0.0635, 0.0576
        ],
        'PSR': [
            -0.0097, -0.0147, -0.0071, 0.0318, -0.0058, 0.0192,
            -0.404, -0.1069, 0.1123, 0.0601, 0.1524, 0.2239,
            0.2734, 0.0029, 0.2426, 0.2028, 0.3575, 0.2857,
            0.3373, 0.3261, 0.3642, 0.211, 0.3045, 0.0002,
            0.0209, 0.1177, -0.1038, 0.2241, 0.2206, 0.2203,
            -0.0643, -0.0202, -0.0447, 0.2008
        ],
    }
}

# ====== 统计箱线图数据 ======
stats = []

for relation, categories in data_dict.items():
    for metric, values in categories.items():
        values = np.array(values)
        Q1 = np.percentile(values, 25)
        Q2 = np.percentile(values, 50)
        Q3 = np.percentile(values, 75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outliers = values[(values < lower) | (values > upper)]
        normal = values[(values >= lower) & (values <= upper)]

        stats.append({
            "relation": relation,
            "metric": metric,
            "total_points": len(values),
            "normal_points": len(normal),
            "outlier_points": len(outliers),
            "Q1": f"{Q1:.2f}",
            "Q2": f"{Q2:.2f}",
            "Q3": f"{Q3:.2f}",
            "IQR": f"{IQR:.2f}",
            "lower_bound": f"{lower:.2f}",
            "upper_bound": f"{upper:.2f}"
        })

json_output = json.dumps(stats, indent=2)
print(json_output)

df = pd.DataFrame([
    {'Group': rel, 'Type': met, 'Value': val}
    for rel, cat in data_dict.items()
    for met, vals in cat.items()
    for val in vals
])

plt.figure(figsize=(10, 6))
sns.boxplot(x='Group', y='Value', hue='Type', data=df)
plt.ylabel('Risk Difference Value')
plt.legend(loc='upper center')
plt.tight_layout()
plt.savefig('./Finetune.pdf', bbox_inches='tight')
plt.show()
