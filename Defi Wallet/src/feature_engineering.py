import pandas as pd
import numpy as np

def extract_wallet_features(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    
    def compute_features(group):
        total_deposit = group[group['action'] == 'deposit']['amount'].sum()
        total_borrow = group[group['action'] == 'borrow']['amount'].sum()
        total_repay = group[group['action'] == 'repay']['amount'].sum()
        total_redeem = group[group['action'] == 'redeemunderlying']['amount'].sum()
        liquidation_count = (group['action'] == 'liquidationcall').sum()
        
        repay_ratio = total_repay / total_borrow if total_borrow > 0 else 1
        redeem_ratio = total_redeem / total_deposit if total_deposit > 0 else 0
        
        active_days = group['timestamp'].dt.date.nunique()
        tx_count = group.shape[0]
        tx_gap = group['timestamp'].sort_values().diff().dt.total_seconds().dropna()
        avg_gap = tx_gap.mean() if not tx_gap.empty else 0

        return pd.Series({
            'wallet_address': group['wallet_address'].iloc[0],
            'total_deposit': total_deposit,
            'total_borrow': total_borrow,
            'total_repay': total_repay,
            'total_redeem': total_redeem,
            'liquidation_count': liquidation_count,
            'repay_ratio': repay_ratio,
            'redeem_ratio': redeem_ratio,
            'active_days': active_days,
            'avg_tx_gap': avg_gap,
            'tx_count': tx_count
        })

    features = df.groupby('wallet_address').apply(compute_features).reset_index(drop=True)
    return features
