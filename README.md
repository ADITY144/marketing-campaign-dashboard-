# Marketing Campaign Performance Dashboard

## 📊 Overview
An end-to-end analytics project analyzing 200,000+ digital marketing 
campaign records to uncover channel performance, ROI trends, and 
engagement patterns — built with Python for data processing and 
Power BI for visualization.

## 🎯 Problem Statement
Marketing teams run campaigns across multiple channels without always 
having clear visibility into which channels and campaign types deliver 
the best return. This dashboard consolidates campaign data to surface 
performance trends and support budget/strategy decisions.

## 📁 Dataset
Marketing Campaign Performance Dataset (Kaggle) — 200,000 rows, 
covering Company, Campaign Type, Channel, Conversion Rate, Acquisition 
Cost, ROI, Engagement Score, Location, and Date across 2021.

## 🔧 Approach
1. **Data Cleaning (Python/Pandas):** Converted cost/duration fields 
   from text to numeric, extracted date features (month, quarter, 
   day of week), engineered KPIs (CTR%, Cost per Conversion, Engagement 
   Level, ROI Category)
2. **Data Modeling (Power BI):** Built DAX measures for aggregate KPIs 
   (Avg ROI, Overall CTR%, Total Conversions)
3. **Dashboard Design:** Interactive Power BI dashboard with KPI cards, 
   trend charts, geographic map, and drill-down tables

## 💡 Key Insights
- Ad spend peaked in August and October, dipping notably in February
- Campaigns in the "High" engagement bucket accounted for ~40% of all 
  campaigns
- ROI and CTR remained fairly consistent across channels, with spend 
  and conversions distributed evenly across campaign types

## 🛠️ Tools & Technologies
Python (Pandas) | Power BI | DAX | Data Modeling | Power Query

## 📸 Dashboard Preview
![Dashboard](images/dashboard_overview.png)

## 🚀 How to Run
1. Clone this repo
2. Run `scripts/01_data_cleaning.py` on the raw dataset to generate 
   the cleaned CSV
3. Open `dashboard marketing_dashboard.pbix` in Power BI Desktop
4. Point the data source to your cleaned CSV if needed, then refresh

## 📫 Connect
[LinkedIn](https://linkedin.com/in/aditya-tiwari-b53157256) | 
[GitHub](https://github.com/ADITY144)
