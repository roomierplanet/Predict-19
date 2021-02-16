import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

pd.set_option('mode.chained_assignment', None)

class Predictor:
    def __init__(self):
        self.input_date()
        self.predictor()

    def input_date(self):
        self.days = [[0]]
        inp = input("Enter date (dd-mm-yyyy): ")
        if len(inp) < 10:
            print("Invalid format")
        date1 = datetime.strptime(inp, "%d-%m-%Y")
        ref_time = '10-01-2021'
        date2 = datetime.strptime(ref_time, "%d-%m-%Y")
        no_days = (date1-date2).days
        self.days[0][0] = no_days

    def predictor(self):
        # import csv file
        df = pd.read_csv('country_vaccinations.csv')

        # cleanup
        df.dropna(subset=['total_vaccinations'], how='all')
        df_India = df[df['country'] == 'India']
        df_India.reset_index(inplace=True)
        df_India.head()
        for i in range(0, len(df_India)):
            df_India.loc[i, 'date'] = i
            df_India.loc[i, 'index'] = i

        #visualization of relationship
        '''
        plt.figure(figsize=(16, 8))
        plt.title('CoViD-19 Vaccinations - India')
        plt.plot(df_India['index'], df_India['total_vaccinations'])
        plt.show()
        '''

        # model
        from sklearn.linear_model import LinearRegression
        # from sklearn.tree import DecisionTreeClassifier
        from sklearn.model_selection import train_test_split
        X = df_India['date']
        y = df_India['total_vaccinations']
        X = X.values.reshape(-1, 1)
        model = LinearRegression()
        model.fit(X, y)
        prediction = model.predict(self.days)
        print(str(int(prediction[0])) + " vaccinations by that date")


app = Predictor()

