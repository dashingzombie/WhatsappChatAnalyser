import pandas as pd

fh = open("final.txt")
date = list()
time = list()
name = list()
text = list()
q = ":"
a =0
for line in fh:
    if not line[0].isdigit():
        continue
    pos=line.find(",");
    x=line[:pos]
    if x[0].isdigit():
        date.append(x);
    pos1 = line.find("-")
    t = line[pos+1:pos1];
    t = t.strip()
    if t[0].isdigit():
        time.append(t);
    line = line[pos1+2:]
    if q in line:
        pos2 = line.find(":")
        n = line[:pos2]
        name.append(n)
        pos3=line.find("\n")
        line = line[pos2+2:pos3]
        line.rstrip();
        text.append(line);

data = pd.DataFrame(list(zip(date,time,name,text)), columns =['Date', 'Time','Name','Text'])
data.to_excel("chat.xlsx")
