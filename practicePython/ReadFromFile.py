import re 

def countNames():
    lea=0
    darth=0
    luke=0
    with open('nameslist.txt', 'r') as open_file:
        line = open_file.readline()
        while line:
            if line.find("Lea") != -1:
                lea+=1
            elif line.find("Darth") != -1:
                darth+=1
            elif line.find("Luke") != -1:
                luke+=1
            line = open_file.readline()
        print(lea,darth,luke)



def find_between(s, start, end):
  return (s.split(start))[1].split(end)[0]
  
def countCatergories():
    arrayA = []

    with open('Training_01.txt', 'r') as open_file:
        line = open_file.readline()
        while line:
            arrayA.append(re.search('%s(.*)%s' % (r"[a-z]", "/sun"), line).group(1))
            # arrayA.append(find_between(line, r"[a-z]", "/sun"))
            line = open_file.readline()
        # print(set(arrayA))
        print(len(set(arrayA)))

# solution 
counter_dict = {}
with open('Training_01.txt') as f:
	line = f.readline()
	while line:
		line = line[3:-26]
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

countCatergories()
countNames()
print(len(counter_dict))
