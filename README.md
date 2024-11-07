
<h1>Introduction</h1>

<p>The dataset is taken from carguru dataset provided by:

https://www.kaggle.com/ananaymital/us-used-cars-dataset</p>

<p>Presented are 3 methods for cleaning data that get progressively more difficult with each iteration.</p> 

<p>The results should enable the availability of more features while retaining the maximum number of records, understanding that we will have fewer records.</p>

<hr>

<h1>Methodology</h1>
<p>Documentation within the Notebooks are in the form of comments</p>
<p>This analysis is based purely in Python 3.11.9 inside 3 Jupyter Notebooks:</p>
<ul>
<li><b>File 1 - </b>split_data_BRUTAL.ipynb</li>
<ul>
<li>IF a column has a missing value, DROP the column</li>
</ul>
<li><b>File 2 -</b> split_data_NORMAL.ipynb</li>
<ul>
<li>IF a clumn has more than 10% missing values, DROP the columns</li>
<li>DROP all rows with missing values</li>
</ul>
<li><b>File 3 - </b>split_data_IMPUTING.ipynb <b>-- WORK IN PROGRESS</b></li>
<ul>
<li>Understand each feature, Identify possible primary keys and problematic features</li>
<li>Create conceptual model of how data can be used and the reasons behind the decisions</li>
<li>Utilise Hot-Deck Imputation to reduce the amount of mising values</li>
<li>Apply all the steps in <b>File 2</b></li>
</ul>
</ul>

<h3>Step-by-step usage</h3>

<ul><li>1. Clone this repository</li>
<li>2. Place the csv file from kaggle in the same directory as the 3 ipynb files</li>
<li>3. Run file 1, 2 and 3</li>
<li>4. Check the results in 3 files xxx_results.csv -</li>  
<ul><li>1st row = # of columns</li>
<li>2nd row = # of rows</li></ul></ul>


<h3>Python modlues used are:</h3>
<ul>
<li>Pandas </li>
<li>Numpy</li>
<li>gc</li>
</ul>

<hr>

<div style="text-align: center;">
<h1>Results</h1>
</div>

<h4><b>REMEMBER -</b> My aim is to reduce the number of columns removed while retaining as many rows as possible</h4>

<ul><li><b><h4>Original Dataset contains:</h4></b></li>
<ul>
<li>66 Columns</li>
<li>3000040 Rows</li>
</ul>
</ul>

<ul><li><h4><b>File 1</b> Dataset contains:</h4></li>
<ul>
<li>17 Columns</li>
<li>3000040 Rows</li>
</ul>
</ul>

<ul><li><h4><b>File 2</b> Dataset contains:</h4></li>
<ul>
<li>42 Columns</li>
<li>2392242 Rows</li>
</ul>
</ul>

<ul><li><h4><b>File 3</b> Dataset contains:</h4></li>
<ul>
<li>xx Columns</li>
<li>xxxxxxx Rows</li>
</ul>
</ul>

<br>

<hr>

<div style="text-align: center;">
<h1>Decision Recommendations</h1>
</div>
<p>Unless it is mission critical, I recommend File 2 as the most productive route.</p>
<p>I come to this conclusion because of the time and industry-specific knowledge required to regain xx% seems unproductive if not needed.</p>

<hr>

<div style="text-align: center;">
<h1>Conclusion</h1>
</div>



<hr>
<hr>









Background





This analysis is based purely in Python 3.11.9 inside a Jupyter Notebook.

Modlues used are:

Pandas
Numpy
gc

Aim

file 1 - split_data_BRUTAL.ipynb
file 2 - split_data_NORMAL.ipynb
file 3 - split_data_BRUTAL.ipynb

OUTPUTS: BRUTAL_results.csv, NORMAL_results.csv, IMPUTE_results.csv
        1st row = # of columns
        2nd row = # of rows

Step-by-step usage

1. Clone this repository
2. Place the csv file from kaggle in the same directory as the 3 ipynb files
3. Run file 1, 2 and 3 

