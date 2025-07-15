import json
import pandas as pd

def load_transactions(path):
    with open(path, 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    # Normalize field names
    df['wallet_address'] = df['userWallet']
    df['amount'] = df['actionData'].apply(lambda x: float(x.get('amount', 0)))

    return df

def save_scores(df, output_path):
    df.to_csv(output_path, index=False)
