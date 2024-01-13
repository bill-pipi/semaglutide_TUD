import pandas as pd
import sys
import os
from matplotlib import pyplot as plt
import numpy as np
from labellines import labelLines
from matplotlib.font_manager import FontProperties


fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(12, 8), height_ratios=[10, 1])


df = pd.read_csv(sys.argv[1], skiprows=6)
#print(df['Cohort 1: Survival Probability'].head(5))

##AA BB contains the  day, count pairs, creatd using tt.sh
AA = pd.read_csv(os.path.dirname(sys.argv[1])+'/AA.txt')
BB = pd.read_csv(os.path.dirname(sys.argv[1])+'/BB.txt')
###read title / row name etc from params.txt
PARAMS =  pd.read_csv(os.path.dirname(sys.argv[1])+'/PARAMS.txt')
probability = PARAMS.to_numpy()[0][0]
t2d = PARAMS.to_numpy()[0][1].lstrip()
comparison = PARAMS.to_numpy()[0][2].lstrip()
title = "Survival probability for {} ({}) (%)".format(probability, t2d)

print (AA['count'].to_numpy())

for column in df:
    df[column].fillna(method='pad', inplace=True)

###resizing###

#plt.subplots_adjust(left=0.5, bottom=0.1, right=0.96, top=0.90)
#plt.xlim(xmin=14)
#plt.locator_params(axis="y", nbins=10)

##############################################################

x = df['Time (Days)']

cohort1 = df['Cohort 1: Survival Probability'] * 100
lower1 = df['Cohort 1: Survival Probability 95 % CI Lower'] * 100
upper1 = df['Cohort 1: Survival Probability 95 % CI Upper'] * 100

cohort2 = df['Cohort 2: Survival Probability'] * 100
lower2 = df['Cohort 2: Survival Probability 95 % CI Lower'] * 100
upper2 = df['Cohort 2: Survival Probability 95 % CI Upper'] * 100

ax0.plot(x,  cohort1, '-', label="Semaglutide", color="#7B16EF")
ax0.fill_between(x, lower1,  upper1, alpha=0.2, color="#7B16EF")

ax0.plot(x,  cohort2, '-', label=comparison, color="#59C1AB")
ax0.fill_between(x, lower2,  upper2, alpha=0.2, color="#59C1AB")

labelLines(ax0.get_lines(), zorder=2.5, fontsize=18)

#plt.legend()
plt.subplots_adjust(left=0.1)
ax0.grid(axis = 'y')
ax0.set_title(title, fontsize=20, pad=20, weight='bold')
ax0.set_xlabel("Days", fontsize=16, weight='bold')
ax0.set_ylabel("Survival Probability (%)", fontsize=16, weight='bold')
ticks = [0, 90, 180, 270, 360]
ax0.set_xticks(ticks)
ax0.set_position([0.15, 0.1700, 0.8, 0.75])
##ax0.set_yticks(fontsize=13)
#plt.legend(prop={'size': 14})



data = [['','','','',''], AA['count'].to_numpy(),
        BB['count'].to_numpy()]
columns = ('ABC')
rows = ['Number at Risk', 'Semaglutide', comparison]
n_rows = len(data)
cell_text = []
y_offset = np.zeros(len(columns))
for row in range(n_rows):
    y_offset =  data[row]
    cell_text.append([x for x in y_offset])

ax1.set_position([0.153, 0.1, 0.9, 0.8150])
ax1.axis("tight");
ax1.axis("off")

# Add a table at the bottom of the axes
the_table = ax1.table(cellText=cell_text,
                      rowLabels=rows,
                      cellLoc='left',
                      loc='bottom',
                      colWidths=[0.2005, 0.2005, 0.2005, 0.2005, 0.2005])
#remove borders for table cells
for key, cell in the_table.get_celld().items():
    cell.set_linewidth(0)


##https://matplotlib.org/3.0.3/gallery/text_labels_and_annotations/font_table_ttf_sgskip.html
for (row, col), cell in the_table.get_celld().items():
    if(col==-1 and row==0):
        cell.set_text_props(fontproperties=FontProperties(weight='bold'))
    if (col == -1):
        cell.set_text_props(horizontalalignment="right")

#plt.savefig("ICU.jpg")
plt.savefig(os.path.dirname(sys.argv[1])+'.jpg', bbox_inches='tight')

#plt.show()
