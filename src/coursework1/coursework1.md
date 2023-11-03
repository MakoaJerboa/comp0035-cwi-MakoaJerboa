# Coursework 1 Markdown
## Explanation
My dataset had multiple CSVs so I selected one which seemed like it had useful and versatile data. I then created a dataframe using pandas and pathlib. I didn't need the first 3 columns so I used pandas to drop them.  Despite the data being quite clean from the start, I used pandas to drop any null values so that the code would still work correctly for other datasets which may not be clean. I then used pandas to reorganise the data into a new dataframe with all of the columns in the order I needed them. Finally I used pandas to write that dataframe to a new CSV, this CSV is now fully prepared for future use.
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