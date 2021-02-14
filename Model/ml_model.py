import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split  # data split
from sklearn.linear_model import LinearRegression  # OLS algorithm
from sklearn.linear_model import Ridge  # Ridge algorithm
from sklearn.linear_model import Lasso  # Lasso algorithm
from sklearn.linear_model import BayesianRidge  # Bayesian algorithm
from sklearn.linear_model import ElasticNet  # ElasticNet algorithm
from sklearn.metrics import explained_variance_score as evs  # evaluation metric
from termcolor import colored as cl
from pandas_convert import DataConverter


class MachineLearningModel:
    def __init__(self, name, user_input):
        self.ml_name = name
        # Example [4, 149, 4881, '0', 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.user_input: list = user_input
        self.choices: list = ['ols', 'ridge', 'lasso', 'bayesian', 'elasticnet']
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
        dummies = np.zeros(len(counties_list))
        index = counties_list.index(user_county)
        dummies[index] = 1
        self.user_input = self.user_input[0:4].append(dummies)
        self.user_input = np.array(self.user_input).reshape(1, -1)

    def ml_model(self):
        if self.name == "OLS":
            self.ols_model()
        elif self.name == "Ridge":
            self.ridge_model()
        elif self.name == "Lasso":
            self.lasso_model()
        elif self.name == "Bayesian":
            self.bayesian_model()
        else:
            self.elastic_net()

    def convert_data_to_pandas(self):
        converter = DataConverter(data_file='raw_data.json')
        self.df = converter.convert_json_to_pandas()

    def create_labels_and_features(self):
        self.labels = np.array(df['Cijena'])
        features = self.df.drop(['Lokacija', 'Cijena'], axis=1)
        feature_list = list(features.columns)
        self.features = np.array(features)

    # 1. OLS
    def ols_model(self):
        ols = LinearRegression()
        ols.fit(self.features, self.labels)
        self.prediction = ols.predict(self.user_input)

    # 2. Ridge
    def ridge_model(self):
        ridge = Ridge(alpha=0.5)
        ridge.fit(self.features, self.labels)
        self.prediction = ridge.predict(self.user_input)

    # 3. Lasso
    def lasso_model(self):
        lasso = Lasso(alpha=0.01)
        lasso.fit(self.features, self.labels)
        self.prediction = lasso.predict(self.user_input)

    # 4. Bayesian
    def bayesian_model(self):
        bayesian = BayesianRidge()
        bayesian.fit(self.features, self.labels)
        self.prediction = bayesian.predict(self.user_input)

    # 5. ElasticNet
    def elastic_net(self):
        en = ElasticNet(alpha=0.01)
        en.fit(self.features, self.labels)
        self.prediction = en.predict(self.user_input)



