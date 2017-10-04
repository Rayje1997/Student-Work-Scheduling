import time

print("What would you like to output to this text file?")
output = input()

f = open ("test.txt", "w")

f.write(output)

f.close()

time.sleep(3)
