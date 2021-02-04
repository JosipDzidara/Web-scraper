# from sklearn.model_selection import train_test_split
import numpy as np

from .pandas_convert import DataConverter


converter = DataConverter(data_file='raw_data.json')
df_croatian = converter.convert_json_to_pandas()
df = converter.english_translation(df_croatian)
features = df.drop(['Location', 'Price'], axis=1)
labels = np.array(features['Price'])
features = np.array(features)

print("Label {}".format(labels))
print("Features {}".format(features))


# train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)