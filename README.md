# Dew-point-and-pitching

This project was a part of a take home project for the [Cincinnati reds](https://www.mlb.com/reds). The goal of this take home is to evaluate my methodology when working with a dataset.

Table of contents
|Section|
|-------|
|[Backgound](#Background)|
|[Problem_Statement](#Problem_Statement)|
|[EDA](#EDA)|
|[Modeling_and_Evaluations](#Modeling_and_Evaluations)|

## Background:

The reds have provided a dataset to determine if weather has an impact on a baseball pitch. The assessment wants to identify humidity via dew point's affect of a pitch and pitcher's comfortability. 

## Problem_Statement:

The goal is to identify the affects of dew point on pitches in temperatures greater than 65 fahrenheit. All work can be found in this [notebook](./Code/Notebook.ipynb)

## EDA

For our EDA process we look at our data dictionary located in [here](./Orignal_files/Dew_Point_and_Pitching.pdf) we examined our dataset and found it is mostly clean. Every column except EVENT_RESULT_KEY had 9889 rows while EVENT_RESULT_KEY had 2631 rows. After examining the columns we concluded that this is an expected result due to that column tracking play ending events, so that would have fewer entries than the rest.

After looking at the descriptions of the columns, I made an assumption that vertical and horizontal break would be the features of interest. I believe I can use these columns to calculate the difference between a pitch in a vaccum and a pitch with environmental factors. Looking at the pitches I noticed Induced Vertical Break had a left skewed distribution while Horizontal break had a bi-modal distribution.

After looking at the distributions I began looking at correlations between specific features. Ultimately I chose continuous variable and plotted the correlation and distribution via a joint plot.

## Modeling_and_Evaluations

The next step was to build two logistic regression models, One with a break feature and one without to feed into an ensemble model to determine the influence of dew point on a pitch. I wanted to calculate how much of a degree drop was caused by dew point. However, I didn't have the domain knowledge to properly created a binary column for dew point over 65 degrees to get my probabilities.
