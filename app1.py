import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('model_pkl.pkl','rb'))


def main():
  st.sidebar.header("Diabetes Risk Prediction for patient with the datset")
  st.sidebar.text("This a Web app that tells you if you are a diabetes whether you are at risk for Diabetes or not.")
  st.sidebar.header("Just fill in the information below")
  st.sidebar.text("The SVM Classifier was used.")


  id = st.text("id", "Type Here")
  cholesterol = st.text("Cholesterol", "Type Here")
  gluc = st.text("gluc", "Type Here")
  smoke = st.text("smoke", "Type Here")
  alco = st.text("alco", "Type Here")
  active = st.text("active", "Type Here")
  pressure = st.text("pressure", "Type Here")
  age1 = st.text("age1", "Type Here")
  height= st.text("height", "Type Here")
  weight = st.text("weight", "Type Here")
  gender = st.text("gender", "Type Here")

  inputs = [[id,cholesterol, gluc,smoke, alco, active, pressure, age1,height,weight,gender]]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(float)
    if updated_res == 0:
       st.write("Not very Proabable you will get Diabetes soon but still take good care of yourself regardless")
    else:
       st.write("It is Probable you might get a Diabetes soon therfore you should take better care of yourself")
   


if __name__ =='__main__':
  main()