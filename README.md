# Technique for Oder Preference by Similarity to Ideal Solution(TOPSIS) for multiple-criteria decision making (MCDM)

# TOPSIS
It is a method of compensatory aggregation that compares a set of alternatives by identifying weights for each criterion, normalising scores for each criterion and calculating the geometric distance between each alternative and the ideal alternative, which is the best score in each criterion. An assumption of TOPSIS is that the criteria are monotonically increasing or decreasing. Normalisation is usually required as the parameters or criteria are often of incongruous dimensions in multi-criteria problems. Compensatory methods such as TOPSIS allow trade-offs between criteria, where a poor result in one criterion can be negated by a good result in another criterion. This provides a more realistic form of modelling than non-compensatory methods, which include or exclude alternative solutions based on hard cut-offs.
[![License](https://img.shields.io/badge/license-MIT-brightgreen)]&nbsp;![Made with Love in India](https://madewithlove.org.in/badge.svg)
---
## INSTALLATION & USAGE
 **1. Now install the required package by running the following commands :-**
 ```bash
  pip install TOPSIS-Ritikkumar-101983054
 ```
 **3.Use the package by running the following commands :-**
 ```bash
  import TOPSIS_Ritikkumar_101983054 as ritik_TOPSIS
  ritik_TOPSIS.TOPSIS(inputFilePath,weightList,impactList,OutputFileName)
 ```
 - inputFilePath : is the location of input file
- weightList : this takes the input value of every parameter weights "0.1,0.2,0.3,0.4"
- impactList : this takes the +ve and -ve as input to take whether to maximize or minimize a parameter
- outputFileName : is the location of the csv file where u want to save it
 ---
 # EXAMPLE USAGE
  ```bash
  import TOPSIS_Ritikkumar_101983054 as ritik_TOPSIS
  ritik_TOPSIS.TOPSIS('./Input.csv',[0.25,0.25,0.25,0.25],['-', '+', '+', '+'],'Output.csv')
 ```
 ####  INPUT
 | Model 	| Corr 	| Rseq 	| RMSE 	| Accuracy 	|
|:-:	|:-:	|:-:	|:-:	|:-:	|
| M1 	| 250 	| 16 	| 12 	| 5 	|
| M2 	| 200 	| 16 	| 8 	| 3 	|
| M3 	| 300 	| 32 	| 16 	| 4 	|
| M4 	| 275 	| 32 	| 8 	| 4 	|
| M5 	| 225 	| 16 	| 16 	| 2 	|

#### OUTPUT
| Model 	| Corr 	| Rseq 	| RMSE 	| Accuracy 	| Topsis Score 	| Rank 	|
|:-:	|:-:	|:-:	|:-:	|:-:	|-	|-	|
| M1 	| 250 	| 16 	| 12 	| 5 	| 0.5254 	| 2 	|
| M2 	| 200 	| 16 	| 8 	| 3 	| 0.2641 	| 5 	|
| M3 	| 300 	| 32 	| 16 	| 4 	| 0.7358 	| 1 	|
| M4 	| 275 	| 32 	| 8 	| 4 	| 0.52082 	| 3 	|
| M5 	| 225 	| 16 	| 16 	| 2 	| 0.37274 	| 4 	|

 ---
## BUILT BY 🤝
 - [**Ritik Kumar**](https://github.com/ritik-sys)  
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)





