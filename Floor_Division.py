seconds = 1042
display_minutes = 1042 // 60
print(display_minutes)

# Output: 17


seconds = 1042
display_minutes = 1042 // 60                        # floor division
display_seconds = 1042 % 60                         # % means Modulo or Mod or (Mod(x))

print(display_minutes)
print(display_seconds)


result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)
print(result_1)
print(result_2)
# The answer is the same in both cases - 1084


demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)


#Convert the negative value to be its absolute value by using abs. If you perform the same operation by 
# using {abs} (and print the answers), you notice that it shows 23 for both equations.


print(abs(39 - 16))
print(abs(16 - 39))


#The built-in Python function called round is also helpful. Use it to round up to the nearest integer if the decimal value 
# is .5 or greater, or down if it's less than .5.


print(round(14.5))


"""Python has libraries to provide more advanced operations and calculations. One of the most common is the math library. 
math allows you to perform rounding with floor and ceil, provide the value of pi, and numerous other operations. Let's see 
how to use this library for rounding up or down.

Rounding numbers enables you to remove the decimal portion of a float. You can choose to always round up to the nearest 
whole number by using ceil, or down by using floor."""

from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

