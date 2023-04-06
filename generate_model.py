import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
file_name = input("Enter dataset file name: ")
df = pd.read_csv(file_name)

# Drop rows with missing values
df.dropna(inplace=True)

# Split the dataset into features and target variable
X = df.drop('TenYearCHD', axis=1).drop('education', axis=1)
y = df['TenYearCHD']

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Create a Random Forest classifier with 100 trees
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on the training data
rf.fit(X_train, y_train)

# Test the model on the test data
y_pred = rf.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# Save the trained model to a file
with open('rf_model.pkl', 'wb') as f:
    pickle.dump(rf, f)


