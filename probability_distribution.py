import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read excel files raw datas into variables
df_jan = pd.read_excel("Data/raw/Monthly+Power+Station+Chart_1-2026.xls", header=28)
df_mar = pd.read_excel("Data/raw/Monthly+Power+Station+Chart_3-2026.xls", header=28)
df_may = pd.read_excel("Data/raw/Monthly+Power+Station+Chart_5-2026.xls", header=28)
df_jul = pd.read_excel("Data/raw/Monthly+Power+Station+Chart_07-2026.xls", header=28)
df_aug = pd.read_excel("Data/raw/Monthly+Power+Station+Chart_08-2026.xls", header=28)

# Add new column to distinguish months
df_jan['Month'] = 'January'
df_mar['Month'] = 'March'
df_may['Month'] = 'May'
df_jul['Month'] = 'July'
df_aug['Month'] = 'August'

# Combine all dataset into 1 master dataset
df_all = pd.concat([df_jan, df_mar, df_may, df_jul, df_aug], ignore_index=True)
# Change the 'Time' from (str) datatype -> actual time datatype in the dataset
df_all['Time'] = pd.to_datetime(df_all['Time'], dayfirst=True)

# Set up the canva size + font
plt.figure(figsize=(12, 6))
sns.set_theme(style = 'whitegrid', rc = {'font.family': 'Times New Roman'})

# Draw the violin plot
sns.violinplot(
    data = df_all,
    x = 'Month',
    y = 'Yield(kWh)',
    color = '#c1493b',
    inner = 'box', #thick black bar
)
# inner context + condition 
plt.ylim(bottom = 0, top = 100)
plt.title("PV energy probability distribution", fontsize=20, fontweight='bold', color="#23497c")
plt.ylabel("PV energy output (kWh)", fontsize=15, fontweight='bold')
plt.xlabel("Month", fontsize=15, fontweight='bold')
# increase the size of numbers/ticks on axes
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
# Render + Output
plt.tight_layout()
plt.savefig('5_months_probability_distribution_chart.png', dpi = 300, bbox_inches='tight')
