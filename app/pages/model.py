import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

st.title('Visuals of the OLS Model')
file1 = open("models\\model.pkl",'rb')
model = pickle.load(file1)
file1.close()
file2 = open("datasets\\newdf.pkl",'rb')
newdf = pickle.load(file2)
file2.close()

def main():
    options = list(model.params.reset_index()['index'])
    options.remove('Intercept')
    option1 = st.selectbox(
                "Chosen Attributes",
                options,
                index=0
                )

    plot = sns.residplot(x=option1, y='Power', data=newdf).set_title('Residuals Scatter Plot')
    plot2 = st.pyplot(fig=plot.get_figure())

    fig = plt.figure(figsize=(14, 8)) 
    fig = sm.graphics.plot_regress_exog(model, option1, fig=fig) 
    plot1 = st.pyplot(fig=fig, use_container_width=True)

if __name__ == '__main__':
    main()