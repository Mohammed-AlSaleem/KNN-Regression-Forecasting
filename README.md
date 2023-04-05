# KNN-Regression-Forecasting
Math405: Learning From Data Project

## Introduction:

The problem is to forecast the travel times between two places (points) which from point (0) Burrard st. to point (1) Highburry st. in the year 2020. The measurements time of the 2017, 2018, 2019 years are given.
The data we have are day order, the season in the year (1 to 3), the day of the week (1 to 6), the period of the day (1 to 4), and the travel time, but there are some measurement errors we need to deal with.


## Mathematical Methodology for KNN Regression:

The first step is calculating the distance between our point (the day and the period with all features) and nearest k neighbors, in this project Manhattan distance is used (Minkowski distance with p = 1) which is the distance between the real vectors of features calculated by the sum of their absolute difference.

After calculating the distances with the nearest k neighbors, we calculate the weighted average of their corresponding times and assign it as the time of our point.

