# Print out all of the numbers in the following array that are divisible by 3:
# ```
# [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
# ```
# The expected output for the above input is:
# ```
# 27
# 81
# 9
# 27
# 99
# 63
# 42
# ```
# You may use whatever programming language you wish.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

arr = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

for i in arr:
    if i % 3 == 0:
        print(i)

# Print out all of the strings in the following array that represent a number divisible by 3:
# ```
# [
#   "five",
#   "twenty six",
#   "nine hundred ninety nine",
#   "twelve",
#   "eighteen",
#   "one hundred one",
#   "fifty two",
#   "forty one",
#   "seventy seven",
#   "six",
#   "twelve",
#   "four",
#   "sixteen"
# ]
# ```
# The expected output for the above input is:
# ```
# nine hundred ninety nine
# twelve
# eighteen
# six
# twelve
# ```

arr1 =  [
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]
