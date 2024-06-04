import streamlit as st
from st_pages import Page, show_pages
import pandas as pd
import altair as alt
import plotly.express as px

show_pages(
    [
        Page("app.py", "Data Visuals"),
        Page("pages/model.py", "OLS Model Visuals")
    ]
)

st.set_page_config(page_title="Car Dataset")

def main():
    st.title('Visuals of the Car Project')
    df = pd.read_csv('datasets\\complete_cars.csv')
    df = df.drop(columns=['Unnamed: 0','index'])
    options1 = ['Model', 'Body', 'Interval Wiper', 'Front Stabilizer', 'Rear Suspension', 'Front Suspension', 'Cylinders', 'Fuel Type',
               'Engine/motor Type', 'Drive Wheel', 'Transmission']
    options2 = ['4 Years Depreciation', 'Compression Ratio', 'Curb Weight',
        'Engine Capacity', 'Front Track Width', 'Fuel Costs', 'Height', 'Insurance', 'Length',
        'Maintenance', 'Max. Payload', 'Max. Permissible Mass', 'Motor Vehicle Tax', 'Power', 'Price', 'Road Tax',
        'Top Speed', 'Valves Per Cylinder', 'Wheelbase', 'Width']
    
    df = df.sort_values(by=["Production Start Group"])

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Number of Attributes", "Facet Graph by Years", "Body Boxplot", "Distribution Plot", "Plot Graph"])
    with tab1:
        option1 = st.selectbox(
            "Categorical Parameter",
            options1,
            index=0
            )
        frame = df[option1].str.get_dummies()
        fig1 = px.bar(frame.sum(), labels={"index": option1, "value":"count"})
        fig1.update_layout(showlegend=False, xaxis={'categoryorder':'total descending'})
        st.plotly_chart(fig1, use_container_width=True, theme="streamlit")
    with tab2:
        option2 = st.selectbox(
            "Numerical Parameter1",
            options2,
            index=0
            )
        fig2 = px.histogram(df, option2, facet_col="Production Start Group",
            color="Production Start Group",
            title="Counts of Education level per Age",
            height=1500,
            facet_col_wrap=1,
            facet_col_spacing=0.1)
        st.plotly_chart(fig2, use_container_width=True, theme="streamlit")
    with tab3:
        option3 = st.selectbox(
            "Numerical Parameter2",
            options2,
            index=0
            )
        fig3 = px.box(df, "Body", option3)
        st.plotly_chart(fig3, use_container_width=True, theme="streamlit")
    with tab4:
        option4 = st.selectbox(
            "Numerical Parameter3",
            options2,
            index=0
            )
        chart = alt.Chart(df).transform_density(option4, as_=[option4, 'density']).mark_area().encode(x=option4+":Q", y='density:Q')
        st.altair_chart(chart, theme="streamlit")
    with tab5:
        option5 = st.selectbox(
            "Option 1",
            options2,
            index=0
            )
        df = df.sort_values(["Production Start"])
        fig4 = px.line(df, x="Production Start", y=option5)
        st.plotly_chart(fig4, use_container_width=True, theme="streamlit")


if __name__ == '__main__':
    main()