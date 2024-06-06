# Given the list of strings as input :

# gaurav1234@gmail.com
# pratik190900234@gmail.com
# 2009_rocking_person@yahoo.com
# GodFather2022@yahoo.com
# Brocklesner_89_WWE@yahoo.com
# TheRock_WWE@yahoo.com
# JohnCena_WWE@yahoo.com
# Undertaker_Roman_reigns@outlook.com
# 6789764666@rediffmail.com
# Kane#6789@gmail.com

# 1) provide me the list of emails that do have special characters of #~`!
# 2) provide me the list of emails that start with numbers
# 3) provide me the list of emails that start with numbers followed by an underscore
# 4) provide me the list of emails that start with numbers followed by an underscore or small case characters
# 5) provide me the list of emails that start with numbers followed by an underscore or small case characters or large case characters
# 6) Provide me list of emails with only numbers before the @
# 7) Provide me list of emails with numbers anywhere before the @


import re

string1 = 'gaurav1234@gmail.com'
string2 = 'pratik190900234@gmail.com'
string3 = '2009_rocking_person@yahoo.com'
string31 = '2009ROCKING_PERSON@yahoo.com'
string4 = 'GodFather2022@yahoo.com'
string5 = 'Brocklesner_89_WWE@yahoo.com'
string6 = 'TheRock_WWE@yahoo.com'
string7 = 'JohnCena_WWE@yahoo.com'
string8 = 'Undertaker_Roman_reigns@outlook.com'
string9 = '6789764666@rediffmail.com'
string10 = 'Kane#6789@gmail.com'

my_list = [string1,string2,string3,string4,string5,string6,string7,string8,string9,string10,string31]


special_chars_emails = [email for email in my_list if re.search(r'[#$~`!]', email)]
print("Emails with special characters of #~`!: \n", special_chars_emails)

# 2. Emails that start with numbers
starts_with_numbers_emails = [email for email in my_list if re.match(r'^\d', email)]
print("Emails that start with numbers: \n", starts_with_numbers_emails)


# 3. Emails that start with numbers followed by an underscore
starts_with_numbers_underscore_emails = [email for email in my_list if re.match(r'^\d_', email)]
print("Emails that start with numbers followed by an underscore: \n", starts_with_numbers_underscore_emails)

# 4. Emails that start with numbers followed by an underscore or small case characters
starts_with_numbers_underscore_or_smallcase_emails = [email for email in my_list if re.match(r'^\d[_a-z]', email)]
print("Emails that start with numbers followed by an underscore or small case characters: \n", starts_with_numbers_underscore_or_smallcase_emails)

# 5. Emails that start with numbers followed by an underscore or small case characters or large case characters
starts_with_numbers_underscore_or_smallcase_or_largecase_emails = [email for email in my_list if re.match(r'^\d[_a-zA-Z]', email)]
print("Emails that start with numbers followed by an underscore or small case characters or large case characters: \n", starts_with_numbers_underscore_or_smallcase_or_largecase_emails)

# 6. Emails with only numbers before the @
only_numbers_before_at_emails = [email for email in my_list if re.match(r'^\d+@', email)]
print("Emails with only numbers before the @: \n", only_numbers_before_at_emails)

# 7. Emails with numbers anywhere before the @
numbers_anywhere_before_at_emails = [email for email in my_list if re.search(r'\d', email.split('@')[0])]
print("Emails with numbers anywhere before the @: \n", numbers_anywhere_before_at_emails)