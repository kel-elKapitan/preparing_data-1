# preparing_data-1
# Background

Presented is an analysis of __Used Car Sales from 2016/2017 from cargugu database__ provided by https://www.kaggle.com/ananaymital/us-used-cars-dataset.

This analysis covers __retieving data__ from a csv file, __computation and data manipulation__ and __visualisation.__

This analysis is based purely in Python

It uses _Pandas_ and _Numpy_ for data manipulation and computation, _matplotlib_ and _seaborn_ for visualisations.

### Aim

To clean a sample of a dataset ready for creating models in statistical analysis and Machine Learning to predict the price of a vehicle made by Jeep

### Step by step usage
1. clone a copy of this repository
1. place the csv file downloaded from kaggle in the same directory as preparing_data.py
1. run __preparing_data.py__
1. OUTPUT: jeep_prepped.csv
1. OUTPUT: 2 pages of distibutions from continuous variables
1. OUTPUT: x pages of frequency plots from the categorical variables

### Data Dictionary
| Continuous Variables | Categorical Variables |
| ----------------- | ------------------- |
| - front_legroom - inches | - body_type | 
| - back_legroom - inches | - city |
| - fuel_tank_volume - gallons |  - engine_cylinders |
| - height - inches | - engine_type |
| - length - inches | - exterior_color |
| - maximum_seating - seats | - fuel_type |
| - wheelbase - inches | - interior_color |
| - width - inches | - listing_color |
| - power_rpm - rpm's | - make_name |
| - torque_rpm - rpm's | - model_name |
| - power_hp - horsepower | - sp_name |
| - torque_lb-ft - lb's per foot | - transmission |
| | - transmission_display |
| | - trimId |
| |- trim_name |
| |- wheel_system |
| |- wheel_system_display |
