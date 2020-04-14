# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#step 1 code

ban = "learning algorithms"

email_one_censored = email_one.replace(ban,"-"*len(ban))

#this completes step 1

#beginning step 2

#test string
email_two_censored = email_two

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

proprietary_terms_upper = []

for word in proprietary_terms:
    proprietary_terms_upper.append(word.title())

proprietary_terms += proprietary_terms_upper

for word in proprietary_terms:
    email_two_censored = email_two_censored.replace(word,"-"*len(word))

#print(email_two_censored)

# beginning step 3

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

email_three_censored = email_three

negative_words_upper = []

for word in negative_words:
    negative_words_upper.append(word.title())

negative_words += negative_words_upper

banned_words = negative_words + proprietary_terms

for word in banned_words:
    email_three_censored = email_three_censored.replace(word,"-"*len(word))

#print(email_three_censored)

# beginning step 4

email_four_censored = email_four

email_four_censored_split = email_four_censored.split(' ')

for word in banned_words:
    try:
        before = email_four_censored_split.index(word) - 1
        during = email_four_censored_split.index(word)
        after = email_four_censored_split.index(word) + 1
        email_four_censored_split[before] = '-'*len(email_four_censored_split[before])
        email_four_censored_split[during] = '-'*len(email_four_censored_split[during])
        email_four_censored_split[after] = '-'*len(email_four_censored_split[after])
    except:
        continue

email_four_censored = ' '.join(email_four_censored_split)

print(email_four_censored)
