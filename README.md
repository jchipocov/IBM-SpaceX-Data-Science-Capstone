# SpaceX Falcon 9 First Stage Landing Prediction

## IBM Applied Data Science Capstone Project

**Repository:** [IBM-SpaceX-Data-Science-Capstone](https://github.com/jchipocov/IBM-SpaceX-Data-Science-Capstone)

**Program:** IBM Data Science Professional Certificate — Coursera

**Technologies:** Python, Pandas, NumPy, BeautifulSoup, SQL, Matplotlib, Seaborn, Folium, Plotly Dash, Scikit-learn, Jupyter Notebook, Google Colab

---

## 1. Project Overview

SpaceX has revolutionized the aerospace industry by developing reusable rocket technology. One of its key innovations is the ability to recover and reuse the Falcon 9 rocket's first stage.

This project applies data science techniques to historical SpaceX launch data to analyze the factors associated with successful first-stage landings and develop machine learning models to predict landing outcomes.

The project follows a complete data science workflow, from data collection and cleaning to exploratory analysis, interactive visualization, predictive modeling, and evaluation.

## 2. Business Problem

The reuse of rocket boosters is an important factor in reducing launch costs.

Predicting whether a Falcon 9 first stage will land successfully can contribute to understanding the operational characteristics associated with reusable launch systems.

**Main objective:**

Develop and compare classification models capable of predicting the success or failure of Falcon 9 first-stage landings using historical launch data.

**Research questions:**

- How does landing success vary across launch sites?
- Does payload mass influence landing success?
- How do orbit types relate to landing outcomes?
- Has the landing success rate improved over time?
- Which classification model provides the best predictive performance?

## 3. Data Sources

The project uses historical SpaceX data provided through the IBM Skills Network laboratories.

| Source | Description |
|---|---|
| SpaceX REST API | Historical rocket launch information |
| Wikipedia | Falcon 9 launch records collected through web scraping |
| IBM Skills Network | Curated datasets used in SQL, EDA, and machine learning |

Different laboratories use different historical datasets:

- **90 observations:** main data preparation and predictive modeling dataset.
- **101 observations:** SQL exploratory analysis dataset.
- **121 observations:** historical records extracted in the web scraping exercise.

These datasets are analyzed separately to avoid mixing statistics from different sources.

## 4. Project Methodology

### 4.1 Data Collection — SpaceX API

Historical launch information was collected and processed using Python and Pandas.

Main steps:

1. Retrieve historical launch information.
2. Transform JSON records into structured data.
3. Select relevant launch and booster attributes.
4. Process missing values.
5. Export the resulting dataset to CSV.

### 4.2 Data Collection — Web Scraping

BeautifulSoup was used to extract historical Falcon 9 launch records from Wikipedia HTML tables.

The process included identifying launch tables, extracting column headers, cleaning text fields, and converting records into a Pandas DataFrame.

### 4.3 Data Wrangling

The dataset was cleaned and prepared for analysis.

Key operations included:

- Handling missing values.
- Selecting relevant features.
- Examining launch sites and orbit types.
- Creating the binary target variable `Class`.

Target definition:

- `Class = 1`: Successful first-stage landing.
- `Class = 0`: Unsuccessful first-stage landing.

### 4.4 Exploratory Data Analysis — SQL

SQL queries were used to investigate launch characteristics, including launch sites, payload mass, booster versions, landing outcomes, and historical events.

### 4.5 Exploratory Data Analysis — Visualization

Matplotlib and Seaborn were used to investigate relationships between:

- Flight number and launch site.
- Payload mass and launch site.
- Orbit type and landing success.
- Flight number and orbit type.
- Payload mass and orbit type.
- Year and landing success rate.

### 4.6 Interactive Geographic Analysis — Folium

Folium was used to create geographic visualizations showing launch-site locations, landing outcomes, and proximity measurements.

The maps include launch-site markers, successful and unsuccessful landing markers, and marker clustering.

### 4.7 Interactive Dashboard — Plotly Dash

An interactive dashboard was developed with Plotly Dash.

Its features include:

- Launch-site dropdown selection.
- Pie charts showing successful landings by site.
- Success-versus-failure analysis for individual sites.
- Interactive payload mass filtering.
- Scatter plots relating payload mass to landing outcomes.

### 4.8 Predictive Modeling

Four supervised classification algorithms were evaluated:

1. Logistic Regression
2. Support Vector Machine (SVM)
3. Decision Tree
4. K-Nearest Neighbors (KNN)

Model development included feature encoding, standardization, training/test splitting, hyperparameter optimization using GridSearchCV, and model evaluation.

## 5. Key Findings

### Exploratory Analysis

The main predictive dataset contained **90 launches**, classified as:

- **60 successful first-stage landings**
- **30 unsuccessful first-stage landings**

Landing success improved substantially over the historical period.

In the exploratory analysis:

- The landing success rate reached **90% in 2019**.
- The landing success rate was approximately **84.2% in 2020**.

The Plotly Dash analysis also showed a **76.9% landing success rate at KSC LC-39A** in the dashboard dataset.

### Machine Learning Results

| Model | Cross-Validation Accuracy | Test Accuracy |
|---|---:|---:|
| Logistic Regression | 84.64% | 83.33% |
| Support Vector Machine | 84.82% | 83.33% |
| Decision Tree | **87.68%** | 83.33% |
| K-Nearest Neighbors | 84.82% | 83.33% |

**Main finding:** All four models achieved the same test accuracy of 83.33%.

Decision Tree achieved the highest cross-validation accuracy, but no model demonstrated superior accuracy on the held-out test set.

The test dataset contained only 18 observations, so the results should be interpreted cautiously.

## 6. Project Files

The repository contains eight main project files:

| File | Description |
|---|---|
| `01_jupyter-labs-spacex-data-collection-api.ipynb` | Data collection using SpaceX API |
| `02_jupyter-labs-webscraping-revisado-colab.ipynb` | Wikipedia web scraping |
| `03_labs-jupyter-spacex-Data wrangling.ipynb` | Data preparation and cleaning |
| `04_jupyter-labs-eda-sql-coursera_sqllite.ipynb` | Exploratory analysis with SQL |
| `05_edadataviz_completado_colab.ipynb` | Exploratory data visualization |
| `06_lab_jupyter_launch_site_location_completado_colab.ipynb` | Interactive Folium maps |
| `07_spacex_dash_app.py` | Interactive Plotly Dash dashboard |
| `08_SpaceX_Machine_Learning_Prediction_Part_5.ipynb` | Machine learning classification |

## 7. How to Run the Project

### Jupyter Notebooks

Most notebooks can be opened using Google Colab or a compatible Jupyter environment.

1. Download or clone this repository.
2. Open the desired `.ipynb` file.
3. Install any required dependencies.
4. Execute the cells in order.

Some notebooks load historical datasets directly from IBM Skills Network URLs, so an internet connection may be required.

### Plotly Dash Application

Install the required packages:

```bash
pip install pandas dash plotly
```

Place the file `spacex_launch_dash.csv` in the same directory as the dashboard application.

Run:

```bash
python 07_spacex_dash_app.py
```

Open the application at:

```text
http://127.0.0.1:8050/
```

The dashboard provides interactive exploration of launch-site performance and payload-related landing outcomes.

## 8. Conclusions

The analysis demonstrates how different data science methods can be combined to investigate rocket-launch operations and predict first-stage landing outcomes.

The main conclusions are:

1. Historical Falcon 9 first-stage landing success improved significantly over time.
2. Launch site, payload mass, orbit type, and flight experience provide useful information for exploratory analysis.
3. Interactive dashboards and geographic maps help communicate complex launch data.
4. All four classification models achieved 83.33% test accuracy in the evaluated dataset.
5. Larger and more recent datasets would be valuable for improving predictive reliability and assessing model generalization.

### Future Improvements

Potential future work includes:

- Expanding the dataset with more recent SpaceX launches.
- Investigating additional engineering and environmental variables.
- Evaluating model calibration and false-positive predictions.
- Applying more extensive cross-validation and statistical uncertainty analysis.
- Exploring ensemble methods and alternative classification techniques.

## 9. References

- [IBM Data Science Professional Certificate — Coursera](https://www.coursera.org/professional-certificates/ibm-data-science)
- [SpaceX API](https://github.com/r-spacex/SpaceX-API)
- [Wikipedia — List of Falcon 9 and Falcon Heavy launches](https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Plotly Dash Documentation](https://dash.plotly.com/)
- [Folium Documentation](https://python-visualization.github.io/folium/)

---

**Project Type:** Educational Data Science Capstone

**Tools:** Python, SQL, Machine Learning, Data Visualization, Interactive Dashboards

**Institution:** IBM Skills Network / Coursera
