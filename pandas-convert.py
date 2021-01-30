import json
import pandas as pd
import matplotlib.pyplot as plt
from termcolor import colored as cl # text customization
import seaborn as sb # visualization

with open("data.json") as obj:
    data = json.load(obj)

#def convert_pandas(data_set):

df = pd.DataFrame(data.values())


# Plot
#plt.scatter(df.area,df.price,s=1,c='magenta')
#plt.xlim(0,4000)
#plt.title('Scatter plot')
#plt.xlabel('area[$m^2$]')
#plt.ylabel('price[hrk]')
#plt.show()
print(df.columns)

#dummies = pd.get_dummies(df.location)
#df = df.join(dummies)


#df = df.drop('location',axis=1)

#print(len(df[df.Šolta == 1]))
print('')
#print(df.describe())

#Data types
#print(cl(df.dtypes,attrs=['bold']))


sb.heatmap(df.corr(), annot = True, cmap = 'magma')
plt.show()




