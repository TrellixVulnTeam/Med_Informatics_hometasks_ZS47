import pandas as pd
from sklearn import linear_model
from sklearn.feature_selection import RFE
from itertools import compress


def get_df(path):
    df = pd.read_excel(path)
    return df


if __name__ == '__main__':
    df = get_df('C:\\Amanturs new\\study\\1sem\\1half\\med informatics\\HW4\\DataOnly\\WaitData.Published.xlsx')

    Y = df['Wait']
    X = df.drop(['Wait', 'x_ScheduledDTTM', 'x_ArrivalDTTM', 'x_BeginDTTM'], 1)
    # model = linear_model.LinearRegression()

    for column in X:
        print(column)
        X_iter = X[column].copy()
        # model.fit(X_iter, Y)
        # Ypred = model.predict(X_iter)  # use trained regression model to predict
        #
        # r = Y - Ypred  # compute prediction error (residual)
        # e = abs(r).mean()  # compute model error
        # print(column, e)

    # Second task
    # if True:  # just in case I want to disable this part
    #     print('\n>Python feature selection:')
    #
    #     for nFeatures in range(1, 5):
    #         rfe = RFE(model, n_features_to_select=nFeatures)
    #         X_rfe = rfe.fit_transform(X, Y)  # transforming data using RFE
    #         # Fitting the data to model
    #         model.fit(X_rfe, Y)
    #         # print(rfe.support_)
    #         # print(rfe.ranking_)
    #         cols = list(compress(X.columns, rfe.support_))
    #         model.fit(X[cols], Y)
    #         e = abs(Y - model.predict(X[cols])).mean()
    #         print(e, cols)