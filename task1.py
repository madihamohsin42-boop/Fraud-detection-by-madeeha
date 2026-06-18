import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

# 1Read CSV
df = pd.read_csv('credit_card_fraud_10k.csv')

print(df.columns)
print(df.head())

print("Data loaded. Rows:", len(df))
print("Fraud cases:", df['is_fraud'].sum())
print("Normal cases:", len(df) - df['is_fraud'].sum())

# 2. histogram of normal  vs Fraud amount
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
df[df['is_fraud']==0]['amount'].hist(bins=50, color='green', alpha=0.7)
plt.title('Normal Transactions')
plt.xlabel('amount')

plt.subplot(1,2,2)
df[df['is_fraud']==1]['amount'].hist(bins=50, color='red', alpha=0.7)
plt.title('Fraud Transactions')
plt.xlabel('amount')

plt.suptitle('Project 2: Fraud Detection - amount Distribution')
plt.tight_layout()
plt.savefig('fraud_amount_distribution.png',dpi=300, bbox_inches='tight')
plt.show()

print("Graph complete! Project 2 done")
