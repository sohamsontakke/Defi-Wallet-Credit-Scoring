from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

def generate_scores(df):
    df = df.fillna(0)

    scaler = MinMaxScaler()
    to_scale = df[['repay_ratio', 'total_deposit', 'redeem_ratio', 'active_days', 'avg_tx_gap']]
    scaled = scaler.fit_transform(to_scale)

    df_scaled = pd.DataFrame(scaled, columns=to_scale.columns)

    score = (
        0.25 * df_scaled['repay_ratio'] +
        0.25 * df_scaled['total_deposit'] +
        0.15 * df_scaled['redeem_ratio'] +
        0.15 * df_scaled['active_days'] -
        0.20 * (df['liquidation_count'] / (df['tx_count'] + 1))
    ) * 1000

    return score.clip(0, 1000).astype(int)