import numpy as np
from sklearn.model_selection import train_test_split  # data split
from sklearn.linear_model import LinearRegression  # OLS algorithm
from sklearn.linear_model import Ridge  # Ridge algorithm
from sklearn.linear_model import Lasso  # Lasso algorithm
from sklearn.linear_model import BayesianRidge  # Bayesian algorithm
from sklearn.linear_model import ElasticNet  # ElasticNet algorithm
from sklearn.metrics import explained_variance_score as evs  # evaluation metric
from termcolor import colored as cl
from pandas_convert import DataConverter


converter = DataConverter(data_file='raw_data.json')
df = converter.convert_json_to_pandas()
labels = np.array(df['Cijena'])
features = df.drop(['Lokacija', 'Cijena'], axis=1)
feature_list = list(features.columns)
features = np.array(features)

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=0)
# MODELING

# 1. OLS

ols = LinearRegression()
ols.fit(X_train, y_train)
ols_yhat = ols.predict(X_test)
# 2. Ridge

ridge = Ridge(alpha=0.5)
ridge.fit(X_train, y_train)
ridge_yhat = ridge.predict(X_test)

# 3. Lasso

lasso = Lasso(alpha=0.01)
lasso.fit(X_train, y_train)
lasso_yhat = lasso.predict(X_test)

# 4. Bayesian

bayesian = BayesianRidge()
bayesian.fit(X_train, y_train)
bayesian_yhat = bayesian.predict(X_test)

# 5. ElasticNet

en = ElasticNet(alpha=0.01)
en.fit(X_train, y_train)
en_yhat = en.predict(X_test)

print(cl('EXPLAINED VARIANCE SCORE:', attrs = ['bold']))
print('-------------------------------------------------------------------------------')
print(cl('Explained Variance Score of OLS model is {}'.format(evs(y_test, ols_yhat)), attrs = ['bold']))
print('-------------------------------------------------------------------------------')
print(cl('Explained Variance Score of Ridge model is {}'.format(evs(y_test, ridge_yhat)), attrs = ['bold']))
print('-------------------------------------------------------------------------------')
print(cl('Explained Variance Score of Lasso model is {}'.format(evs(y_test, lasso_yhat)), attrs = ['bold']))
print('-------------------------------------------------------------------------------')
print(cl('Explained Variance Score of Bayesian model is {}'.format(evs(y_test, bayesian_yhat)), attrs = ['bold']))
print('-------------------------------------------------------------------------------')
print(cl('Explained Variance Score of ElasticNet is {}'.format(evs(y_test, en_yhat)), attrs = ['bold']))
print('-------------------------------------------------------------------------------')