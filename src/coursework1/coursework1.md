# Coursework 1 Markdown
## Explanation
My dataset had multiple CSVs so I selected one which seemed like it had useful and versatile data.

The dataset I selected contained, how many hours a person worked, the area where they lived and what their occupation was. This dataset didn't have any numbers in its original state so I decided the best place to start was by summing up the different categories so I could compare them against each other to answer questions and create graphs.

I then created a dataframe using pandas and pathlib. I didn't need the first 3 columns so I used pandas to drop them.  Despite the data being quite clean from the start, I used pandas to drop any null values so that the code would still work correctly for other datasets which may not be clean.

My dataset had the workers split into different categories based on how many hours they worked, so I created a function which used pandas to create a new dataframe of how many workers were in each category and compare them against a given criteria which the function takes as an argument. I decided to use a function so that multiple different criteria could be sorted into seperate data frames by calling the function again.

After each time I called the function, I saved the dataframe as a new CSV. I decided to use seperate CSVs instead of combining them all together since this would mean when I load a csv into a dataframe, I will only be loading the data I need which is more efficient. This is helpful as my dataset is quite large with nearly 180,000 rows. Using multiple files also means that when plotting graphs, I won't need to drop unnecessary columns since I'll be loading a dataset which already has them removed.

Finally, I adjusted the linter to allow up to 120 characters rather than 79 per line. Trying to keep the lines under 80 characters forced me to use shorter, less readable variable names and split lines.
## Product and Project Definition
### Product Overview
This coursework involves creating two webapps. 

The first app will be a REST API which will allow developers to access and use my dataset in their apps. The target audience of this is software developers.

The second app will be a data visualisation / dashboard app. This app will be used to repesent that data in a visual way with graphs. Since my dataset is based on census data, the target audience for this app would be researchers such as students, politicians or journalists.
### Persona
## Tools and Techniques
### Source Code Control
https://github.com/ucl-comp0035/comp0035-cwi-MakoaJerboa


GitHub was used for source code control, the GitHub extension was also used in Visual Studio Code to allow pulling and pushing from within the editor.
### Use of AI
GitHub Copilot autocomplete was used for the data preparation section. The loop near the end of the code was also quite long, I asked github copilot to shorten it and combined its shortened code with my original loop.