# float_precision_issue.py

# This program demonstrates floating-point precision errors in Python

# Add two floating-point numbers
# Mathematically, 0.1 + 0.2 should equal 0.3
# But due to the way floats are represented in binary, this is not exact
if (0.1 + 0.2 == 0.3):
    print("true")
else:
    print("false")  # ❌ This will print "false" because 0.1 + 0.2 = 0.30000000000000004
