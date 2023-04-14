# Milestone 6 

## Introduction: 

Having come from football playing countries, the three of us have always watched the sport and grown into enthusiasts. Due to this common liking for football, we chose to team up for our data project and dig deeper to work on questions we have always been curious about. It is closely followed and the slightest changes make a difference in team and player valuations. To discover connections between factors and lower the related risk and ambiguity when concluding deals, data analysis is extremely important. In our project we tried to find out correlations between a player's performance of xG and xA (expected assists) to actual results of the matches. We also identified players who performed better or worse than average as well as their overall efficiency thanks to our study's ability to compare xG to actual goals scored and xA to actual assists. Finally, we also compared G to xG, A to xA, xG to xG per 90, and xA as extra criteria.


## Exploratory Data Analysis 

In our exploratory data analysis, we explored correlations between several variables which we have defined below. 
Variables:
- G = the number of goals players actually score throughout the season.
- xG = the number of goals that a player is expected to score based on the chances he has received.
- G - xG = the difference shows how much the expectation deviates from reality.
- xG90 = expected Goals per 90 minutes
- A = the number of assists player earned throughout the season
- xA = the number of assists that a player is expected to earned based on his passes
- A - xA = the difference shows how much the expectation deviates from reality.
- xA90 = expected Assists per 90 minutes


![Plot 1](images/Dependency_(G&xG))

An important visualization from our EDA is the scatter plot showing dependency between xG and G. For this plot, we chose to use linear regression to analyze the dependency of the two variables and it turned out to have a linear result, which shows that actual goals are very much correlated to expected numbers and as one of the variables increases, the other will increase too. 

![Plot 2](images/xG90(filtered_outliers))

This is an interesting plot to analyze because it shows the Expected Goals per 90 minutes data for all the players who have played in the Premier League for the 2021-2022 season AFTER we’ve filtered outliers. The data seems pretty consistent which is far from what it was initially.


## Research Question 1: 

RQ: What is the correlation between G, xG, and G-xG? 

The correlation between G and xG shows how efficient players and teams were in converting their scoring chances into actual goals. If there is a positive correlation between the two variables then the players are efficiently meeting their target. On the other hand, if there is a weak or negative correlation, it could indicate that the player or team is struggling to convert their chances into goals. To find out the answer to this research question, we carried out exploratory data analysis and found that G and xG are very closely related. This is evident in the two plots provided below. 

![Plot 3](images/Pairplots_(G&xG)) 

From the plot above, it is evident that G and XG have a positive linear correlation as G increases when XG increases. Also, most data points for G-XG are clustered between -2.5 to 2.5, except a few outliers, and have little to no proportionality. This is because G and XG are similar and therefore have little difference.  


![Plot 4](images/Teams_G&xG) 

The second plot shows that teams that had many players meet their expected goals or over achieve finished higher in terms of the total number of goals and teams that had players with higher G and XG also finished higher in general. For example, Manchester City had several players who met their expected goals on the higher end and made the team accumulate more points. Liverpool, on the other hand, ended up second place because it had one of the highest scoring players and other players on the lower end who almost met their expected values. Even though these teams ended in top positions, they were expected to do slightly better. This is evident in the plot with the negative G-XG for the two teams. 

In conclusion, there is linear dependency between G and xG. If a player has high XG, chances are that his actual goals would also be high and the team of this player would also finish higher. Additionally, if the difference between G and xG is more than 0 then the player is said to have over achieved. If the difference is 0, then the player has just met their target. Finally, if the difference is negative, then the player has not quite met the target. 


## Research Question 2: 

The second research question that we were working with was about A, xA and xA-A i.e. finding correlation and coherency present in the datasheet about Assists, Expected Assists and the difference between them. What Assists dictate is the pass given to a player right before the goal. To elaborate, when a player shoots for a goal, the ball he receives from a pass from a different player acts as an assist for the game. Expected Assists are basically the expectations of a certain player in Assisting with the goal. The criteria (xA-A) gives us the insight about the overall performance of the player, if his performance was true to his data ( both real and expected), if he overachieved or underachieved at his criteria. If the value resulting from xA-A is 0, it means that his Assists and Expected Assists are true to his datasheet. If the value from xA-A is a positive integer, it means that he underachieved or underperformed in his criteria. But, if the value from xA-A is a negative integer, it means that he overachieved or over performed. From the overall Data Analysis, it was evidently clear that A and xA was pretty much similar. The real analytical data came from the difference of xA and A i.e. xA-A. 

![Plot5](images/Screenshot1)

The first diagram is a barplot of players vs A, xA and the difference between xA and A. We can see from the diagram that while the first and second bar plots follow a similar trend, however,  their differences can be noted significantly in the third bar plot which shows some under the bar graph data and over the bar graph data. The barplots which go over means that the difference of xA and A is positive which further denotes that the player has underperformed. Similarly the bar plots which go under means that the difference of xA and A is negative which further denotes that the player has overperformed.

![Plot6](images/Screenshot2)

The Second diagram is where we further justify our data analytics. We can see how the overachievement or underachievement of players in their respective teams has affected their team, as a whole. We can see that due to those performances of all the players, some of the teams were overachieving while some of the teams were underachieving. This further led to either the glory or demise of that specific team in that season.


## Research Question 3: 

My research question dives into the correlation between Expected Goals on a per 90 minute basis (xG90) and Expected Assists on a per 90 minute basis (xG90). The reason why I chose these two statistics to take a deeper analysis into is because the Expected metrics highlights a player’s performance based off of how many goals/assists they should have scored. This is calculated through the positions they put themselves into which is why this correlation particularly interests me because I want to see if based on a player’s positional play is there a correlation between the amount of goals a player is expected to score per game and the amount of assists a player is expected to earn per game. The reason why I’m choosing per 90 minute metrics to evaluate this data is because I want to assess the use of per 90 minute metrics to evaluate players and whether they are a reliable statistic to judge player performance. 

![Plot7](images/Boxplot_xG90&xA90) 

From this graph we can see that the Expected Goals per 90 minutes(xG90) statistic is dominated by outliers who performed 3-4x higher than other players. However, looking further into this statistic gives us an idea that these are players who haven’t had many appearances and are typically performing at this level in a very limited number of appearances which is why their statistic is so high on a per 90 minute metric. When we see these players typically don’t have many actual Goals it brings up a question about how reliable this metric is in order to judge a player. If we filter Outliers it brings up the question about using these kinds of statistics because oftentimes the best players are considered to be outliers. Expected Assists per 90 minutes (xA90) follows the same direction which we can see in the following BoxPlot.


![Plot8](images/Expected_xA90&xG90) 

From the plot above we can see the degree to which some players are skewing the data because of the nature of these per 90 minute metrics. The outliers are performing at an unrealistically higher rate than most players. These players as we’ve seen from the previous plot are outliers because of their low number of appearances.


## Summary: 

Overall, through this project we were able to find several relationships between variables related to football. We were able to figure out the expected values are not just randomly guessed numbers but very reliable figures that contribute to team and player valuations. Some of the key highlights from our project include: 
Players with high expected goals (xG) had a high number of actual goals (G) and their teams also finished in better positions.
It was evidently clear that A and xA were also pretty much similar to each other. 
The difference between xG and G and xA and A helped show if a player was underperforming or overachieving. 
It was evident that players who perform substantially in the xG90 and xA90 metrics are typically players who have a low number of appearances which makes it not the best statistic to judge player performance as it’s commendable for players to perform at a high level in more appearances and having low number of minutes shouldn’t positively affect the judgment of that player.





















