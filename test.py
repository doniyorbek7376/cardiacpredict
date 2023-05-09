import tensorflow_decision_forests as tfdf
import numpy as np
import pandas as pd
import pickle

dataset_df = pd.read_csv("resources/framingham.csv")
label = "TenYearCHD"

def split_dataset(dataset, test_ratio=0.30):
  """Splits a panda dataframe in two."""
  test_indices = np.random.rand(len(dataset)) < test_ratio
  return dataset[~test_indices], dataset[test_indices]


train_ds_pd, test_ds_pd = split_dataset(dataset_df, 0.01)
print("{} examples in training, {} examples for testing.".format(
    len(train_ds_pd), len(test_ds_pd)))

train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(train_ds_pd, label=label)
test_ds = tfdf.keras.pd_dataframe_to_tf_dataset(test_ds_pd, label=label)

model_1 = tfdf.keras.RandomForestModel(verbose=2)

model_1.fit(train_ds)

model_1.compile(metrics=['accuracy'])
evaluation = model_1.evaluate(test_ds, return_dict=True)
print(evaluation)
model_1.summary()

with open('tf_rf.pkl', 'wb') as f:
    pickle.dump(model_1, f)