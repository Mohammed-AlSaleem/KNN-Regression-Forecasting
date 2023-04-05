# KNN-Regression-Forecasting
Math405: Learning From Data Project

Introduction:

The problem is to forecast the travel times between two places (points) which from point (0) Burrard st. to point (1) Highburry st. in the year 2020. The measurements time of the 2017, 2018, 2019 years are given.
The data we have are day order, the season in the year (1 to 3), the day of the week (1 to 6), the period of the day (1 to 4), and the travel time, but there are some measurement errors we need to deal with.


Literature review on KNN Regression:

KNN regression is a method that depends on the neighbor observations with independent variables to forecast future values. KNN regression considers as an intuitive manner, not a parametric method.
The number of neighbors which will be calculated represented by ‘k’, calculating the distance between neighbors can be done in many ways, the famous one is Minkowski distance. When the power parameter (p) equal to 2 it called “Euclidean Distance”, and when it equal to 1 it called “Manhattan Distance”. The distance has an inverse relationship with the weight of neighbors.
