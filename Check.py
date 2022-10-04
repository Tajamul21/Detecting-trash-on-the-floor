

file=open("testcase2.txt",'w')

for i in range(2,10000):
    file.write(str(i)+'('.rstrip('\n'))
file.write('+X+Y+Z-X-Y-Z+X+Y'.rstrip('\n'))
for i in range(2,20):
    file.write(')'.rstrip('\n'))
file.write('+X+Y-Z-Y'.rstrip('\n'))

file.write("\n")

for i in range(2,20):
    file.write(str(i)+'('.rstrip('\n'))
file.write('+X+Y+Z-X-Y-Z+X+Y-Z+X-Y+Z-Z+Y-X+Y'.rstrip('\n'))
for i in range(2,20):
    file.write(')'.rstrip('\n'))
file.write('+X+Y-Z-Y-X-Z-Z-X'.rstrip('\n'))

file.write("\n")

for i in range(2,50):
    file.write(str(i)+'('.rstrip('\n'))
file.write('+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X'.rstrip('\n'))
for i in range(2,50):
    file.write(')'.rstrip('\n'))
file.write('+X+X+X+Y+X+X+X+X'.rstrip('\n'))

file.write("\n")


for i in range(2,100):
    file.write(str(2)+'('.rstrip('\n'))

file.write('+X+Y-X-Y'.rstrip('\n'))
for i in range(2,100):
    file.write(')'.rstrip('\n'))


file.write("\n")


for i in range(2,100):
    file.write(str(2)+'('.rstrip('\n'))

file.write('+X-x'.rstrip('\n'))
for i in range(2,100):
    file.write(')'.rstrip('\n'))
file.write('+X'.rstrip('\n'))




file.close()