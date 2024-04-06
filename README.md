### question model ###
Question Class to establish the model of each question
using text and answer to be used to establish each question
for the "question bank" from data.py file

### data ###
File used to establish connection with OPEN TRIVIA DB (API)
Parameters used:
amount: number of questions
category: category of questions
difficulty: Easy, medium, hard
type: Multiple choice or True/False
encode: default, base64...

data is fetch using .json() method

## Quiz Brain ##
Class which itialize score to 0 and picks the questions from
the question bank (main.py).

### still_has_question_method ###
Used to create a loop until reach the amount of questions defined
in the data.py parameters

### next_question method ###
Pick a question from the list, decrypt it using
unescape from html package and return it to the UI

### check_answer method ###
Check the answer from user (right_choice & wrong_choice method
of QuizInterface Class) and update the score

# UI #
User interface using tkinter with initializacion 
of the score label, canvas for questions and right
and wrong buttons.

It also calls a class QUIZ from QUIZBRAIN and it calls
next_question method

### get_next_question method ###
Picks the question text from QUIZBRAIN next_question method
and used the itemconfig method of canvas to change the text

### right_choice & wrong_choice method ###
Call check_answer method on QUIZBRAIN class passing them
"True" or "False" as user answer then it pass the result
to give_feedback method

### give_feedback method ###
Change background color of the canvas image and
call next_question method of QUIZBRAIN

