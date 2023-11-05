# Coursework 1 Markdown
## Explanation
### Step 1: Selecting Appropriate Data
My dataset had multiple Excel files, after examining the various datasets I decided to use the census data on hours worked in different areas in 2011 and 2021. I decided to use this data as it seemed versatile, I could explore the trends on average hours worked in different areas, and also see how these values changed between the 2 years.

### Step 2: Importing the Data
My dataset had multiple books inside the Excel file. I used pathlib and pandas to read the books for 2011 and 2021 into seperate dataframes. There was a third book showing the change between years, but I decided not to import it since I could just add or subtract the data myself once I've finished transforming it. This would also mean that I don't have to consider negative numbers at this stage. Some of the columns contained extra area code data. Since the second column already had human readable names for the areas, I didn't need the other columns so I used pandas to drop them. From observation of the Excel, the data seemed quite clean. However to ensure there were no null values present I used pandas to drop any to ensure they didn't carry through and become problematic later on.

### Step 3: Transforming the Data
My dataset had the workers split into different categories based on how many hours they worked. Each row also had the area in which the data was taken, however these areas were split into smaller sub areas with area codes. I wanted to consider the total number of workers in each major area so I created a function which used pandas to sum all these rows together and return that as a new dataframe. I decided to use a function so that I could feed the dataframe for each year into it seperately and not have to repeat any code. I decided to consider only major areas and ignore the smaller ones so that my dataset would have fewer rows, thereby allowing trends to be more clearly visible across larger areas. 

### Step 4: Examining the Data
I created a function called summary to print out general information about the dataframe. It prints out the number of rows and columns in the dataframe, then the first and last 5 lines of it, finally it prints the datatypes in the dataframe. Because my original data had no numbers in it, outliers were not really a concern, my main concern when summing up how many people were in each category was if there were any typos which would cause a line to not be grouped correctly. This step shows how many rows and columns there are in the data, so if there was an extra column with the same data spelled slightly differently this step would reveal that, looking at the datatypes within the function would also help diagnose and potential problems in the dataset if anything unexpected was present. Finally printing the first and last few lines of the dataset is a simple common sense check which would reveal and obvious problems with the data such as row being labelled incorrectly or all of the values being completely incorrect. I also considered using boxplots or histograms to verify the integrity of the data and check for outliers, however to effectively ensure there were no outliers present, several graphs would have to be generated, so I decided these simple measures were more practical.

### Step 6: Saving the Data
I decided to save the returned dataframes to new CSVs manually, while it was possible to make a function for this, doing so would be significantly longer and less readable than just copying the same line twice. However if I had several dataframe it would have been appropriate to use a function. I decided to use seperate CSVs for each year instead of combining them together since it would make my future code more efficient. Since I would only be loading the data I intend to use, my code would require less system resources to run. Using multiple files also means that when loading dataframes in future code, I won't need to drop unnecessary columns since I'll be loading from a CSV which has only the columns I need for that specific part.

### Linter Adjustments
I adjusted the linter to allow up to 120 characters rather than 79 per line. Trying to keep the lines under 80 characters forced me to use shorter, less readable variable names and split lines making them harder to follow.
## Product and Project Definition
### Product Overview
This coursework involves creating two webapps. 

The first app will be a REST API which will allow developers to access and use my dataset in their apps. The target audience of this is software developers.

The second app will be a data visualisation / dashboard app. This app will be used to repesent that data in a visual way with graphs. Since my dataset is based on census data, the target audience for this app would be researchers such as students, politicians or journalists.
### Persona
![Persona](persona.png)

## Tools and Techniques
### Source Code Control
https://github.com/ucl-comp0035/comp0035-cwi-MakoaJerboa


GitHub was used for source code control, the GitHub extension was also used in Visual Studio Code to allow pulling and pushing from within the editor.
### Use of AI
GitHub Copilot autocomplete was enabled and used throughout the data preparation section.