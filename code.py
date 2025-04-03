# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Set the path to the file you'd like to load
file_path = ""

# Load the latest version of the dataset
data = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "arindamsahoo/icc-mens-t20-world-cup-2024-stats",
  file_path,
)

print("First 5 records:", data.head())

# Sample Data Processing
team_wins = data.groupby('winner')['match_id'].count().reset_index()
team_wins.columns = ['Team', 'Wins']

# Visualization - Team Wins
plt.figure(figsize=(12,6))
plt.bar(team_wins['Team'], team_wins['Wins'], color='blue')
plt.xlabel('Teams')
plt.ylabel('Number of Wins')
plt.title('T20 World Cup Team Wins')
plt.xticks(rotation=45)
plt.savefig('team_wins.png')
plt.show()

# Top Run Scorers
top_scorers = data.groupby('top_scorer')['runs'].sum().reset_index().sort_values(by='runs', ascending=False).head(10)

plt.figure(figsize=(12,6))
plt.bar(top_scorers['top_scorer'], top_scorers['runs'], color='green')
plt.xlabel('Players')
plt.ylabel('Total Runs')
plt.title('Top 10 Run Scorers in T20 World Cup')
plt.xticks(rotation=45)
plt.savefig('top_scorers.png')
plt.show()

# Best Bowling Figures
best_bowlers = data.groupby('best_bowler')['wickets'].sum().reset_index().sort_values(by='wickets', ascending=False).head(10)

plt.figure(figsize=(12,6))
plt.bar(best_bowlers['best_bowler'], best_bowlers['wickets'], color='red')
plt.xlabel('Players')
plt.ylabel('Total Wickets')
plt.title('Top 10 Wicket Takers in T20 World Cup')
plt.xticks(rotation=45)
plt.savefig('top_bowlers.png')
plt.show()

# Team-wise Average Strike Rate
strike_rate = data.groupby('team')['strike_rate'].mean().reset_index().sort_values(by='strike_rate', ascending=False)
plt.figure(figsize=(12,6))
sns.barplot(x='strike_rate', y='team', data=strike_rate, palette='coolwarm')
plt.xlabel('Average Strike Rate')
plt.ylabel('Team')
plt.title('Team-wise Average Strike Rate')
plt.savefig('team_strike_rate.png')
plt.show()

# Toss Decision Analysis
toss_decision = data.groupby('toss_decision')['match_id'].count().reset_index()
toss_decision.columns = ['Toss Decision', 'Matches']
plt.figure(figsize=(8,6))
plt.pie(toss_decision['Matches'], labels=toss_decision['Toss Decision'], autopct='%1.1f%%', colors=['gold', 'lightblue'])
plt.title('Toss Decision Analysis')
plt.savefig('toss_decision.png')
plt.show()

# Runs Distribution
plt.figure(figsize=(12,6))
sns.histplot(data['runs'], bins=30, kde=True, color='purple')
plt.xlabel('Runs Scored')
plt.ylabel('Frequency')
plt.title('Runs Distribution in T20 World Cup')
plt.savefig('runs_distribution.png')
plt.show()

# Create a Dream 11 Team
# Selecting players based on top scorers, best bowlers, and random picks
batsmen = list(top_scorers['top_scorer'].head(4))
bowlers = list(best_bowlers['best_bowler'].head(4))
all_rounders = list(data[data['role'] == 'All-Rounder'].nlargest(2, 'runs')['player_name'])
wicket_keeper = list(data[data['role'] == 'Wicket-Keeper'].nlargest(1, 'runs')['player_name'])

# Combining into a final Dream 11 Team
dream_11_team = batsmen + bowlers + all_rounders + wicket_keeper
random.shuffle(dream_11_team)

print("Dream 11 Team:")
for i, player in enumerate(dream_11_team, 1):
    print(f"{i}. {player}")
