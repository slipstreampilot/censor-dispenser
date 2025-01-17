# censor-dispenser
Project Goals
You’ve recently gotten a job working in the IT department at one of Silicon Valley’s hottest new startups, AirWeb. The company is developing a state-of-the-art artificial intelligence engine designed to help provide a new perspective on the world’s problems. Interestingly, very few people know the details of AirWeb ‘s work and the company is very secretive about its technology, even to its own investors.

You report directly to the Head of Product, a person named Mr. Cloudy, and he has a very important task for you. You see, every month, the head researchers down in the lab send an email to the board of investors to tell them about the status of the project. Cloudy wants you to intercept these emails and censor any “proprietary information” included in them.

*Step 1*
Write a function that can censor a specific word or phrase from a body of text, and then return the text.

Mr. Cloudy has asked you to use the function to censor all instances of the phrase learning algorithms from the first email, email_one. Mr. Cloudy doesn’t care how you censor it, he just wants it done.

*Step 2*
Write a function that can censor not just a specific word or phrase from a body of text, but a whole list of words and phrases, and then return the text.

Mr. Cloudy has asked that you censor all words and phrases from the following list in email_two.
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

*Step 3*
The most recent email update has concerned Mr. Cloudy, but not for the reasons you might think. He tells you, “this is too alarmist for the Board of Investors! Let’s tone down the negative language and remove unnecessary instances of ‘negative words.’”

Write a function that can censor any occurance of a word from the “negative words” list after any “negative” word has occurred twice, as well as censoring everything from the list from the previous step as well and use it to censor email_three.
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

*Step 4*
This final email has Mr. Cloudy in a frenzy. “We can’t let this information get out!” He tells you, “our company would be ruined! Censor it! Censor it all!”

Write a function that censors not only all of the words from the negative_words and proprietary_terms lists, but also censor any words in email_four that come before AND after a term from those two lists.

*Step 5*
Great job! The Board of Investors is none the wiser to what is going on in the lab and Mr. Cloudy is very happy.

Take a moment to look over your functions, are they the best they can be? As a challenge, make sure they:

Handle upper and lowercase letters.
Handle punctuation.
Censor words while preserving their length.

*Step 6*
Great work! Visit our forums to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different from ours, and that’s okay! There are multiple ways to solve these projects, and you’ll learn more by seeing others’ code.
https://discuss.codecademy.com/t/censor-dispenser-challenge-project-python/462400

