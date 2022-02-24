import fileinput

def encrypt(tableau,msg,points,cols,rows):
    res = ''
    msg = msg.upper().replace(' ','')
    for w in msg:
        for i in range(0,len(tableau)):
            for j in range(0,len(tableau[0])):
                if tableau[i][j] == w:
                    rows.append(i)
                    cols.append(j)
    points = rows + cols
    for r in range(0,len(points),2):
        res = res + tableau[points[r]][points[r+1]]
    return res
    
def decrypt(tableau,msg,points,cols,rows):
    res = ''
    for w in msg:
        for i in range(0,len(tableau)):
            for j in range(0,len(tableau[0])):
                if tableau[i][j] == w:
                    points.append(i)
                    points.append(j)
    length = int(len(points)/2)
    rows = points[0:length]
    cols = points[length:len(points)]
    for r in range(0,len(rows)):
        res = res + tableau[rows[r]][cols[r]]
    return res

#msg = 'PDFRRNGBENOPNIAGGF'
#msg = 'BRING ALL YOUR MONEY'

def bifid(option,msg):
	rows, cols, points = [], [], []
	res = ''
	tableau = [['E','N','C','R','Y'], ['P','T','A','B','D'], ['F','G','H','I','K'], ['L','M','O','Q','S'], ['U','V','W','X','Z']]
	if option.upper() == "ENCRYPT":
	    res = encrypt(tableau,msg,points,cols,rows)

	elif option.upper() == "DECRYPT":
	    res = decrypt(tableau,msg,points,cols,rows)
	return res

#print(bifid("ENCRYPT",msg))

#Alphagrader testing
lines = []
for line in fileinput.input():
    line = line.replace('\n','')
    lines.append(line)
    if(len(lines) == 2):
        print(bifid(lines[0],lines[1]))

