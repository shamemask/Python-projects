a="^\n"
b_0_="/0\\\n"
b_1_="/1\\\n"
c="*---*\n"
bn="/"
bu="\\"
b_0_0="/0\\0"
b_0_1="/0\\1"
b_1_0="/1\\0"
b_1_1="/1\\1"
c2="*---"
t=" "
s=[64,63,62,57,56,55,54,33,32,31,30,25,24,23,22,61,60,59,58,53,36,35,34,29,28,27,26,21,52,51,50,37,44,43,42,45,20,19,18,49,40,39,38,41,48,47,46,17,16,15,14,9,8,7,6,13,12,11,10,5,4,3,2,1]
sa=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
sb=['0000','1000','0001','0010','0000','0010','1011','1011','0100','0101','0111','1111','1101','1110','0111','1111']
def expo(n1,k1,i1,x1,zed1):
    b1=t*(2*(n1-i1)-1)+"/"
    h=0
    while h < (2*i1+1):
        if h % 2 == 0:
            b1=b1+x1[-zed1]+bu
            zed1=zed1+1
        else:
            b1=b1+x1[-zed1]+bn
            zed1=zed1+1
        h=h+1
    b1=b1+"\n"
    
    c1=t*(2*(n1-1-i1))+c2*(n1-k1)+c
    return(b1+ c1)
def upcode(upc):
    if(len(upc)==64):
        upb=[]
        upb.append(upc[:4])
        upb.append(upc[4:8])
        upb.append(upc[8:12])
        upb.append(upc[12:16])
        upb.append(upc[16:20])
        upb.append(upc[20:24])
        upb.append(upc[24:28])
        upb.append(upc[28:32])
        upb.append(upc[32:36])
        upb.append(upc[36:40])
        upb.append(upc[40:44])
        upb.append(upc[44:48])
        upb.append(upc[48:52])
        upb.append(upc[52:56])
        upb.append(upc[56:60])
        upb.append(upc[60:])
        
    elif(len(upc)==16):
        upb=[]
        upb.append(upc[:4])
        upb.append(upc[4:8])
        upb.append(upc[8:12])
        upb.append(upc[12:])
        
    elif(len(upc)==4):
        upb=[]
        upb.append(upc)
    else:
        return(upc)
    iu=1
    while iu <= len(upb):
        ui=1
        kp=iu+1
        while iu != kp:
            
            if(upb[iu-1]==sa[ui-1]):
                upb[iu-1]=sb[ui-1]
                iu=iu+1
            ui=ui+1
    return(str(upb).replace(', ','').replace('[','').replace(']','').replace("'",''))
def decode(dec):
    i_s=len(dec)
    yap=''
    i_t=1
    while i_t <= i_s:
        kap=s[64-i_s+i_t-1]
        yap=yap+dec[i_s-(int(kap))]
        i_t=i_t+1
    return(yap)
def cell(x,n):
    if(len(x)>1):
        x=decode(x)
        
    x=str(x)
    if(n>0):
        y=''
        if(x[-1]=='0'):
            y=t*2*n+a+t*(2*n-1)+b_0_+t*2*(n-1)+c
        elif(x[-1]=='1'):
            y=t*2*n+a+t*(2*n-1)+b_1_+t*2*(n-1)+c
        
        i=1
        z=2
        
        while i < n:
            y=y+expo(n,n-i,i,x,z)
            i=i+1
            z=z+2*i-1
    else:
        y=''
        n=1
        if(x[-1]=='0'):
            y=t*2*n+a+t*(2*n-1)+b_0_+t*2*(n-1)+c
        elif(x[-1]=='1'):
            y=t*2*n+a+t*(2*n-1)+b_1_+t*2*(n-1)+c
    return(y)
x2="1101"
def zipping(zipl,nom1):
    kr=1
    ziplock=''
    if(zipl[:4]=='0000'):
        ziplock='0'
    if(zipl[:4]=='1111'):
        ziplock='1'
    if(nom1>=4):
        kr=4
        if(zipl[4:8]=='0000'):
            ziplock=ziplock+'0'
        if(zipl[4:8]=='1111'):
            ziplock=ziplock+'1'
        if(zipl[8:12]=='0000'):
            ziplock=ziplock+'0'
        if(zipl[8:12]=='1111'):
            ziplock=ziplock+'1'
        if(zipl[12:16]=='0000'):
            ziplock=ziplock+'0'
        if(zipl[12:16]=='1111'):
            ziplock=ziplock+'1'
        if(nom1>=8):
            kr=16
            if(zipl[16:20]=='0000'):
                ziplock=ziplock+'0'
            if(zipl[16:20]=='1111'):
                ziplock=ziplock+'1'
            if(zipl[20:24]=='0000'):
                ziplock=ziplock+'0'
            if(zipl[20:24]=='1111'):
                ziplock=ziplock+'1'
            if(zipl[24:28]=='0000'):
                ziplock=ziplock+'0'
            if(zipl[24:28]=='1111'):
                ziplock=ziplock+'1'
            if(zipl[28:32]=='0000'):
                ziplock=ziplock+'0'
            if(zipl[28:32]=='1111'):
                ziplock=ziplock+'1'
            if(zipl[32:36]=='0000'):
                ziplock=ziplock+'0'
            if(zipl[32:36]=='1111'):
                ziplock=ziplock+'1'
            if(zipl[36:40]=='0000'):
                ziplock=ziplock+'0'
            if(zipl[36:40]=='1111'):
                ziplock=ziplock+'1'
            if(zipl[40:44]=='0000'):
                ziplock=ziplock+'0'
            if(zipl[40:44]=='1111'):
                ziplock=ziplock+'1'
            if(zipl[44:48]=='0000'):
                ziplock=ziplock+'0'
            if(zipl[44:48]=='1111'):
                ziplock=ziplock+'1'
            if(zipl[48:52]=='0000'):
                ziplock=ziplock+'0'
            if(zipl[48:52]=='1111'):
                ziplock=ziplock+'1'
            if(zipl[52:56]=='0000'):
                ziplock=ziplock+'0'
            if(zipl[52:56]=='1111'):
                ziplock=ziplock+'1'
            if(zipl[56:60]=='0000'):
                ziplock=ziplock+'0'
            if(zipl[56:60]=='1111'):
                ziplock=ziplock+'1'
            if(zipl[60:]=='0000'):
                ziplock=ziplock+'0'
            if(zipl[60:]=='1111'):
                ziplock=ziplock+'1'
    if(kr==len(ziplock)):
        print(ziplock)
        print(cell(ziplock,nom1//2))
        return(ziplock)
    else:
        return(zipl)
def coding(code):
    code=str(code)
    while len(code)>1:
        if(len(code)>=64):
            nom=8
            zcode=code[-64:]
            code=code[:-64]
        elif(len(code)>=16):
            nom=4
            zcode=code[-16:]
            code=code[:-16]
        elif(len(code)>=4):
            nom=2
            zcode=code[-4:]
            code=code[:-4]
        elif(len(code)<4):
            ik=0
            nom=2
            while ik < (4-len(code)):
                code='0'+code
                ik=ik+1
            zcode=code
            code=''
        else:
            zcode=code
        print(zcode)
        print(cell(zcode,nom))
        zcode=zipping(zcode,nom)
        nom=0
        code=code+upcode(zcode)
        
    

print(coding('0100'))

input("Press Enter to continue...")
