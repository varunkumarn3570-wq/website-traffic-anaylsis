# Website Traffic & Revenue Analytics Dashboard

An end-to-end **Website Traffic Analytics project** built using **SQL and Microsoft Power BI** to analyze website traffic, user behavior, engagement, and revenue performance.

The project transforms raw website-session data into interactive business intelligence reports that help identify high-performing traffic sources, valuable visitor segments, engagement patterns, and revenue opportunities.

---

## Business Objective

The objective of this project is to answer key business questions such as:

- Which traffic sources generate the most website traffic?
- Which traffic sources generate the highest revenue?
- Which countries contribute the most revenue?
- How do new and returning visitors behave differently?
- Which devices generate stronger user engagement?
- Does higher user engagement correspond to higher revenue?
- Which visitor segments represent the greatest business value?

---

## Tools & Technologies

- **SQL** — Data analysis and business querying
- **Microsoft Power BI** — Interactive dashboard development
- **Power Query** — Data transformation and preparation
- **DAX** — KPI and analytical calculations
- **Data Visualization** — Business reporting and storytelling

---

## Dataset

The dataset contains **5,000+ website session/user records** with information related to:

- User ID
- Session ID
- Traffic Source
- Country
- City
- Device Type
- Browser
- Operating System
- New / Returning Visitor
- Clicks
- Pages Visited
- Page Views
- Session Duration
- Revenue
- Conversion-related information
- Bounce-related information

---

#  Dashboard Structure

The Power BI solution is organized into **three analytical reports**.

---

##  Overview — Traffic & Audience

### Purpose
Provides an executive-level overview of website traffic and audience composition.

### Key KPIs
- Total Revenue
- Total Users
- Average Revenue
- Average Session Duration
- Total Countries

### Key Analysis
- Website traffic by traffic source
- Revenue by traffic source
- Revenue by country
- New vs returning visitors
- Audience and traffic characteristics

### Business Question

> **Where are website visitors coming from, and which audience segments are most valuable?**

---

##  Engagement & User Behaviour

### Purpose
Analyzes how users interact with the website and identifies differences in engagement across user segments.

### Key KPIs
- Total Users
- Average Clicks
- Average Pages Visited
- Average Page Views
- Average Session Duration

### Key Analysis
- Engagement by traffic source
- Engagement by device type
- New vs returning visitor engagement
- Relationship between engagement and revenue

### Business Question

> **How are users interacting with the website, which segments are most engaged, and does engagement translate into business value?**

---

##  Revenue & Conversion Performance

### Purpose
Focuses on revenue generation and identifies the visitor segments and acquisition channels contributing to business performance.

### Key KPIs
- Total Revenue
- Average Revenue
- Total Users
- Average Session Duration

### Key Analysis
- Revenue performance by traffic source
- Revenue by country
- Revenue by new vs returning visitors
- Engagement vs revenue relationship

### Business Question

> **Which sources and visitor segments generate the greatest business value?**

---

# SQL Analysis

SQL was used to perform the underlying analytical investigation before building the Power BI reports.

The analysis included:

- Aggregations
- `GROUP BY`
- `HAVING`
- `ORDER BY`
- Filtering
- Revenue analysis
- Traffic-source analysis
- User segmentation
- Subqueries
- CTEs
- Window functions
- `ROW_NUMBER()`
- `RANK()`
- `DENSE_RANK()`
- `LAG()`
- `LEAD()`
- Running totals
- Running averages
- Business-oriented analytical queries

---

# Key Analytical Findings

### Traffic Sources
Traffic sources were compared based on both **traffic volume and revenue contribution** to identify channels that attract users as well as channels that generate business value.

### Geographic Performance
Countries were analyzed to identify markets contributing the highest levels of website revenue.

### User Behaviour
New and returning visitors were compared using engagement metrics such as:

- Clicks
- Pages Visited
- Page Views
- Session Duration

### Device Behaviour
Device-level analysis was performed to understand how engagement varies across different visitor devices.

### Engagement vs Revenue
The relationship between website engagement and revenue was analyzed using correlation and visualization.

The correlation between **Pages Visited and Revenue was approximately -0.0013**, indicating an extremely weak linear relationship between the two variables.

This demonstrates an important business insight:

> **Higher page visits alone do not necessarily translate into higher revenue.**

Therefore, businesses should evaluate visitor quality and conversion behaviour rather than relying only on engagement volume.

---

#  Business Insights

The dashboard helps stakeholders:

- Identify high-performing acquisition channels
- Understand valuable geographic markets
- Compare new and returning visitor behaviour
- Identify device-level engagement patterns
- Evaluate the relationship between engagement and revenue
- Move from traffic-focused analysis toward revenue-focused decision-making

---

# Project Workflow

```text
Raw Website Data
       ↓
Data Cleaning & Preparation
       ↓
SQL Data Analysis
       ↓
Business Question Identification
       ↓
KPI Development
       ↓
Power BI Dashboard Development
       ↓
Interactive Analysis
       ↓
Business Insights & Recommendations
