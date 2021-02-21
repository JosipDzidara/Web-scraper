from pprint import pprint

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression  # OLS algorithm
from sklearn.linear_model import Ridge  # Ridge algorithm
from sklearn.linear_model import Lasso  # Lasso algorithm
from sklearn.linear_model import BayesianRidge  # Bayesian algorithm
from sklearn.linear_model import ElasticNet  # ElasticNet algorithm
from ML_Model.pandas_convert import DataConverter


class MachineLearningModel:
    def __init__(self, name, user_input):
        self.ml_name = name
        self.user_input: list = user_input
        self.df = pd.DataFrame([])
        self.features = np.array([])
        self.labels = np.array([])
        self.prediction: int = 0

    def start_ml_analysis(self):
        self.serialize_user_input()
        self.convert_data_to_pandas()
        self.create_labels_and_features()
        self.ml_model()

    def serialize_user_input(self):
        counties_list = ['Bjelovarsko-bilogorska', 'Brodsko-posavska', 'Dubrovačko-neretvanska',
                'Grad Zagreb', 'Istarska', 'Karlovačka', 'Koprivničko-križevačka',
                'Krapinsko-zagorska', 'Ličko-senjska', 'Međimurska',
                'Osječko-baranjska', 'Požeško-slavonska', 'Primorsko-goranska',
                'Sisačko-moslavačka', 'Splitsko-dalmatinska', 'Varaždinska',
                'Virovitičko-podravska', 'Vukovarsko-srijemska', 'Zadarska',
                'Zagrebačka', 'Šibensko-kninska']
        user_county = self.user_input[-1]
        dummies = [0]*len(counties_list)
        index = counties_list.index(user_county)
        dummies[index] = 1
        self.user_input.remove(self.user_input[-1])
        self.user_input.extend(dummies)
        self.user_input = np.array(self.user_input).reshape(1, -1)

    def ml_model(self):
        if self.ml_name == "OLS":
            prediction = self.ols_model()
        elif self.ml_name == "Ridge":
            self.ridge_model()
        elif self.ml_name == "Lasso":
            self.lasso_model()
        elif self.ml_name == "Bayesian":
            self.bayesian_model()
        else:
            self.elastic_net()

    def convert_data_to_pandas(self):
        converter = DataConverter(data_file=r'C:\Users\jddzi\Desktop\Web-scraper\Source\ML_Model\raw_data.json')
        self.df = converter.convert_json_to_pandas()

    def create_labels_and_features(self):
        self.labels = np.array(self.df['Cijena'])
        features = self.df.drop(['Lokacija', 'Cijena'], axis=1)
        self.features = np.array(features)

    # 1. OLS
    def ols_model(self):
        ols = LinearRegression()
        ols.fit(self.features, self.labels)
        prediction = round(ols.predict(self.user_input)[0])
        return prediction


    # 2. Ridge
    def ridge_model(self):
        ridge = Ridge(alpha=0.5)
        ridge.fit(self.features, self.labels)
        self.prediction = round(ridge.predict(self.user_input)[0])

    # 3. Lasso
    def lasso_model(self):
        lasso = Lasso(alpha=0.01)
        lasso.fit(self.features, self.labels)
        self.prediction = round(lasso.predict(self.user_input)[0])

    # 4. Bayesian
    def bayesian_model(self):
        bayesian = BayesianRidge()
        bayesian.fit(self.features, self.labels)
        self.prediction = round(bayesian.predict(self.user_input)[0])

    # 5. ElasticNet
    def elastic_net(self):
        en = ElasticNet(alpha=0.01)
        en.fit(self.features, self.labels)
        self.prediction = round(en.predict(self.user_input)[0])




