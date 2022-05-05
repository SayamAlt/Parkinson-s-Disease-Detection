#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


model = joblib.load('model.pkl')
model


# In[4]:


@app.route("/")
def home():
    return render_template('home.html')


# In[5]:


@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        shimmer = request.form["mdvp_shimmer"]
        apq = request.form["mdvp_apq"]
        spread1 = request.form["spread1"]
        spread2 = request.form["spread2"]
        ppe = request.form["ppe"]
        prediction = model.predict([[
            shimmer,
            apq,
            spread1,
            spread2,
            ppe
        ]])
        output = prediction[0]
        if output == 0:
            return render_template('home.html',prediction_text="The person with the given details is healthy and immune to the Parkinson's disease.")
        else:
            return render_template('home.html',prediction_text="The person with these details is highly vulnerable to getting affected by Parkinson's disease.")


# In[ ]:


if __name__ == "__main__":
    app.run(port=8080)

