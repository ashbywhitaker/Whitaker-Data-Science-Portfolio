# In this project, I will explore the Olympic Medalists of different sports across gender. I load the "olympics_08_medalists.csv" dataset. Because the data is not tidy, I begin by tidying the data and fixing some of the conjoined variables. After the data is cleaned, I begin with visualizations to explore types of medals and medals by gender. Finally, I aggregate a pivot table by gender and medal counts. This gives a clear indication of medals by sport and gender - perhaps the most enlightening part of my project. 

# After establishing the purpose of my project, one must understand why tidy data is important. While it will be clear in the project the before and after of the data frame is significantly easier to follow, the principles of tidy data require this change. In order to properly understand data, eliminate possibilities for mistakes, and remove unnecessary complexities, each variable must have its own column, each observation must have its own row, and different entities should have their own tables. As an example of tidy data, in my project I had to split gender and sport because each variable needed its own column. 

# In order to run this project, one must import pandas, matplotlib, and seaborn. I have commented the code in order to allow for the project to be easily followed or replicated.

# The dataset that I use is the "olympics_08_medalists.csv" data. The purpose of the dataset is to include medal winners by place of birth and not country. The goal of the dataset is to show what countries are actually strongest in team sports, not necessarily by their olympic teams but by their medalist winners. I use the dataset out of more interest in gender, sport, and medal count. I am including a link to the source: https://edjnet.github.io/OlympicsGoNUTS/2008/ 

# Finally, in order to faciliate further study and understanding of this project and the importance of tidy data, I am providing links to a cheat sheet and a paper by Hadley Wickham, entitled "Tidy Data." The paper was published in the Journal of Statistical Software. 

## https://vita.had.co.nz/papers/tidy-data.pdf 
## Data Cleaning Cheat Sheet: https://www.kdnuggets.com/publications/sheets/Data_Cleaning_with_Python_Cheat_Sheet_Anello.pdf 
## Data Wrangling Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf 
