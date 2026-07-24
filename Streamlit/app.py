import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df=pd.read_csv("D:\Cognetix_Internship\Cognetix_Covid_Analysis\data\Covid19_Data.csv")
df["Date"]=pd.to_datetime(df["Date"])
st.set_page_config(
    page_title="COVID-19 Dashboard",
    layout="wide"
)

st.title("🦠 COVID-19 Analysis Dashboard")
st.markdown("---")


# KPI Cards
latest = df[df["Date"] == df["Date"].max()]
total_confirmed = latest["Confirmed"].sum()
total_deaths = latest["Deaths"].sum()
total_recovered = latest["Recovered"].sum()
active_cases = total_confirmed - total_recovered - total_deaths
mortality_rate = (total_deaths/total_confirmed)*100
recovery_rate = (total_recovered/total_confirmed)*100

# Daily New Cases
india=df[df["Country/Region"]=="India"].copy()

india = india.sort_values("Date")

india["Daily Cases"] = india["Confirmed"].diff()

india["Daily Deaths"] = india["Deaths"].diff()

india["Daily Recovered"] = india["Recovered"].diff()

plt.figure(figsize=(15,6))

plt.plot(india["Date"], india["Daily Cases"])

plt.title("Daily New Cases")

st.pyplot(plt.gcf())
plt.clf()
#Rolling Average
india["Rolling Avg"] = india["Daily Cases"].rolling(7).mean()

#Daily Deaths
plt.figure(figsize=(14,6))

sns.lineplot(data=india,
             x="Date",
             y="Daily Deaths")

plt.title("Daily Deaths")

st.pyplot(plt.gcf())
plt.clf()

#Daily Recoveries
plt.figure(figsize=(14,6))

sns.lineplot(data=india,
             x="Date",
             y="Daily Recovered",
             color="green")

plt.title("Daily Recoveries")

st.pyplot(plt.gcf())
plt.clf()

#Top 10 Countries
latest = df[df["Date"]==df["Date"].max()]

top = latest.groupby("Country/Region")["Confirmed"].sum()

top = top.sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(x=top.values, y=top.index, ax=ax)
plt.title("Top 10 Countries")
st.pyplot(fig)

#Top 10 Deaths
top = latest.groupby("Country/Region")["Deaths"].sum()

top = top.sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(x=top.values, y=top.index, ax=ax)
plt.title("Top 10 Countries for Deaths")
st.pyplot(fig)

#Top 10 Recoveries
top = latest.groupby("Country/Region")["Recovered"].sum()

top = top.sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(x=top.values, y=top.index, ax=ax)
plt.title("Top 10 Countries for Recoveries")
st.pyplot(fig)

#Active Cases by Country
latest = latest.copy()
latest["Active"] = latest["Confirmed"] - latest["Recovered"] - latest["Deaths"]

top = latest.groupby("Country/Region")["Active"].sum().sort_values(ascending=False).head(10)

# World Map

import plotly.express as px

fig = px.choropleth(
    latest,
    locations="Country/Region",
    locationmode="country names",
    color="Confirmed",
    hover_name="Country/Region",
    color_continuous_scale="Reds",
    title="Worldwide Confirmed Cases"
)

st.plotly_chart(fig, use_container_width=True)

# Monthly Trend
df["Month"] = df["Date"].dt.strftime("%Y-%m")

india = df[df["Country/Region"]=="India"].copy()

monthly = india.groupby("Month")["Confirmed"].max()

fig, ax = plt.subplots(figsize=(15,6))
monthly.plot(ax=ax)

st.pyplot(fig)


#Weekly Trend
india["Week"] = india["Date"].dt.isocalendar().week
india["Daily Cases"] = india["Confirmed"].diff()
weekly = india.groupby("Week")["Daily Cases"].sum()
fig, ax = plt.subplots(figsize=(15,6))
weekly.plot(ax=ax)
plt.title("Weekly Trend")
st.pyplot(fig)


#Correlation Heatmap
fig, ax = plt.subplots(figsize=(8,6))

sns.heatmap(
    df[["Confirmed","Recovered","Deaths"]].corr(),
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)

# Distribution Pie Chart

top5 = latest.groupby("Country/Region")["Confirmed"].sum().sort_values(ascending=False).head(5)

fig, ax = plt.subplots(figsize=(8,8))

ax.pie(
    top5,
    labels=top5.index,
    autopct="%1.1f%%"
)

st.pyplot(fig)
# Scatter Plot

plt.figure(figsize=(10,7))

fig, ax = plt.subplots(figsize=(10,7))

sns.scatterplot(
    data=latest,
    x="Confirmed",
    y="Deaths",
    ax=ax
)

st.pyplot(fig)

# Histogram

plt.figure(figsize=(12,6))

fig, ax = plt.subplots(figsize=(12,6))

sns.histplot(
    latest["Confirmed"],
    bins=30,
    ax=ax
)

st.pyplot(fig)
# BoxPlot

fig, ax = plt.subplots()

sns.boxplot(
    x=latest["Confirmed"],
    ax=ax
)

st.pyplot(fig)

# Country Comparison
countries = st.multiselect(
    "Choose Countries",sorted(df["Country/Region"].unique()),default=["India","China"]
)

# Data Range Filter

start = st.date_input("Start Date")

end = st.date_input("End Date")

filtered = df[(df["Date"]>=pd.to_datetime(start)) & (df["Date"]<=pd.to_datetime(end))]

# Download Clean Data

st.download_button(
    "Download CSV",
    filtered.to_csv(index=False),
    file_name="covid.csv"
)

# Country Statistics Table

summary = latest.groupby("Country/Region")[["Confirmed","Deaths","Recovered"]].sum()

st.dataframe(summary)

# Growth Rate
india["Growth Rate"] = india["Confirmed"].pct_change()*100

# Recovery Rate

latest["Recovery Rate"] = latest["Recovered"]/latest["Confirmed"]*100

top = latest.sort_values("Recovery Rate", ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10,6))

sns.barplot(
    data=top,
    x="Recovery Rate",
    y="Country/Region",
    ax=ax
)

st.pyplot(fig)

# Mortality Rate

latest["Mortality Rate"] = latest["Deaths"]/latest["Confirmed"]*100
top = latest.sort_values("Mortality Rate", ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(
    data=top,
    x="Mortality Rate",
    y="Country/Region",
    ax=ax
)

st.pyplot(fig)

# Dashboard Theme

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Cases", f"{total_confirmed:,}")

with col2:
    st.metric("Deaths", f"{total_deaths:,}")

with col3:
    st.metric("Recovered", f"{total_recovered:,}")

