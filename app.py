import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻",
                   layout="wide")

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor 💻")




# making 2 cols left_column and right_column=                       1st row
left_column, right_column = st.columns(2)
# 1st row
with left_column:
    # brand input
    company = st.selectbox("Brand", df["Company"].unique())

with right_column:
    # type of laptop
    type = st.selectbox('Type',df['TypeName'].unique())

   
  
  
# making 2 cols left_column and right_column=                       2nd row
left_column, right_column = st.columns(2)
# 2nd row
with left_column:
    # Ram
    ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

with right_column:    
    # weight
    weight = st.number_input('Weight of the Laptop')




 
# making 3 cols left_column and right_column=                      3rd row
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # Touchscreen
    touchscreen = st.selectbox('Touchscreen',['No','Yes'])

with middle_column:
    # IPS
    ips = st.selectbox('IPS',['No','Yes'])
    
with right_column:
    # screen size
    screen_size = st.number_input('Screen Size')
    
    #if screen_size is not None:
    #else:
        #st.markdown("### Please Upload Both Images")




# making 3 cols left_column and right_column=                      4th row
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # screen size
    resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

with middle_column:
    #cpu
    cpu = st.selectbox('CPU',df['Cpu brand'].unique())

with right_column:
    #hdd
    hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])





# making 3 cols left_column, middle_column and right_column=        5th row
left_column, middle_column,  right_column = st.columns(3)
with left_column:
    #ssd
    ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

with middle_column:
    #gpu
    gpu = st.selectbox('GPU',df['Gpu brand'].unique())

with right_column:
    #os
    os = st.selectbox('OS',df['os'].unique())


# Predict Button=                                                  Last row

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0
        
    if screen_size == 0.0:
        st.markdown("### Please enter screen size")
    else:
        pass
      
    

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
   
   
      
      
    query = pd.DataFrame(np.array([[company, type, ram, weight, touchscreen, ips, ppi , cpu, hdd, ssd, gpu, os]]), columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'Ips', 'ppi', 'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'])

    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))

