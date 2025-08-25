# Moodboard-Website
a project to help learn the ropes of frontend and backend design.

## Project description
### Functional requirements
what the app will do.
The app's main function will be a moodboard. It will be downloadable on PC.

It is basically a blank board where you can paste links, images, gifs or videos or even recordings(optional) from the internet and add notes to annotate it.
 - I'm taking some inspiration from moodboard appls like Ar*ena, Behance and Cosmos.

The app will feature a login function so users can access their moodboards across different devices. An authorisation function will ensure that their data and privacy is well-protected from hackers and people with malicious intent. - Maybe I'll even add a human verification step.
--> the login function will use google accounts which will be the profile

My moodboard will have different themes and customisable options. It allows users to:
- move items around
- change the background colour
- change font colour, size and highlight text
- click on buttons to use different functions
- move across the whiteboard by scrolling and using the mouse to click and drag.

to allow users to easily use the app:
- can just copy and paste images(crop and spin is optional)

social network:
share moodboard with others, similar to google docs
great for group design projects!


### Non-functional requirements
what the app will looks like + how it will function

To enter the app, you need to create an account, verify it, then login.

The app will look like a plain whiteboard with a control bar at the top(similar to google docs). By interacting with this control bar, users should be able to have access to all the customisation functions.

if the website doesn't load, an error message will pop up with a list of all the reasons it did not work.

if the login is incorrect, a message will pop up.

if the image/element pasted into the app doesn't work, a message will say "image not valid??"

when the system is loading, a loading screen with a spinning circle will pop up.

the system shouldn't overload and is expected to have a good response time.


This entire coding process should not be too difficult because there are tutorials online and what i have decided to do follows closely to the conent we learnt in grok.



## Vision Wireframe
The social network I'm designing will be called Vision.
Note: it is a Design Website, not app
The style I am going for is a simple and elegant. I'm planning on using font Vollkorn. 
My colour palette will be grey because grey is a flexible colour which will adapt to different moodboard themes. I've tried to keep the website simple because my capabilities, time and recources are limited, however I should be able to create a simple model of this design.

Next week I'm planning on refining my web design on Wix because so far it is very rough, and I need to see how it will look and flow on a laptop.



## Designing an algorithm: The Login Algorithm
### My evaluation of my login function
The algorithm I'm planning to design for Vision is the login function. This would include starting on the login page --> inputting username and password and checking the terms and conditions box --> pressing the login button --> being brought to the home page. The verification will work for the user's google account only. In order for the verification to work, the user username and password must match with an existing google account.

The complexity of my algorithm is simple and should successfully meet performance requirements. The login process I'm designing my algorithm for is relatively simple, the conditions that must be met to login include: correct username input, correct password input and ticking the "I agree to the Terms & Conditions" box. After these conditions are met, the user should be able to successfully login and enter the Vision Homepage. In designing this algorithm I'm only considering the login process and not other elements involved in the login like the retriving google account details, the "create an account" link, the link to the Terms & Conditions page or the loading page screen. I've decided there will be two error messages "Terms & Conditions not agreed to" and "Username or password is incorrect" rather than specifying each incorrect input because this makes it harders for hackers to sign in.

Since the algorithm is simply to check whether the inputted data is correct and is very simple, there shouldn't be any scaling difficulties with user input. For exmaple, if the user input password is a paragraph long, there shouldn't be any problems with confirming it's validity. In addition, the login function operates independently for each user, meaning it wouldn't face server overload or any difficulties associated with cross-user functions.

### Implement and Testing of the login function
I'm going to implement the login algorithm in Spyder - I've attatched a copy of the code and how it runs(Login algorithm code).
In regards to how the algorithm should operate, I've attatched a flowchart of the basic process(login algorithm flowchart)).


### Test Cases
These are the test cases for the login function.

Test Case ID: 1
Test Case Name: User Login process
Preconditions: User must be on the vision login page and user must have a google account.
Test Steps:
1. Open the login page.
2. Check box "I agree to the Terms & Conditions"
3. Enter valid username and password.
4. Click the “Login” button.
Expected Result: The user is directed to the homepage.
Actual Result: The user successfully logs in and is directed to the home page.
Pass/Fail: passed
Priority: High

Test Case ID: 2
Test Case Name: User Login process
Preconditions: User must be on the Vision login page and user must have a google account.
Test Steps:
1. Open the login page.
2. Check box "I agree to the Terms & Conditions"
3. Enter invalid username and password.
4. Click the “Login” button.
Expected Result: The error message "incorrect username or password" pops up.
Actual Result: The error message "incorrect username or password" pops up.
Pass/Fail: passed
Priority: High

does this algorithm ALIGN WITH THE STATED PURPOSE OF THE APP and meet the client needs?
Yes, the purpose of the app is to allow users to collaborate together on an artistic project using moodboard. Having this google login functions allows users to protect their privacy, save their moodboard projects and share these projects with specific individuals. This login enables users to collaborate together on the same project at the same time.

-sync to cloud function

## Setting up SQL
SQL has been successfully set up 21/8/2025

### Creating my own database structure 
- consider table names, data headings, primary keys, foreign keys, types of data stored etc.
Considerations for my data:
what data do you want stored during the use of your app?
the different google users
any moodboard projects
any and all imported assets
comments/feedback database
collaborators database
tags databas(favourite or not favourite)

what data you want displayed on your front end?
Moodboard project names, pictures and tags
Images and names of imported assets
The profiles and external information of users
The profiles of collaborators
Comments: The dates they were made and the content of the comment

To understand and explain what data is related to each other, I must use arrows and explain the flow. 
How the data will be used and interact with other data in the backend.

what data types should for elements be in your database (text, numeric, image etc)
Integer
string
boolean
datetime
content(assets can be any type: text, images, links and videos)

what queries might you need to write (between and across tables) allowing for good information storage and retrieval
Potential data query types needed:
- exact match(search bar), nearest neighbour(recent moodboards)
- neraest neighbour query
- Insertion, deletion and update queries for moodboards and during moodboard editing.

### SQL Queries
Here is the Excel databse: https://schoolsnsw-my.sharepoint.com/:x:/g/personal/tianna_liu1_education_nsw_gov_au/Eb0u3LLtonROve5Bz90Ep9cB6LIx-s8JwNC1Z7PSVi_aJw?e=QALNk7

d) Write a series (5+) of SQL queries to combine and test your data is displaying correctly from your tables - read through SQL Tutorial
for some ideas - PS. SELECT * FROM "Table" is only a very, very basic Query - create several from across tables showing joins and MEANINGFUL data that a user might find useful.

Query 1. 
Query 2. 
Query 3. 
Query 4. 
Query 5. 
Query 6. 
