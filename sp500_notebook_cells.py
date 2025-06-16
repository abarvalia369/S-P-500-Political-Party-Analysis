#%%
# Cell 1: Imports and Setup
# Copy everything below this line into your first code cell
#-----------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import statsmodels.api as sm
from scipy import stats

# Set visualization styles
plt.style.use('default')  # Changed from 'seaborn'
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['axes.grid'] = True  # Add grid by default
plt.rcParams['grid.alpha'] = 0.3  # Lighter grid lines

print('All imports successful!')
#%%

# Cell 2: Data Loading and Cleaning
# Copy everything below this line into your second code cell
#-----------------------------------------------------------
def clean_sp500_data(df):
    """Clean and prepare S&P 500 data for analysis."""
    df = df.copy()
    
    # Convert date
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Clean numeric columns
    numeric_cols = ['Price', 'Open', 'High', 'Low']
    for col in numeric_cols:
        df[col] = df[col].str.replace(',', '').astype(float)
    
    # Clean percentage column
    df['Change %'] = df['Change %'].str.replace('%', '').astype(float) / 100
    
    # Sort by date and reset index
    df = df.sort_values('Date').reset_index(drop=True)
    
    return df

# Load and clean data
sp500_data = pd.read_csv('S&P 500 Historical Data (1).csv')
sp500_clean = clean_sp500_data(sp500_data)

print("Data shape:", sp500_clean.shape)
print("\nFirst few rows:")
display(sp500_clean.head())
#%%
# Cell 3: Add Presidential Information
# Copy everything below this line into your third code cell
#-----------------------------------------------------------
def add_presidential_data(df):
    """Add presidential party information to the dataset."""
    presidents = {
        'Clinton': {'start': '1993-01-20', 'end': '2001-01-20', 'party': 'Democratic'},
        'Bush Jr': {'start': '2001-01-20', 'end': '2009-01-20', 'party': 'Republican'},
        'Obama': {'start': '2009-01-20', 'end': '2017-01-20', 'party': 'Democratic'},
        'Trump': {'start': '2017-01-20', 'end': '2021-01-20', 'party': 'Republican'},
        'Biden': {'start': '2021-01-20', 'end': '2025-01-20', 'party': 'Democratic'}
    }
    
    df = df.copy()
    df['President'] = ''
    df['Party'] = ''
    
    for president, info in presidents.items():
        mask = (df['Date'] >= pd.to_datetime(info['start'])) & \
               (df['Date'] < pd.to_datetime(info['end']))
        df.loc[mask, 'President'] = president
        df.loc[mask, 'Party'] = info['party']
    
    # Add binary indicator for Democratic (1) vs Republican (0)
    df['is_Democratic'] = (df['Party'] == 'Democratic').astype(int)
    
    return df

# Add presidential data
sp500_with_presidents = add_presidential_data(sp500_clean)

# Display distribution of data by party
party_dist = sp500_with_presidents['Party'].value_counts()
print("Number of trading days by party:")
print(party_dist)
print("\nSample of data with presidential information:")
display(sp500_with_presidents[['Date', 'Price', 'President', 'Party']].head())

#%%
# Cell 4: Calculate Returns
# Copy everything below this line into your fourth code cell
#-----------------------------------------------------------
def calculate_returns(df):
    """Calculate various return metrics."""
    df = df.copy()
    
    # Calculate returns
    df['Daily_Return'] = df['Price'].pct_change()
    df['Log_Return'] = np.log(df['Price'] / df['Price'].shift(1))
    df['Cumulative_Return'] = (1 + df['Daily_Return']).cumprod() - 1
    
    # Calculate rolling metrics
    df['Rolling_Vol_30d'] = df['Daily_Return'].rolling(window=30).std() * np.sqrt(252)
    df['Rolling_Return_30d'] = df['Daily_Return'].rolling(window=30).mean() * 252
    
    return df

# Calculate returns
sp500_with_returns = calculate_returns(sp500_with_presidents)

# Display summary statistics
print("Summary statistics of daily returns:")
print(sp500_with_returns['Daily_Return'].describe().round(4))

# Plot returns distribution with improved styling
plt.figure(figsize=(12, 6))
colors = ['#1f77b4', '#ff7f0e']  # Default matplotlib colors
for i, party in enumerate(['Democratic', 'Republican']):
    party_data = sp500_with_returns[sp500_with_returns['Party'] == party]['Daily_Return']
    plt.hist(party_data, bins=50, alpha=0.5, label=party, color=colors[i])
plt.title('Distribution of Daily Returns by Party', pad=15)
plt.xlabel('Daily Return')
plt.ylabel('Count')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
#%%
# Cell 5: Performance Analysis
# Copy everything below this line into your fifth code cell
#-----------------------------------------------------------
def calculate_performance_metrics(returns):
    """Calculate key performance metrics for a return series."""
    metrics = {
        'Daily Return (%)': returns.mean() * 100,
        'Daily Volatility (%)': returns.std() * 100,
        'Annualized Return (%)': returns.mean() * 252 * 100,
        'Annualized Volatility (%)': returns.std() * np.sqrt(252) * 100,
        'Sharpe Ratio': (returns.mean() * 252) / (returns.std() * np.sqrt(252)),
        'Positive Days (%)': (returns > 0).mean() * 100,
        'Maximum Drawdown (%)': ((1 + returns).cumprod().expanding().max() - 
                                (1 + returns).cumprod()).max() * 100
    }
    return pd.Series(metrics)

# Calculate metrics by party
party_metrics = sp500_with_returns.groupby('Party')['Daily_Return'].apply(calculate_performance_metrics)
print("Performance Metrics by Party:")
print(party_metrics.round(2))

# Plot cumulative returns with improved styling
plt.figure(figsize=(15, 8))
for i, party in enumerate(['Democratic', 'Republican']):
    party_data = sp500_with_returns[sp500_with_returns['Party'] == party]
    plt.plot(party_data['Date'], party_data['Cumulative_Return'] * 100, 
             label=party, color=colors[i], linewidth=2)

plt.title('Cumulative Returns by Party', pad=15)
plt.xlabel('Date')
plt.ylabel('Cumulative Return (%)')
plt.legend(frameon=True)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
#%%
# Cell 6: Statistical Tests
# Copy everything below this line into your sixth code cell
#-----------------------------------------------------------
# Perform t-test
dem_returns = sp500_with_returns[sp500_with_returns['Party'] == 'Democratic']['Daily_Return']
rep_returns = sp500_with_returns[sp500_with_returns['Party'] == 'Republican']['Daily_Return']

t_stat, p_value = stats.ttest_ind(dem_returns, rep_returns, equal_var=False)

print("Statistical Test Results:")
print(f"Democratic mean daily return: {dem_returns.mean()*100:.4f}%")
print(f"Republican mean daily return: {rep_returns.mean()*100:.4f}%")
print(f"Difference: {(dem_returns.mean() - rep_returns.mean())*100:.4f}%")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"\nInterpretation: {'Statistically significant' if p_value < 0.05 else 'Not statistically significant'} at 5% level")

# Regression analysis
X = sm.add_constant(sp500_with_returns['is_Democratic'])
model = sm.OLS(sp500_with_returns['Daily_Return'], X).fit()
print("\nRegression Analysis:")
print(model.summary().tables[1])
#%%
# Cell 7: Market State Analysis
# Copy everything below this line into your seventh code cell
#-----------------------------------------------------------
def analyze_market_states(df, threshold=0.2):
    """Identify and analyze bull/bear market states."""
    df = df.copy()
    df['Market_State'] = ''
    
    peak = df['Price'].iloc[0]
    trough = df['Price'].iloc[0]
    current_state = 'Unknown'
    
    for i in range(1, len(df)):
        price = df['Price'].iloc[i]
        
        if current_state in ['Unknown', 'Bull']:
            if price > peak:
                peak = price
            elif price < peak * (1 - threshold):
                current_state = 'Bear'
                trough = price
        
        elif current_state == 'Bear':
            if price < trough:
                trough = price
            elif price > trough * (1 + threshold):
                current_state = 'Bull'
                peak = price
        
        df.loc[i, 'Market_State'] = current_state
    
    return df

# Analyze market states
sp500_with_states = analyze_market_states(sp500_with_returns)
market_state_dist = pd.crosstab(
    sp500_with_states['Party'],
    sp500_with_states['Market_State'],
    normalize='index'
) * 100

print("Market State Distribution by Party (%):")
print(market_state_dist.round(2))

# Plot market states distribution with improved styling
plt.figure(figsize=(10, 6))
ax = market_state_dist.plot(kind='bar', stacked=True, width=0.8)
plt.title('Distribution of Market States by Party', pad=15)
plt.xlabel('Party')
plt.ylabel('Percentage of Days')
plt.legend(title='Market State', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3, axis='y')  # Grid lines only on y-axis for bar charts
plt.tight_layout()
plt.show() 