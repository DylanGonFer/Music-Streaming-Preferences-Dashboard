This repository contains an analysis of listener preferences on music platforms around the world. Python (Pandas) is used for data cleansing and Power BI is used to generate an interactive dashboard.
🚀 Project Objetive
Explore music streaming trends and gain insights into listener preferences by genre, country, and other relevant metrics.
🛠️ Tools
- Python (Pandas): For data cleaning and transformation.
- Power BI: For interactive visualization and analysis.

📊 Data Source
The dataset used in this project comes from Kaggle, a leading platform for data analysis and machine learning. You can find it at the following link: Worldwide Music Streaming Trends and Insights.
Dataset of the Details
The dataset contains information on music streaming trends across various countries, including preferred genres, average listening duration, and other key insights.
📋 Data Cleaning Methodology
The data cleaning and transformation process was performed using Python with Pandas combined with pandasql, which allowed me to leverage the convenience and familiarity of SQL directly within the Python environment. This approach was ideal for efficiently querying and manipulating the dataset.
Why Use SQL and pandasql?
- Convenience and Familiarity:
SQL is a widely-used language for data manipulation, and its integration with pandasql allowed me to apply SQL queries without leaving the Python environment.
- Advantages of Pandas:
While SQL is powerful, the versatility of Pandas enabled advanced tasks like statistical imputations and detailed transformations that are less intuitive in pure SQL.
- Efficient Workflow:
The combination of these tools offered the best of both worlds:- SQL for quick filtering, joining, and selecting data.
- Pandas for more advanced operations, such as handling missing values, normalizing columns, and exporting the processed dataset.

- Export to CSV:
The cleaned dataset was saved as a new CSV file (clean_dataset.csv), making it ready for import into Power BI while ensuring high-quality data for visualization.

This methodology ensures a professional and reproducible data cleaning process by utilizing modern tools that maximize both precision and productivity.
