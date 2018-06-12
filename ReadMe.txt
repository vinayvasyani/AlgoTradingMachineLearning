This is still under development. The scripts download stock history quotes from NSE India exchange using Yahoo Finance, puts in MySQL db and performs algo trading and machine learning. 
Will update with time..Its Work in progress!



=====================================================================================
We will build a model on nifty index over its monthly returns. 
Every first of month we will decide to go long or short on nifty. 
For each month we will build a signal number that will be between -3 to 3. 
Plus meaning go long, negative is short and the magnitude will indicate the size of position we want to take

Step 1: Take  Nifty data. 
Step 2: Calculate the daily returns. 
Step 3: Calculate daily log returns. I.e log(1+ returns)…this  helps taking the sum of returns. 
Step 4: Momentum = Sum of Returns / Standard Deviation. …over say last 75 days. 
We take out the daily prices and replace with the monthly  prices. 
Step 5. We build a signal measure from Z-score between -3 and +3. 
Z-score or signal = Average Momentum - Momentum DataPoint / Standard Dev of momentum series. 
i.e we will have z-score over the momentum of 75 day prices ending on the day previous to that month. 
However since we are developing strategy over monthly returns, we have included 30 days extra data of the last month. 
Thus we shift the Momentum calculations one cell up in the excel. 

Step 6: Get Momentum returns as MomSignal * MomZscore. 

Step 7: Get the sharpe ratio over the momentum = Sqrt(12) * Returns / Std Dev of momentum

Step 8: On this momentum only stategy we will find sharpe ratio is -0.39% for the 2016 data. 
So we try and build Jump factor of mean reversion which is valuaiton strategy 
Jump factor =zscore over the recent average / long term average. 
Jump factor = Averegae of last 2 month returns - Avg of last 2year returns/Std dev. Of last 2 years. 
We bet on reverse direction of Jump. 
We will get 1.29 sharpe ration that’s better.


Step 9: Could use weighted average on Jump and Momentum signal. 

