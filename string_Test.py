mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage)


print("""\nBoth sides of the %s get the same amount of sunlight,
but only one side is seen from %s because
the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

print("""\nYou are lighter on the {0}, because on the {0} 
you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

#Instead of empty braces, the substitution is to use numbers. The {0} means to use the first (index of zero) argument 
# to .format(), which in this case is Moon. For simple repetition {0} works well, but it reduces readability. To improve 
# readability, use keyword arguments in .format() and then reference the same arguments within braces:

print("""\nYou are lighter on the {moon}, because on the {moon} 
you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

print(f"\nOn the Moon, you would weigh about {mass_percentage} of your weight on Earth")

#The variables go within braces, and the string must use the f prefix.

#Aside from f-strings being less verbose than any other formatting option, it's possible to use expressions within 
# the braces. These expressions can be functions or direct operations. For example, if you want to represent the 
# 1/6 value as a percentage with one decimal place, you can use the round() function directly:

print(f"\nOn the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")

subject = "\ninteresting facts about the moon"
print(f"{subject.title()}")

