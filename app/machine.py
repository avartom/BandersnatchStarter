from pandas import DataFrame
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

class Machine:


    def __init__(self, df: DataFrame):
        df = df.dropna()
        lst = []
        for x in df["claim"]:
            if x <=20000:
                lst.append(0)
            else:
                lst.append(1)
        self.name = "Random Forest Classifier"
        self.model = RandomForestClassifier()
        features = df.drop(columns=["claim"])
        target = lst
        le = LabelEncoder()
        features["gender"] = le.fit_transform(features["gender"])
        features["diabetic"] = le.fit_transform(features["diabetic"])
        features["smoker"] = le.fit_transform(features["smoker"])
        features["region"] = le.fit_transform(features["region"])
        self.model.fit(features, target)
    
    #def __call__(self,feature_basis: DataFrame):
        # prediction, *_ = self.model.predict(feature_basis)
        # return prediction
       

    def save(self, filepath):
        rfc = self.model
        joblib.dump(rfc, filepath)

    @staticmethod
    def open(filepath):
        return joblib.load(filepath)
        

    def info(self):
        return self.name
    
if __name__ == '__main__':

    import pandas as pd
    df = pd.read_csv("/Users/ara_vartomian/Downloads/insurance_data.csv")
    df.dropna(inplace=True)
    X_test = df.drop(columns=["PatientID", "index"])
    le = LabelEncoder()
    X_test["gender"] = le.fit_transform(X_test["gender"])
    print(le.inverse_transform([0,1]))
    X_test["diabetic"] = le.fit_transform(X_test["diabetic"])
    print(le.inverse_transform([0,1]))
    X_test["smoker"] = le.fit_transform(X_test["smoker"])
    print(le.inverse_transform([0,1]))
    # X_test["children"] = le.fit_transform(X_test["children"])
    X_test["region"] = le.fit_transform(X_test["region"])
    # machine = Machine(X_test)
    # machine.save("app/model.joblib")
    # machine = Machine.open("app/model.joblib")
    # prd = machine(X_test.iloc[:1])
    # X_test = X_test.drop(columns=["claim"])
    print(le.inverse_transform([0,1, 2 ,3]))