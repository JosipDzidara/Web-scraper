from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np

from pandas_convert import DataConverter

converter = DataConverter(data_file='raw_data.json')
df_croatian = converter.convert_json_to_pandas()
df = converter.english_translation(df_croatian)
print(df.describe())
labels = np.array(df['Price'])
features = df.drop(['Location', 'Price'], axis=1)
# Saving feature names for later use
feature_list = list(features.columns)
features = np.array(features)


train_features, test_features, train_labels, test_labels = train_test_split(features, labels,
                                                                            test_size=0.25, random_state=42)

# # The baseline predictions are the historical averages
# baseline_predictions = test_features[:, feature_list.index('average')]
# # Baseline errors, and display average baseline error
# baseline_errors = abs(baseline_predictions - test_labels)
# print('Average baseline error: ', round(np.mean(baseline_errors), 2))

# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators=24, random_state=42)
# Train the model on training data
rf.fit(train_features, train_labels)

# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'kuna.')

# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / test_labels)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')


