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
The algorithm I'm planning to design for Vision is the login function. This would include starting on the login page --> inputting username and password and checking the terms and conditions box --> pressing the login button --> being brought to the home page.

The complexity of my algorithm is simple and should successfully meet performance requirements. The login process I'm designing my algorithm for is relatively simple, the conditions that must be met to login include: correct username input, correct password input and ticking the "I agree to the Terms & Conditions" box. After these conditions are met, the user should be able to successfully login and enter the Vision Homepage. In designing this algorithm I'm only considering the login process and not other elements involved in the login like the link to the Terms & Conditions page or the loading page screen.

Since the algorithm is simply to check whether the inputted data is correct and is very simple, there shouldn't be any scaling difficulties with user input. For exmaple, if the user input password is a paragraph long, there shouldn't be any problems with confirming it's validity. In addition, the login function operates independently for each user, meaning it wouldn't face server overload or any difficulties associated with cross-user functions.

### Implement and Testing of the login function
Translate the algorithm into code using a suitable programming language and rigorously test it with various inputs, to validate its correctness and robustness.

Developer: a) Design an algorithm for one functional component of your web application. MAKE SURE your algorithm is a STEP BY STEP outline of how input is processed/checked/stored by the system and produces an output. 
Functional components examples - web messaging system, login screen functionality, events posting, commenting on posts etc.

b) Design 2 test cases to discuss with your client - see "Test Case Template & Example" in the web link below entitled "HOw to create Test Cases" - you do not need to complete the ACTUAL RESULT and PASS/FAIL component at this stage 

### Test Case Example:
Let’s say you’re testing the login functionality of an app (This is the simplest example). Here’s how you could fill out the template:

Test Case ID: TC001
Test Case Name: Verify user login
Preconditions: User must have a registered account.
Test Steps:
Open the application.
Enter valid username and password.
Click the “Login” button.
Expected Result: The user is directed to the homepage.
Actual Result: To be filled after execution.
Pass/Fail: To be filled after execution.
Priority: High
