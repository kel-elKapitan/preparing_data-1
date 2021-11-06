import pandas as pd
import matplotlib.pyplot as plt


'''

###############################################################
# Uncomment and Run only once to create sample of the dataset #
###############################################################
def get_data(i):


    raw_test = []
    print('Creating csv for ' + i + '...')
    # import samples of the dataset, all vehicles split with the make_name column
    iter_csv = pd.read_csv('<path_to_dataset>/used_cars_data.csv', iterator=True, chunksize=500)
    raw = pd.concat([chunk[chunk['make_name'] == i] for chunk in iter_csv])
      
    raw.to_csv(i + '.csv')
    print(i + ' descriptive stats complete...')
        
    raw.describe().to_csv( i + '_Desc.csv')
        
          

        # print(len(raw_jeep()))

        # save the sample dataset into a csv for easy reference and as a checkpoint in the process

    print(i + '.csv saved')

    return

get_data('Jeep')

###################################################
# END of run once only - Recomment immediately ####
###################################################
'''


jeep = pd.read_csv('jeep.csv')

# save the shape of the data at the beginning so we can compare later
jeep_shape_beginning = jeep.shape

#########################
# Missing Values (start)# 
#########################

# check percentages of missing values in each variable
pd.set_option('display.max_rows', None)

a = jeep.isnull().sum()/len(jeep)*100

variables = jeep.columns
variable = []
# remove variables with more than 10% missing values
for i in range(0,len(variables)-1):
    if a[i] <=10: # set threshold to 10%
        variable.append(variables[i])
# Create dataframe with the reduced number of variables
jeep_slimmed = jeep[variable].copy(deep=True)

# drop any records that have any missing values left at this point
jeep_slimmed.dropna(inplace=True)

#######################
# Missing Values (end)# 
#######################

###################################################
# Reformat and cast datatypes of features (start) #  
###################################################

# split the values by the '@' and ' ' and put the 1st value in tuple back into variable
def split_me_space(n):
    mine_to_go = []
    for i in n:
        my_split = str(i).split(' ')
        mine_to_go.append(my_split[0])
    return mine_to_go

def split_me_at(n):
    mine_to_go = []
    for i in n:
        my_split = str(i).split('\@')
        mine_to_go.append(my_split[0])
    return mine_to_go

# split values from strings
jeep_slimmed['back_legroom'] = split_me_space(jeep_slimmed['back_legroom'])
jeep_slimmed['front_legroom'] = split_me_space(jeep_slimmed['front_legroom'])
jeep_slimmed['fuel_tank_volume'] = split_me_space(jeep_slimmed['fuel_tank_volume'])
jeep_slimmed['height'] = split_me_space(jeep_slimmed['height'])
jeep_slimmed['length'] = split_me_space(jeep_slimmed['length'])
jeep_slimmed['maximum_seating'] = split_me_space(jeep_slimmed['maximum_seating'])
jeep_slimmed['wheelbase'] = split_me_space(jeep_slimmed['wheelbase'])
jeep_slimmed['width'] = split_me_space(jeep_slimmed['width'])

# run through split_me_at and split_me_space
jeep_slimmed['power_hp'] = split_me_at(jeep_slimmed['power'])
jeep_slimmed['power_hp'] = split_me_space(jeep_slimmed['power_hp'])

jeep_slimmed['torque_lb-ft'] = split_me_at(jeep_slimmed['torque'])
jeep_slimmed['torque_lb-ft'] = split_me_space(jeep_slimmed['torque_lb-ft'])


# now we want the second value after the split

# split the power column into 2 values hp at rpm
my_rpm = []
for n in jeep_slimmed['power']:

    the_split = str(n).split('@')
    # print(the_split[0]) # we have already reformatted the power_hp variable
    #print(the_split[1])
    
    second_split = the_split[1].split(' ')
    my_rpm.append(second_split[1])    


# remove the comma in the numbers
the_rpm = []
for i in my_rpm:
    my_number = i.replace(',','')
    the_rpm.append(my_number)


# assign the_rpm integers into power_rpm variable
jeep_slimmed['power_rpm'] = the_rpm

# split the torque column into 2 values lb-ft at rpm
my_rpm2 = []
for n in jeep_slimmed['torque']:

    the_split = str(n).split('@')
    
    second_split = the_split[1].split(' ')
    my_rpm2.append(second_split[1])    


# remove the comma in the numbers
the_rpm2 = []
for i in my_rpm2:
    my_number = i.replace(',','')
    the_rpm2.append(my_number)


# assign the_rpm2 integers into power_rpm variable
jeep_slimmed['torque_rpm'] = the_rpm2

# remove odd characters in the dataset that prevents type casting
jeep_slimmed = jeep_slimmed[jeep_slimmed['back_legroom'] != '--']
jeep_slimmed = jeep_slimmed[jeep_slimmed['fuel_tank_volume'] != '--']

# Convert Datatypes that are not correct
jeep_slimmed['back_legroom'] = jeep_slimmed['back_legroom'].astype('float') # continuous variable
jeep_slimmed['vin'] = jeep_slimmed['vin'].astype('string') # ID Variable
jeep_slimmed['body_type'] = jeep_slimmed['body_type'].astype('category') # Categorical variable
jeep_slimmed['city'] = jeep_slimmed['city'].astype('category') # Categorical variable
jeep_slimmed['description'] = jeep_slimmed['description'].astype('string')
jeep_slimmed['engine_cylinders'] = jeep_slimmed['engine_cylinders'].astype('category') # Categorical variable
jeep_slimmed['engine_type'] = jeep_slimmed['engine_type'].astype('category') # Categorical variable
jeep_slimmed['exterior_color'] = jeep_slimmed['exterior_color'].astype('category') # Categorical variable
jeep_slimmed['front_legroom'] = jeep_slimmed['front_legroom'].astype('float') # continuous variable
jeep_slimmed['fuel_tank_volume'] = jeep_slimmed['fuel_tank_volume'].astype('float') # continuous variable
jeep_slimmed['fuel_type'] = jeep_slimmed['fuel_type'].astype('category') # categorical variable
jeep_slimmed['height'] = jeep_slimmed['height'].astype('float') # continuous variable
jeep_slimmed['interior_color'] = jeep_slimmed['interior_color'].astype('category') # categorical variable
jeep_slimmed['length'] = jeep_slimmed['length'].astype('float') # continuous variable
jeep_slimmed['listed_date'] = jeep_slimmed['listed_date'].astype('datetime64[s]') # continuous variable
jeep_slimmed['listing_color'] = jeep_slimmed['listing_color'].astype('category') # categorical variable
######## major_options is a list of options fitted to the vehicle, extra analysis of this variable is needed when I understand
jeep_slimmed['make_name'] = jeep_slimmed['make_name'].astype('category') # categorical variable
jeep_slimmed['maximum_seating'] = jeep_slimmed['maximum_seating'].astype('int64') # continuous variable
jeep_slimmed['model_name'] = jeep_slimmed['model_name'].astype('category') # categorical variable
jeep_slimmed['power_hp'] = jeep_slimmed['power_hp'].astype('int64') # continuous variable
jeep_slimmed['power_rpm'] = jeep_slimmed['power_rpm'].astype('int64') # continuous variable
jeep_slimmed['sp_name'] = jeep_slimmed['sp_name'].astype('category') # categorical variable
jeep_slimmed['torque_lb-ft'] = jeep_slimmed['torque_lb-ft'].astype('int64') # continuous variable
jeep_slimmed['torque_rpm'] = jeep_slimmed['torque_rpm'].astype('int64') # continuous variable
jeep_slimmed['transmission'] = jeep_slimmed['transmission'].astype('category') # categorical variable
jeep_slimmed['transmission_display'] = jeep_slimmed['transmission_display'].astype('category') # categorical variable
jeep_slimmed['trimId'] = jeep_slimmed['trimId'].astype('category') # categorical variable
jeep_slimmed['trim_name'] = jeep_slimmed['trim_name'].astype('category') # categorical variable, may need cleaning slightly as the strings do not seem to perfectly formatted
jeep_slimmed['wheel_system'] = jeep_slimmed['wheel_system'].astype('category') # categorical variable
jeep_slimmed['wheel_system_display'] = jeep_slimmed['wheel_system_display'].astype('category') # categorical variable
jeep_slimmed['wheelbase'] = jeep_slimmed['wheelbase'].astype('float') # continuous variable
jeep_slimmed['width'] = jeep_slimmed['width'].astype('float') # continuous variable

# remove the variables that were split for their information and are of no furthe use
del jeep_slimmed['power']
del jeep_slimmed['torque']

#################################################
# Reformat and cast datatypes of features (end) #  
#################################################

######################
# Data Check (start) # 
######################

# Check all datatypes are of the correct type
print('3. Final check to ensure no missing values and variables are of the correct type')
print(jeep_slimmed.dtypes)
print('\n\n')
print('Percentage of missing values in the dataset')
print(str(jeep_slimmed.isnull().sum()/len(jeep_slimmed)*100))
print('\n\n')
print('A little peek at the top of the dataset')
pd.set_option('display.max_rows', None)
print(jeep_slimmed.head())
print('\n\n')
print('The shape of the data at the beginning of the script')
print(jeep_shape_beginning)
print('\n\n')
print('The shape of the data after cleaning')
print(jeep_slimmed.shape)
print('\n\n')
removed_features = jeep_shape_beginning[1] - jeep_slimmed.shape[1]
removed_records = jeep_shape_beginning[0] - jeep_slimmed.shape[0]

print('Difference in the number of Features: ' + str(removed_features))
print('Difference in the number of Records: ' + str(removed_records))

####################
# Data Check (end) # 
####################

#################################################
# Distributions of continuous variables (start) #
#################################################

# page 1 of the subplots
fig, ax = plt.subplots(3,2 ,sharex= False, sharey=False)
fig.suptitle('Distributions from the raw dataset - Page 1')
plt.ylabel('Number of occurences')
ax[0][0].hist(jeep_slimmed['front_legroom'], bins=20)
ax[0][1].hist(jeep_slimmed['back_legroom'], bins=20)
ax[1][0].hist(jeep_slimmed['fuel_tank_volume'], bins=20)
ax[1][1].hist(jeep_slimmed['height'], bins=20)
ax[2][0].hist(jeep_slimmed['length'], bins=20)
ax[2][1].hist(jeep_slimmed['maximum_seating'], bins=20)

# set the labels of the subplots
ax[0, 0].set_title("Front Legroom")
ax[0, 0].set_xlabel("Inches")
ax[0, 0].set_xlim(40, 42)

ax[0, 1].set_title("Back Legroom")
ax[0, 1].set_xlabel("Inches")
ax[0, 1].set_xlim(33, 41)

ax[1, 0].set_title("Fuel Tank Volume")
ax[1, 0].set_xlabel("Gallons")
ax[1, 0].set_xlim(0, 25)

ax[1, 1].set_title("Height")
ax[1, 1].set_xlabel("Inches")

ax[2, 0].set_title("Length")
ax[2, 0].set_xlabel("Inches")

ax[2, 1].set_title("Maximum Seating")
ax[2, 1].set_xlabel("number of seats")
ax[2, 1].set_xlim(3, 6)

fig.tight_layout()

plt.savefig('distributions_p1.jpg')
plt.show()

# page 2 of the subplots
fig, ax = plt.subplots(3,2 ,sharex= False, sharey=False)
fig.suptitle('Distributions from the raw dataset - Page 2')
plt.ylabel('Number of occurences')
ax[0][0].hist(jeep_slimmed['wheelbase'], bins=20, density=True)
ax[0][1].hist(jeep_slimmed['width'], bins=20)
ax[1][0].hist(jeep_slimmed['power_rpm'], bins=20)
ax[1][1].hist(jeep_slimmed['torque_rpm'], bins=20)
ax[2][0].hist(jeep_slimmed['power_hp'], bins=20)
ax[2][1].hist(jeep_slimmed['torque_lb-ft'], bins=20)

# set the labels of the subplots
ax[0, 0].set_title("Wheelbase")
ax[0, 0].set_xlabel("Inches")

ax[0, 1].set_title("Width")
ax[0, 1].set_xlabel("Inches")

ax[1, 0].set_title("Power")
ax[1, 0].set_xlabel("rpm")

ax[1, 1].set_title("Torque")
ax[1, 1].set_xlabel("rpm")

ax[2, 0].set_title("Power")
ax[2, 0].set_xlabel("horspower")

ax[2, 1].set_title("torque")
ax[2, 1].set_xlabel("lb's per foot")

fig.tight_layout()

plt.savefig('distributions_p2.jpg')
plt.show()

###############################################
# Distributions of continuous variables (end) #
###############################################

print('Lets hope this data is clean enough to create models for the coming analyses')

jeep_slimmed.to_csv('jeep_prepped.csv')



