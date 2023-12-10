import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#this app is taking linear regression equation from this paper 
#https://www.vurup.sk/wp-content/uploads/dlm_uploads/2017/07/pc_3_2015_stratiev_354_0.pdf
#credit to them
#set the page headings
image=Image.open('MEGATLogo.png')

# Define the scale factor
scale_factor = 0.25  # Replace with the desired scale factor

# Calculate the new dimensions based on the scale factor
new_width = int(image.width * scale_factor)
new_height = int(image.height * scale_factor)

# Resize the image
resized_image = image.resize((new_width, new_height))

st.image(resized_image)
st.title("MEGAT ASTM Conversion")
st.write("""ASTM D1160 Conversion to TBP using Linear 
         Regression model proposed by 
         https://www.vurup.sk/wp-content/uploads/dlm_uploads/2017/07/pc_3_2015_stratiev_354_0.pdf """)

#set the boundaries
col1,col2=st.columns(2)

#now we have to set input
with col1:
    X5 = float(st.number_input('5% wt'))
    X10 = float(st.number_input('10% wt'))
    X20 = float(st.number_input('20% wt'))
    X30 = float(st.number_input('30% wt'))
    X40 = float(st.number_input('40% wt'))
    X50 = float(st.number_input('50% wt'))
    X60 = float(st.number_input('60% wt'))
    X70 = float(st.number_input('70% wt'))
    X80 = float(st.number_input('80% wt'))
    X90 = float(st.number_input('90% wt'))
    X95 = float(st.number_input('95% wt'))

button = st.button('Convert all')
if button:
    Y5 = 123.819 + 0.65472 * (X5)
    Y10 = 76.292 + 0.7834 * (X10)
    Y20 = 14.751 + 0.9507 * (X20)
    Y30 = -0.2458 + 0.9966 * (X30)
    Y40 = 35.959 + 0.9272 * (X40)
    Y50 = -0.2302 + 1.0059 * (X50)
    Y60 = -5.17605 + 1.01565 * (X60)
    Y70 = -11.0791 + 1.03811 * (X70)
    Y80 = -13.9023 + 1.05086 * (X80)
    Y90 = -16.44 + 1.065998 * (X90)
    Y95 = 7.70 + 1.00225946 * (X95)

    a = ["5%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "95%"]
    b = [X5, X10, X20, X30, X40, X50, X60, X70, X80, X90, X95]
    c = [Y5, Y10, Y20, Y30, Y40, Y50, Y60, Y70, Y80, Y90, Y95]

    df = pd.DataFrame({'wt%': a, 'ASTM D1160': b, 'TBP': c})

    # Set 'wt%' as the index for better plotting
    df.set_index('wt%', inplace=True)
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(kind='line', ax=ax)
    plt.xlabel('wt%')
    plt.ylabel('Values')
    plt.title('Plot of TBP vs ASTM D1160')
    plt.legend(title='Columns', loc='upper left')

    with col2:
        st.write(df)
        st.pyplot(fig)

        csv = df.to_csv(index=False).encode('utf-8')

        st.download_button("Press to Download",csv,"ASTMTBP.csv","text/csv",key='download-csv')


