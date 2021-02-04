import json
import pandas as pd
import matplotlib.pyplot as plt
from termcolor import colored as cl # text customization
import seaborn as sb # visualization
import sns

def convert_pandas():
    with open("data3.json") as obj:
        data = json.load(obj)
    df = pd.DataFrame(data.values())
    df[["Broj soba","Broj parkirnih mjesta"]] = df[["Broj soba","Broj parkirnih mjesta"]].apply(pd.to_numeric)
    df.Cijena = df.Cijena.map(lambda element: int(element.replace(".","")))
    df["Stambena površina"] = df["Stambena površina"].map(lambda element:element.replace(".","").replace(",",".").split("m")[0])
    df["Površina okućnice"] = df["Površina okućnice"].map(lambda element:element.replace(".","").replace(",",".").split("m")[0])
    df[["Stambena površina","Površina okućnice"]] = df[["Stambena površina","Površina okućnice"]].apply(pd.to_numeric)
    df["Pogled na more"] = pd.to_numeric(df["Pogled na more"].replace("Da","1"))
    return df

def english_translate(df):
    croatian = list(df.columns)
    english = ["Loc", "N_rooms","Sqr_in","Sqr_out","Parking","View","Price"]
    translate = {}
    for i,column in enumerate(croatian):
        translate[str(column)] = english[i]
    df = df.rename(columns = translate)
    return df

def give_excel(language):
    language = language.lower() 
    if language == "english":
        english_translate(convert_pandas()).to_excel("data_{}.xlsx".format(language),index = False)  
    elif language == "croatian":
        convert_pandas().to_excel("data_{}.xlsx".format(language),index = False)  
    else:
        print("Data available only in english and croatian")

df_english = english_translate(convert_pandas())
#give_excel("english")
print(df_english.describe())


def most_common(df,parameter):
    df[parameter].value_counts().plot(kind='bar')
    plt.ylabel("Count")
    plt.xlabel(parameter)
    plt.show()


#most_common(df_english,"N_rooms")
#most_common(df_english,"Loc")

plt.figure(1)
plt.scatter(df_english.Price,df_english.Loc)
plt.xlabel('Price in HRK')
plt.show()


plt.figure(2)
plt.scatter(df_english.View,df_english.Price)
plt.xlabel('Seaview')
plt.show()







