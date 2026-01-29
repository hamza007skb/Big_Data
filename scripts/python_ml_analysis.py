import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt


data_path = "/output/retail_data_sample.csv"
df = pd.read_csv(data_path)
df.columns = df.columns.str.strip()

# Feature engineering
df['Avg_Transaction'] = df['Total_Amount'] / df['Total_Purchases'].replace(0, 1)
df['Customer_Value_Score'] = (df['Total_Amount'] * df['Total_Purchases']) / 1000

# Encode categorical columns
categorical_cols = ['Gender', 'Payment_Method', 'Product_Category', 'Country', 'Income']
for col in categorical_cols:
    le = LabelEncoder()
    df[col + '_enc'] = le.fit_transform(df[col])

# Select features for ML
features = ['Age', 'Total_Purchases', 'Total_Amount', 'Ratings',
            'Gender_enc', 'Payment_Method_enc', 'Product_Category_enc', 'Country_enc', 'Income_enc']
X = df[features].copy()

# Impute missing values
X = X.replace([np.inf, -np.inf], np.nan)
imputer = SimpleImputer(strategy='median')
X_imputed = imputer.fit_transform(X)

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)


# --- K-Means clustering ---
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# --- Random Forest classification (predict Customer_Segment) ---
# Encode target
le_target = LabelEncoder()
y = le_target.fit_transform(df['Customer_Segment'])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# Train model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Predictions
y_pred = rf.predict(X_test)

# Evaluation
print("\nRandom Forest Classification Report:")
print(classification_report(y_test, y_pred))

# Cluster distribution
print("\nCustomer Segments (K-Means):")
print(df['Cluster'].value_counts())


# Scatter plot: Age vs Total_Amount
plt.figure(figsize=(10,5))
plt.scatter(df['Age'], df['Total_Amount'], c=df['Cluster'], cmap='viridis', alpha=0.6)
plt.xlabel('Age')
plt.ylabel('Total Amount')
plt.title('Customer Clusters: Age vs Total Amount')
plt.colorbar(label='Cluster')
plt.savefig('/output/customer_clusters.png')
plt.close()

# Payment Method distribution
payment_counts = df['Payment_Method'].value_counts()
plt.figure(figsize=(8,5))
plt.bar(payment_counts.index, payment_counts.values, color='skyblue')
plt.xticks(rotation=45)
plt.ylabel('Number of Customers')
plt.title('Payment Method Distribution')
plt.tight_layout()
plt.savefig('/output/payment_method_distribution.png')
plt.close()
