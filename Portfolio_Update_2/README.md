# Olympic Medalists Data Exploration

## Project Overview
This project explores Olympic medalists from the 2008 Olympics, with a focus on differences across gender and sport. Using the dataset "olympics_08_medalists.csv", the goal of the project is to clean and restructure the data before creating visualizations that highlight trends in medal distribution. A major component of this project is demonstrating the importance of tidy data. The dataset initially contains combined variables, which makes analysis more difficult. After cleaning and restructuring the data, I create visualizations and summary tables that provide clearer insights into medal counts by gender and sport.

## Instructions

### Running Locally
1. **Download Necessary Packages**
    pip install pandas matplotlib seaborn
2. **Run the Script**
    Open the Python file in VS Code or another preferred environment

## Project Features
### Dataset
- Uses the dataset: olympics_08_medalists.csv
- Dataset source: https://edjnet.github.io/OlympicsGoNUTS/2008/

### Data Cleaning (Tidy Data)
- The dataset initially contains non-tidy data with combined variables
- Data is restructured to follow tidy data principles: 
    - Each variable has its own column
    - Each observation has its own row
    - Each type of entity is stored separately

### Visualizations
- Graphs are created to explore:
    - Distribution of medal types
    - Medal counts by gender
    - Visualizations help highlight trends and differences across groups

## Additional Resources
### Tidy Data Paper (Hadley Wickham):
- https://vita.had.co.nz/papers/tidy-data.pdf
### Data Cleaning Cheat Sheet:
- https://www.kdnuggets.com/publications/sheets/Data_Cleaning_with_Python_Cheat_Sheet_Anello.pdf
### Pandas Data Wrangling Cheat Sheet:
- https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

