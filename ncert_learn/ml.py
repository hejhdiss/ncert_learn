import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import joblib
import matplotlib.pyplot as plt



# --------------------------- Data Cleaning Functions ---------------------------

def handle_missing_values(df, strategy='mean'):
    """Handles missing values in a DataFrame using specified strategy."""
    try:
        imputer = SimpleImputer(strategy=strategy)
        return pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    except Exception as e:
        print(f"Error in handle_missing_values: {e}")
        return None

def normalize_data(df):
    """Normalizes the dataset (scales the data between 0 and 1)."""
    try:
        return (df - df.min()) / (df.max() - df.min())
    except Exception as e:
        print(f"Error in normalize_data: {e}")
        return None

def standardize_data(df):
    """Standardizes the dataset (scales the data to have mean=0 and std=1)."""
    try:
        scaler = StandardScaler()
        return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    except Exception as e:
        print(f"Error in standardize_data: {e}")
        return None

def encode_categorical_columns(df):
    """Encodes categorical columns using one-hot encoding."""
    try:
        return pd.get_dummies(df)
    except Exception as e:
        print(f"Error in encode_categorical_columns: {e}")
        return None

def split_dataset(df, target_column, test_size=0.2, random_state=42):
    """Splits the dataset into training and testing sets."""
    try:
        X = df.drop(columns=[target_column])
        y = df[target_column]
        return train_test_split(X, y, test_size=test_size, random_state=random_state)
    except Exception as e:
        print(f"Error in split_dataset: {e}")
        return None, None, None, None


# --------------------------- Basic Machine Learning Models ---------------------------

def linear_regression_model(X_train, y_train, X_test):
    """Fits a linear regression model and makes predictions."""
    try:
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model.predict(X_test), model
    except Exception as e:
        print(f"Error in linear_regression_model: {e}")
        return None, None

def evaluate_regression_model(y_true, y_pred):
    """Evaluates the regression model using Mean Squared Error."""
    try:
        return mean_squared_error(y_true, y_pred)
    except Exception as e:
        print(f"Error in evaluate_regression_model: {e}")
        return None

def evaluate_classification_model(y_true, y_pred):
    """Evaluates the classification model using accuracy score."""
    try:
        return accuracy_score(y_true, y_pred)
    except Exception as e:
        print(f"Error in evaluate_classification_model: {e}")
        return None


# --------------------------- Utility Functions ---------------------------

def shuffle_data(df):
    """Shuffles the rows of the DataFrame."""
    try:
        return df.sample(frac=1, random_state=42).reset_index(drop=True)
    except Exception as e:
        print(f"Error in shuffle_data: {e}")
        return None

def cross_validation(X, y, model, k=5):
    """Performs k-fold cross-validation on the given model."""
    try:
        fold_size = len(X) // k
        accuracies = []
        for i in range(k):
            test_data = X[i * fold_size: (i + 1) * fold_size]
            test_target = y[i * fold_size: (i + 1) * fold_size]
            train_data = np.concatenate([X[:i * fold_size], X[(i + 1) * fold_size:]], axis=0)
            train_target = np.concatenate([y[:i * fold_size], y[(i + 1) * fold_size:]], axis=0)

            model.fit(train_data, train_target)
            y_pred = model.predict(test_data)
            accuracies.append(accuracy_score(test_target, y_pred))

        return np.mean(accuracies)
    except Exception as e:
        print(f"Error in cross_validation: {e}")
        return None

def feature_importance(model, X):
    """Returns the feature importance of a trained model."""
    try:
        if hasattr(model, 'coef_'):
            return model.coef_
        elif hasattr(model, 'feature_importances_'):
            return model.feature_importances_
        else:
            raise ValueError("Model does not have feature importance attribute.")
    except Exception as e:
        print(f"Error in feature_importance: {e}")
        return None


# --------------------------- Model Persistence Functions ---------------------------

def save_model(model, filename):
    """Saves the trained model to a file."""
    try:
        joblib.dump(model, filename)
        return True
    except Exception as e:
        print(f"Error in save_model: {e}")
        return False

def load_model(filename):
    """Loads a trained model from a file."""
    try:
        return joblib.load(filename)
    except Exception as e:
        print(f"Error in load_model: {e}")
        return None


# --------------------------- Data Visualization Functions ---------------------------

def plot_data(X, y, plot_type='scatter'):
    """Plots the data (scatter or line plot)."""
    try:
        if plot_type == 'scatter':
            plt.scatter(X, y)
        elif plot_type == 'line':
            plt.plot(X, y)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'{plot_type.capitalize()} Plot')
        plt.show()
    except Exception as e:
        print(f"Error in plot_data: {e}")
        return False

def plot_decision_boundary(model, X, y):
    """Plots the decision boundary of a classifier."""
    try:
        h = .02  # Step size in the mesh
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, alpha=0.8)
        plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o', s=30)
        plt.title('Decision Boundary')
        plt.show()
    except Exception as e:
        print(f"Error in plot_decision_boundary: {e}")
        return False


# --------------------------- Advanced Model Functions ---------------------------

def polynomial_features(X, degree=2):
    """Generates polynomial features for the dataset."""
    try:
        poly = PolynomialFeatures(degree)
        return poly.fit_transform(X)
    except Exception as e:
        print(f"Error in polynomial_features: {e}")
        return None

def logistic_regression_model(X_train, y_train, X_test):
    """Fits a logistic regression model and makes predictions."""
    try:
        model = LogisticRegression()
        model.fit(X_train, y_train)
        return model.predict(X_test), model
    except Exception as e:
        print(f"Error in logistic_regression_model: {e}")
        return None, None

def decision_tree_model(X_train, y_train, X_test):
    """Fits a decision tree model and makes predictions."""
    try:
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)
        return model.predict(X_test), model
    except Exception as e:
        print(f"Error in decision_tree_model: {e}")
        return None, None

def random_forest_model(X_train, y_train, X_test):
    """Fits a random forest model and makes predictions."""
    try:
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        return model.predict(X_test), model
    except Exception as e:
        print(f"Error in random_forest_model: {e}")
        return None, None
