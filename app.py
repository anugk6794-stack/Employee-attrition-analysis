import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")
st.title("2. Employee Attrition Analytics - Anu GK")
st.caption("IBM HR 1470 employees | Early 29.8% attrition is key insight")
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
df['Tenure_Band']=pd.cut(df['YearsAtCompany'], bins=[-1,2,5,10,40], labels=['0-2 Early','3-5 Mid','6-10 Long','10+ Vet'])
early = len(df[(df['YearsAtCompany']<=2)&(df['Attrition']=='Yes')])/len(df[df['YearsAtCompany']<=2])*100
c1,c2,c3,c4=st.columns(4)
c1.metric("Total", len(df))
c2.metric("Left", len(df[df['Attrition']=='Yes']))
c3.metric("Rate", f"{len(df[df['Attrition']=='Yes'])/len(df)*100:.1f}%")
c4.metric("Early 0-2", f"{early:.1f}%")
st.divider()
st.plotly_chart(px.histogram(df, x="Department", color="Attrition", barmode="group", title="Step3: Dept vs Attrition"), use_container_width=True)
st.plotly_chart(px.histogram(df, x="Tenure_Band", color="Attrition", barmode="group", title="Step4: Tenure Band 29.8% Early Risk"), use_container_width=True)
st.plotly_chart(px.histogram(df, x="OverTime", color="Attrition", barmode="group", title="Workload: OverTime vs Attrition"), use_container_width=True)
st.plotly_chart(px.box(df, x="Attrition", y="MonthlyIncome", color="Attrition", title="Compensation vs Attrition"), use_container_width=True)
st.success("Strongest Pattern: Early 29.8% leave + OverTime risk | Action: Mentorship, Hire more")
st.dataframe(df.head(30))
