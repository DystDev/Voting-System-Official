


# Intoduction
 A simple, lightweight, however feature packed voting system, made to run using python. Has features including Day Stats Tracking, named voter with votes, and even corruption. Optimised to be run in a command line. Stylish and smooth.

# Main Usage
 When run, the app will prompt you to add candidates. Duplicate candidate names are not allowed. Then, set the password (hidden from view). After that, the program will start.
 
# Administration
 On typing ADMIN, you will be prompted to enter the password. On authentication, there are many functions possible:
 - CORRUPT: Adds 1000000 votes to a candidate of your choice
 - SAVE: Saves the results, voters, and days to their respective files.
 - LOAD: Loads the results from the files.
 - RETURN: Goes back to Voter view. Can return to Admin panel at any time
 - END: Ends the program - views end results for each candidate and the winner. Can reset the program after 5 seconds on this screen
 - SET: Choose a candidate, then choose the number of votes to set their result to.
 - VOTERS: Shows the voters in the campaign and who they voted for
 - NEWDAY: Will start a new day of voting.
 - DAYS: Shows the results for the candidates on each day

# Requirements
 You will need 3 .txt files in the directory of main.py. There are 4 builtin modules used.
 - votes.txt: Saves the candidates and their number of votes.
 - voters.txt: Saves the voters and their chosen candidate
 - days.txt: Saves the past and current results for each candidate for each day.

 These files are vital for saving and loading.

# Warning
 WARNING! This is an informal program. There is no encryption for saved results. If you want encryption, add an issue.
 
# How to use
 
#### Clone the repo in the command line. You need github to be installed
```console
git clone https://github.com/DystDev/Voting-System-Official
 ```
 #### Run main.py in the created directory, which includes all needed text files.
 ```console
 python main.py
 ```
