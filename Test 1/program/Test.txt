import datetime
now = datetime.datetime.now()

def FileTest(a,b,c_done,c_undone,time):
    my_file = open(b+"_"+time+".txt", "w+")
    my_file.write("# Сотрудник №"+a+"\n")
    my_file.write(now.strftime("%Y.%m.%d %H:%M")+"\n"+"\n")
    my_file.write("## Завершённые задачи:"+"\n")
    my_file.write(c_done+"\n"+"\n")
    my_file.write("## Оставшиеся задачи:"+"\n")
    my_file.write(c_undone)
    my_file.close()
    
def FileData(f):
    
    data_File = []
    for line in f:
        line = line[4:-1]
        line = line.replace("\"","")
        line = line.replace(",","")
        line = line.split("\t")
        if line!=['']:
            data_File.append(line)
    return(data_File)

def SborData(i_sbor,data_sbor):
    sbor=[]
    if i_sbor >= 0:
        if str(data_sbor[i_sbor-1]).count("userId")>0:
            sbor.append(data_sbor[i_sbor-1])
        else:
            sbor.append('')
    else:
        sbor.append('')
    sbor.append(data[i_sbor])
    if i_sbor+2 <= len(data_sbor):
        if str(data_sbor[i_sbor+1]).count("title")>0:
            sbor.append(data_sbor[i_sbor+1])
        else:
            sbor.append('')
    else:
        sbor.append('')
    if i_sbor+3 <= len(data_sbor):
        if str(data_sbor[i_sbor+2]).count("completed")>0:
            sbor.append(data_sbor[i_sbor+2])
        else:
            sbor.append('')
    else:
        sbor.append('')
    return(sbor)


file = open('todos.json','r')
data=FileData(file)
i=0
c_done_test=''
c_undone_test=''
while i != len(data):
    if str(data[i]).count('id:')>0:
        sbor_test=SborData(i,data)
        a_test=str(sbor_test[0]).strip("['userId: ").strip("']")
        b_test=str(sbor_test[1]).strip("['id: ").strip("']")
        c_test=str(sbor_test[2]).strip("['title: ").strip("']")
        if len(c_test)>50:
            c_test=c_test[:49]+"..."
        d_test=str(sbor_test[3]).strip("['completed:").strip("']")
        time=str(now.strftime('%Y-%m-%dT%H-%M'))
        if d_test==' true':
            c_done_test=c_done_test+c_test+"\n"
        else:
            c_undone_test=c_undone_test+c_test+"\n"
        FileTest(a_test,b_test,c_done_test,c_undone_test,time)
        sbor_test=[]
    i=i+1
    
