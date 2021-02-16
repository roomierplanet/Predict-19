# Predict-19
Program to produce an estimated number of cumulative COVID-19 vaccinations in India by date provided by user.

Libraries Used:
1) Matplotlib
2) Pandas
3) NumPy
4) Datetime
5) Sklearn

Working:
1) Firstly, a data-set for worldwide COVID-19 vaccination was retrieved from Kaggle. The data was then filtered to find the vaccinations data for India in particular.
2) A plot of date v/s total_vaccinations was done to identify the growth so far. Visualization points to a linear pattern.
3) Cleanup performed on data to make it ready for reading by Linear Regression Model
4) X and y data-frames created from the total_vaccinations and date column of the file
5) Prediction Model written inside Prediction Class with an I/O module
6) I/O module enables user to input date in 'dd-mm-yyyy' format and then for the appropriate predictions to be made

Thank you for visitin the repo, hope you like it!

