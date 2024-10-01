# Import necessary libraries for data manipulation, visualization, and machine learning
import pandas as pd           # For handling data in tabular form (like Excel sheets)
import numpy as np            # For numerical operations
import matplotlib.pyplot as plt   # For creating plots and graphs
import seaborn as sns         # For making attractive statistical graphics
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from sklearn.preprocessing import LabelEncoder, StandardScaler  # For encoding categories and scaling data
from sklearn.ensemble import RandomForestClassifier  # For building the machine learning model (Random Forest)
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report  # For evaluating the model

# Load the Titanic dataset directly from an online source (GitHub)
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)  # Read the data into a pandas DataFrame

# Step 1: Data exploration and cleaning
print(data.head())  # Print the first few rows of the dataset to understand its structure
print(data.isnull().sum())  # Check for missing values in each column

# Fill missing values in the 'Age' column with the median age (most common central value)
data['Age'].fillna(data['Age'].median(), inplace=True)
# Fill missing values in the 'Embarked' (port) column with the most frequent value (mode)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
# Drop the 'Cabin' column because it has too many missing values, which would be hard to fill in a meaningful way
data.drop(columns='Cabin', inplace=True)

# Step 2: Convert non-numeric (categorical) data to numeric values using LabelEncoder
# The 'Sex' and 'Embarked' columns contain text, so we need to convert them to numbers for machine learning
label_encoder = LabelEncoder()
data['Sex'] = label_encoder.fit_transform(data['Sex'])  # Convert 'male' and 'female' to 0 and 1
data['Embarked'] = label_encoder.fit_transform(data['Embarked'])  # Convert 'Embarked' categories to numbers

# Drop unnecessary columns like 'PassengerId', 'Name', and 'Ticket' as they don't provide useful information for predictions
data.drop(columns=['PassengerId', 'Name', 'Ticket'], inplace=True)

# Step 3: Exploratory Data Analysis (EDA) - Let's see relationships and distributions in the data
# Create a heatmap showing correlations between different variables (how related they are)
plt.figure(figsize=(10, 8))  # Set the figure size for better visibility
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")  # Visualize correlations with a heatmap
plt.title('Correlation between Features')  # Add a title to the heatmap
plt.show()  # Display the heatmap

# Show the distribution of the 'Survived' column (how many survived vs. how many didn't)
sns.countplot(x='Survived', data=data)  # Plot the survival count (0 = did not survive, 1 = survived)
plt.title('Survival Distribution')  # Add a title to the plot
plt.show()  # Display the plot

# Step 4: Preparing data for the model (Feature scaling and train-test split)
# 'X' contains all the features (columns used to predict), except the 'Survived' column (our target)
X = data.drop('Survived', axis=1)
# 'y' is the target variable (what we want to predict), which is the 'Survived' column
y = data['Survived']

# Split the data into a training set (80%) and a testing set (20%) so we can evaluate the model on unseen data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the feature data to make sure all values are in the same range (helps some models perform better)
scaler = StandardScaler()  # Initialize a StandardScaler (which normalizes the data)
X_train = scaler.fit_transform(X_train)  # Fit the scaler on the training data and transform it
X_test = scaler.transform(X_test)  # Use the same scaler to transform the test data

# Step 5: Train a Random Forest Classifier
# Initialize a Random Forest Classifier with 100 decision trees (n_estimators = 100)
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit (train) the Random Forest model on the training data (X_train and y_train)
clf.fit(X_train, y_train)

# Step 6: Make predictions and evaluate the model
# Use the trained model to predict survival on the test data (X_test)
y_pred = clf.predict(X_test)

# Calculate and print the accuracy of the model (percentage of correct predictions)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')  # Display accuracy as a percentage (e.g., 90%)

# Create a confusion matrix to see how well the model performed on different classes (survived vs. didn't survive)
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d')  # Visualize the confusion matrix as a heatmap
plt.title('Confusion Matrix')  # Add a title to the plot
plt.show()  # Display the heatmap

# Print a detailed classification report showing precision, recall, F1-score for each class (0 and 1)
print(classification_report(y_test, y_pred))
