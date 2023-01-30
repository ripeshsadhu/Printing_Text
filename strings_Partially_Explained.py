heading = "temperatures and facts about the moon"
heading.title()
'Temperatures And Facts About The Moon'


"temperatures and facts about the moon".title()
'Temperatures And Facts About The Moon'


temperatures = """Daylight: 260 F
Nighttime: -280 F"""
temperatures .split()
['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']


temperatures .split('\n')
['Daylight: 260 F', 'Nighttime: -280 F']


"Moon" in "This text will describe facts and challenges with space travel"
False
"Moon" in "This text will describe facts about the Moon"
True


temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
while Mars has -28 Celsius."""
temperatures.find("Moon")
-1
#The .find() method returns a -1 when the word isn't found, or it returns the index 
#(the number representing the place in the string). This is how it would behave if you're searching for the word Mars:


temperatures.find("Mars")
65


temperatures.count("Mars")
1
temperatures.count("Moon")
0

#Strings in Python are case-sensitive, which means that Moon and moon are considered different words. To do a case-insensitive comparison, 
#you can convert a string to all lowercase letters by using the .lower() method:
"The Moon And The Earth".lower()
'the moon and the earth'

#Similar to the .lower() method, strings have an .upper() method that does the opposite, converting every character to uppercase:
"The Moon And The Earth".upper()
'THE MOON AND THE EARTH'


#Tip
"""When you're searching for and checking content, a more robust approach is to lowercase a string so that casing doesn't prevent 
a match. For example, if you're counting the number of times the word the appears, the method wouldn't count the times where The 
appears, even though they're both the same word. You can use the .lower() method to change all characters to lowercase."""


