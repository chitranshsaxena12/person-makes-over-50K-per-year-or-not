from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler


app = Flask(__name__,template_folder = "template")
model = pickle.load(open("finalisedmodel.pickle","rb"))

@app.route("/",methods=["GET"])
def home_page():
    return render_template("index.html")

standard = StandardScaler()

@app.route("/predict",methods = ["POST"])
def predict_page():
    if request.method == "POST":
        age = int(request.form["age"])
        workclass = request.form["workclass"]
        if workclass == 'Private':
            workclass = 4
        elif workclass == 'Self-emp-not-inc':
            workclass = 6
        elif workclass == 'Local-gov':
            workclass =2
        elif workclass == "None":
            workclass = 0
        elif workclass == "State-gov":
            workclass = 7
        elif workclass == 'Self-emp-inc':
            workclass = 5
        elif workclass == 'Federal-gov':
            workclass = 1
        elif workclass == 'Without-pay':
            workclass = 8
        else: #Never - worked
            workclass = 3
        education = request.form["education"]
        if education == "HS-grad":
            education = 11
        elif education == "Some-college":
            education = 15
        elif education == "Bachelors":
            education = 9
        elif education == "Masters":
            education = 12
        elif education == "Assoc-voc":
            education = 8
        elif education == "11 th":
            education = 1
        elif education == "Assoc-acdm":
            education = 7
        elif education == " 10 th":
            education = 0
        elif education == "7th-8th":
            education = 5
        elif education == "Prof-school":
            education = 14
        elif education == "9 th":
            education = 6
        elif education == "12 th":
            education = 2
        elif education == "Doctorate":
            education = 10
        elif education == "5th-6th":
            education = 4
        elif education == "1st-4th":
            education = 3
        else: #Preschool
            education = 13
        education_num = int(request.form["education_num"])
        marital_status = request.form["marital_status"]
        if marital_status == "Married-civ-spouse":
            marital_status = 2
        elif marital_status == "Never-married":
            marital_status = 4
        elif marital_status == "Divorced":
            marital_status = 0
        elif marital_status == "Separated":
            marital_status = 5
        elif marital_status == "Widowed":
            marital_status = 6
        elif marital_status == "Married-spouse-absent":
            marital_status = 3
        else: #Married-AF-spouse
            marital_status = 1
        occupation = request.form["occupation"]
        if occupation == "Prof-specialty":
            occupation = 10
        elif occupation == "Craft-repair":
            occupation = 3
        elif occupation == "Exec-managerial":
            occupation = 4
        elif occupation == "Adm-clerical":
            occupation = 1
        elif occupation == "Sales":
            occupation = 12
        elif occupation == "Other-service":
            occupation = 8
        elif occupation == "Machine-op-inspct":
            occupation = 7
        elif occupation == "None":
            occupation = 0
        elif occupation == "Transport-moving":
            occupation = 14
        elif occupation == "Handlers-cleaners":
            occupation = 6
        elif occupation == "Farming-fishing":
            occupation = 5
        elif occupation == "Tech-support":
            occupation = 13
        elif occupation == "Protective-serv":
            occupation = 11
        elif occupation == "Priv-house-serv":
            occupation = 9
        else: #Armed-Forces
            occupation = 2
        relationship = request.form["relationship"]
        if relationship == "Husband":
            relationship = 0
        elif relationship == "Not-in-family":
            relationship = 1
        elif relationship == "Own-child":
            relationship = 3
        elif relationship == "Unmarried":
            relationship = 4
        elif relationship == "Wife":
            relationship = 5
        else: #Other-relative
            relationship = 2
        race = request.form["race"]
        if race == "White":
            race = 4
        elif race == "Black":
            race = 2
        elif race == "Asian-Pac-Islander":
            race = 1
        elif race == "Amer-Indian-Eskimo":
            race = 0
        else: #Other
            race = 3
        sex = request.form["sex"]
        if sex == "Male":
            sex = 1
        else: #"Female"
            sex = 0
        capital_gain = int(request.form["capital_gain"])
        capital_loss = int(request.form["capital_loss"])
        hours_per_week = int(request.form["hours_per_week"])
        native_country = request.form["native_country"]
        if native_country == "United-States":
            native_country = 39
        elif native_country == "Mexico":
            native_country = 26
        elif native_country == "None":
            native_country = 0
        elif native_country == "Philippines":
            native_country = 30
        elif native_country == "Germany":
            native_country = 11
        elif native_country == "Canada":
            native_country = 2
        elif native_country == "Puerto-Rico":
            native_country = 33
        elif native_country == "El-Salvador":
            native_country = 8
        elif native_country == "India":
            native_country = 19
        elif native_country == "Cuba":
            native_country = 5
        elif native_country == "England":
            native_country = 9
        elif native_country == "Jamaica":
            native_country = 23
        elif native_country == "South":
            native_country = 35
        elif native_country == "China":
            native_country = 3
        elif native_country == "Italy":
            native_country = 22
        elif native_country == "Dominican-Republic":
            native_country = 6
        elif native_country == "Vietnam":
            native_country = 40
        elif native_country == "Guatemala":
            native_country = 13
        elif native_country == "Japan":
            native_country = 24
        elif native_country == "Poland":
            native_country = 31
        elif native_country == "Columbia":
            native_country = 4
        elif native_country == "Taiwan":
            native_country = 36
        elif native_country == "Haiti":
            native_country = 14
        elif native_country == "Iran":
            native_country = 20
        elif native_country == "Portugal":
            native_country = 32
        elif native_country == "Nicaragua":
            native_country = 27
        elif native_country == "Peru":
            native_country = 29
        elif native_country == "France":
            native_country = 10
        elif native_country == "Greece":
            native_country = 12
        elif native_country == "Ecuador":
            native_country = 7
        elif native_country == "Ireland":
            native_country = 21
        elif native_country == "Hong":
             native_country = 17
        elif native_country == "Cambodia":
            native_country = 1
        elif native_country == "Trinadad&Tobago":
            native_country = 38
        elif native_country == "Laos":
            native_country = 25
        elif native_country == "Thailand":
            native_country = 37
        elif native_country == "Yugoslavia":
            native_country = 41
        elif native_country == "Outlying-US(Guam-USVI-etc)":
            native_country = 28
        elif native_country == "Honduras":
            native_country = 16
        elif native_country == "Hungary":
            native_country = 18
        elif native_country == "Scotland":
            native_country = 34
        else: #Holand-Netherlands
            native_country = 15


        prediction = model.predict([[age,workclass,education,education_num,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,native_country]])
        if prediction == 0:
            return render_template("result.html", prediction_result = "Person Makes over <=50K per year")
        else:
            return  render_template("result.html", prediction_result = "Person Makes over >50K per year")

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)























































































