import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = np.where((df['weight'] / (df['height'] / 100) ** 2) > 25, 1, 0)

# 3
df['cholesterol'] = (df['cholesterol'] != 1).astype(int)
df['gluc'] = (df['gluc'] != 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=['alco', 'smoke', "gluc" , 'cholesterol', 'overweight', 'active'])


    # 6
    df_cat = sns.catplot(x= "variable", kind ="count" ,hue = "value", data = df_cat, col= "cardio")
    df_cat.set_axis_labels("variable", "total") 
    

    # 7
    


    # 8
    fig = df_cat


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
         (df['ap_lo'] <= df['ap_hi']) & 
         (df['height'] >= df['height'].quantile(0.025)) & 
         (df['height'] <= df['height'].quantile(0.975)) &
         (df['weight'] >= df['weight'].quantile(0.025)) & 
         (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype= bool))



    # 14
    fig, ax = plt.subplots(figsize = (12,12))

    # 15

    sns.heatmap(corr, vmin=0, vmax= 0.25, fmt='.1f', linewidth = 1, annot = True, square = True, mask=mask, cbar_kws = {'shrink':.82})

    # 16
    fig.savefig('heatmap.png')
    return fig


draw_heat_map()
draw_cat_plot()