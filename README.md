# NFL STATS
Tkinter application where you can retrieve team schedules, calculate elo rankings, and generate win probabilities and game spreads

## What is Elo?
Elo is a method of quantifying the relative skill of players in a game. It is best used for zero-sum games, such as chess. Those where you either win or lose, and there is no distinction of score. This is why its use for football is flawed and never really seen. So the creation of this project isn't to create the best possible method of predicting results or ranking teams, I just did it for fun. That being said, the reason why Elo is flawed for a game like football is because a 10-7 win counts the same as a 49-0 win for example. Elo only looks like the end result and does not account for how dominant or close a victory might be.

## How Elo is calculated in this project
First, we create and manage a dictionary where the keys are the abbreviations for team lookups on SportsReference and the values are the team objects themselves. The team objects are initally instantiated at 1500 Elo, and change according to the results in the timeframe specified.

As the program runs through each boxscore week by week and extracts game data, it notes the winners and losers of each game. When this is found, we can then apply the elo algorithm. Given a winner and loser of a particular game, we calculate the expected win probability of each team with:
```
def probability(self, team1elo, team2elo):
        return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (team1elo - team2elo) / 400))
```
Then we use this result and our k factor where k = 30 to determine the teams' elo ratings after the game.
Note: K factor is essentially the largest amount of elo a team can gain or lose in a single game, so if two teams with the same elo would result in the winner gaining k/2 elo. This means that the larger the k factor, the more impact each individual game will have on a team's total elo. 
Finally, the elo is calculated using this equation, where a winning result is a 1 and a losing result is a 0:
 elo = elo + K(actual result - predictedresult)
```
winner.elo = winner.elo + k * (1 - prob_winner)
loser.elo = loser.elo + k * (0 - prob_loser)
```



## Features
  * **Calculate Elo**
    - Provides the Elo Ratings calculated between the inputted years, accurate to the week, as well as writing them to an excel sheet where the yearly breakdown is seperated by sheets
    
  ![calc elo](https://i.gyazo.com/b5b998de275eac33dcffc990b4d7756c.png)
  ![excel sheet](https://i.gyazo.com/dd649ec54861d1a92716459e48ee8814.png)
  
  * **Generate Win Probabilites and Spreads**
    - Using the elo rankings that have been calculated, generate the win probabilities for each match in a certain week as well as the game spreads
   
   ![win prob and spreads](https://i.gyazo.com/ee29b88f5eb5f0a621302e84738736af.png)
  
  * **Retrieve Schedule**
    - Select team from dropdown menu and supply a year to search for. Returns the schedule for that year
   
   ![schedule](https://i.gyazo.com/44ed39f82690caa73a6cf2aeaddf2d3f.png)
    
  
  
