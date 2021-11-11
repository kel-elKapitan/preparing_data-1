# preparing_data-1
# Background

Presented is an analysis of __Used Car Sales from 2016/2017 from cargugu database__ provided by https://www.kaggle.com/ananaymital/us-used-cars-dataset.

This analysis covers __retieving data from a csv file, computation and data manipulation.__

This analysis is based purely in Python

It uses <i>Pandas and Numpy</i> for data manipulation and computation, <i>matplotlib and seaborn</i> for visualisations.

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
###### Continuous Variables
front_legroom - inches
back_legroom - inches
fuel_tank_volume - gallons
height - inches
length - inches
maximum_seating - seats
wheelbase - inches
width - inches
power_rpm - rpm's
torque_rpm - rpm's
power_hp - horsepower
torque_lb-ft - lb's per foot

###### Categorical Variables
body_type
city
engine_cylinders
engine_type
exterior_color
fuel_type
interior_color
listing_color
make_name
model_name
sp_name
transmission
transmission_display
trimId
trim_name
wheel_system
wheel_system_display
