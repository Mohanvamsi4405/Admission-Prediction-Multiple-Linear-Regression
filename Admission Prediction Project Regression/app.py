
# # # # importing the necessary dependencies
# # import pickle
# # import logging
# # from flask import Flask, render_template, request
# # from flask_cors import cross_origin
# # from sklearn.preprocessing import StandardScaler
# # app = Flask(__name__) # initializing a flask app

# # @app.route('/',methods=['GET'])  # route to display the home page
# # @cross_origin()
# # def homePage():
# #     return render_template("index.html")

# # @app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
# # @cross_origin()
# # def index():
# #     if request.method == 'POST':
# #         try:
# #             #  reading the inputs given by the user
# #             st=StandardScaler()
            
# #             gre_score=float(request.form['gre_score'])
# #             toefl_score = float(request.form['toefl_score'])
# #             university_rating = float(request.form['university_rating'])
# #             sop = float(request.form['sop'])
# #             lor = float(request.form['lor'])
# #             cgpa = float(request.form['cgpa'])
# #             is_research = request.form['research']
# #             if(is_research=='yes'):
# #                 research=1
# #             else:
# #                 research=0
        
# #             # filename = 'Admission_Model.pickle'
# #             loaded_model = pickle.load(open("Admission_Model.pickle", 'rb')) # loading the model file from the storage
# #             # predictions using the loaded model file
# #             print("File reading")
           
# #             prediction=loaded_model.predict(st.transform([[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]]))
# #             print('prediction is', prediction)
# #             # showing the prediction results in a UI
# #             return render_template('results.html',int(prediction*100))
        
# #         except Exception as e:
# #             # return render_template('results.html',prediction=round(100*prediction[0]))
# #             # print('The Exception message is: ',e)
# #             # return render_template('results.html')
# #             # print("Error")
# #             "Good"
# #             return render_template('results.html',int(prediction*100))

# #             # return 'something is wrong'
# #     else:
# #         return render_template('index.html')



# # if __name__ == "__main__":
# #     #app.run(host='127.0.0.1', port=8001, debug=True)
# # 	app.run(debug=True) # running the app
# import pickle
# import logging
# from flask import Flask, render_template, request
# from flask_cors import cross_origin
# from sklearn.preprocessing import StandardScaler
# import sklearn.preprocessing import  
# app = Flask(__name__)  # initializing a flask app

# @app.route('/', methods=['GET'])  # route to display the home page
# @cross_origin()
# def homePage():
#     return render_template("index.html")

# @app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
# @cross_origin()
# def predict():
#     if request.method == 'POST':
#         try:
#             # Reading the inputs given by the user
#             gre_score = float(request.form['gre_score'])
#             toefl_score = float(request.form['toefl_score'])
#             university_rating = float(request.form['university_rating'])
#             sop = float(request.form['sop'])
#             lor = float(request.form['lor'])
#             cgpa = float(request.form['cgpa'])
#             is_research = request.form['research']
#             research = 1 if is_research == 'yes' else 0

#             # Load the model and scaler
#             loaded_model = pickle.load(open("Admission_Model.pickle", 'rb'))
#             # scaler = pickle.load(open("StandardScaler.pickle", 'rb'))  # Assuming you have a scaler file

#             # Transform the input data
#             input_data = [[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]]
#             scaled_data = scaler.transform(input_data)

#             # Predict using the loaded model
#             prediction = loaded_model.predict(scaled_data)
#             prediction_percentage = round(prediction[0] * 100)

#             # Show the prediction results in a UI
#             return render_template('results.html', prediction=prediction_percentage)
        
#         except Exception as e:
#             logging.error(f"Error: {e}")
#             return render_template('results.html', prediction="Error in processing your request.")
    
#     else:
#         return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)  # running the app
import pickle
import logging
from flask import Flask, render_template, request
from flask_cors import cross_origin

app = Flask(__name__)  # initializing a flask app

@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def predict():
    if request.method == 'POST':
        try:
            # Reading the inputs given by the user
            gre_score = float(request.form['gre_score'])
            toefl_score = float(request.form['toefl_score'])
            university_rating = float(request.form['university_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            is_research = request.form['research']
            research = 1 if is_research == 'yes' else 0

            # Load the model
            loaded_model = pickle.load(open("Admission_Model.pickle", 'rb'))

            # Predict using the loaded model
            input_data = [[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]]
            prediction = loaded_model.predict(input_data)
            prediction_percentage = round(prediction[0]*10)

            # Show the prediction results in a UI
            return render_template('results.html', prediction=prediction_percentage)
        
        except Exception as e:
            logging.error(f"Error: {e}")
            return render_template('results.html', prediction="Error in processing your request.")
    
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)  # running the app
