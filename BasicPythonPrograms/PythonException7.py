# Put unsafe operation in try block
try:
    print("Code Start")
    # Unsafe opertion perform
    print(1/0)
# If error occur the it goes in except block
except:
    print("an error occurs")
# final code in finally block
finally:
    print("Pushkar")
