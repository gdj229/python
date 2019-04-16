import re

def parsethroughregularexpression(sourcepath,targetpath,regularexpression):
    f=open(sourcepath)
    st=f.read()
    #rule_name=r'errorStatus: ([^,|N]*ERROR).*requestId: ([^,]*).*label: ([^,]*)'
    rule_name=r'(^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*errorStatus: ([^,|N]*ERROR).*requestId: ([^,]*).*label: ([^,]*)'
    #rule_name=r'errorStatus: (*((?<!NO_ERROR).)*).*requestId: ([^,]*).*label: ([^,]*)'
    compile_name = re.compile(rule_name, re.M)
    res_name = compile_name.findall(st)
    print(res_name[1])
    fl=open(r'E:\tmp\businesslog\result2.txt','w')
    for i in range(len(res_name)):
        s=str(res_name[i])
        fl.write(s)
        fl.write('\n')
    fl.close()

if __name__ == "__main__":
    sourcepath=input("please input the source file with full path:")
    targetpath=input("please input the target file with full path:")
    regularexpression=input("please input the regularexpression:")
    parsethroughregularexpression(sourcepath,targetpath,regularexpression)