import urllib2
import fnmatch
import os
#find a file
hope='a'
drive=raw_input('ENTER THE DRIVE NAME: ')
deive=drive.lower()
if drive=='desktop':
    drive1='C:\Users\Vishal Jain\Desktop/'
else:
    drive1=drive+':/'
print 'ENTER THE FILE NAME : '
filenam=raw_input()
ann=''
tag=''
try:
    try:
        rootPath = drive1
        pattern = filenam
        for root, dirs, files in os.walk(rootPath):
            if tag=='y' or tag=='Y':
                 break
            for filename in fnmatch.filter(files, pattern):
                print( os.path.join(root, filename))
                tag=raw_input('PRESS Y IF THIS FILE IS CORRECT ELSE PRESS N: ')
                if tag=='y' or tag=='Y':
                    hope= os.path.join(root, filename)
                    break
                elif tag=='n' or tag=='N':
                    continue
                
                                
                
                    
                        
        fil1=open(hope)
        print '-------------------FILE FOUND ------------------------------'
        text1=fil1.read()
        fil1.close()
    except:
        print 'FILE NOT FOUND <PLEASE CHECK THE FILE EXIST IN DRIVE G AND THE TRY AGAIN> '
    
    leng=len(text1)
    #if(text1[leng-1])=='\n':
    text3=text1.strip('\n')
    text2=text3+'\n^\n'
    word1=''

    l=0;

    
    while text2[l]!='^':
        k=l
        if text2[l]=='\n':
            l=l+1
            k=l
        while text2[l]!='\n':
            l=l+1
        word2=text2[k:l]
        word2=word2.strip(' ')
        
        if word2=='^':
            break
        if 'http://' in word2:
            word3=word2
        elif 'https://' in word2:
            word3=word2
        else:
            word3='http://'+word2
        if word3=="http://\n": continue
        
        if (word3=='http://'):
            continue
        elif (word3=='http:// '):
            continue
        else:
            print word3
        
        
    #URL BEGIN
    #resp=urllib2.urlopen(word3)
    #result=resp.read()
        try:
            try:
                opener = urllib2.build_opener()
                opener.addheaders = [('User-Agent', 'chrome')]
                response = opener.open(word3)
                result=response.read();
            except:
                resp=urllib2.urlopen(word3)
                result=resp.read()
        except:
            print'website not found'
            print'------------------------------------------------------------'
            continue
            
    
        search='" name="description"></meta'
        search1='meta name="description" content="'
        search2='<meta name="description" content="'
    

    
        termination='\"'
        if search in result:
        
            end=result.find('" name="description">')
            start=end
            while result[start]!='"':
                start=start-1
            final=result[start:end]
        elif search1 in result:
        
            location=result.find('meta name="description" content="')
        
            
         
            start=location+33
            end=start
            while result[end]!=termination:
                end=end+1
            final=result[start:end]
            if '<meta name="description" content="" />' in result:
            
                final=result
        elif search2 in result:
        
            location=result.find('<meta name="description" content="')
        
            
         
            start=location+33
            end=start
            while result[end]!=termination:
                end=end+1
            final=result[start:end]
        
        else:
            #label(nxt)
        
            final=result
        

    
        final1=final.lower()
    
        # FILE BEGIN
        fil=open('vishal1.txt')
        text=fil.read()
        fil.close()
        word=''
            
        i=0;
        count=0
        while text[i]!='.':
            j=i
            while text[i]!='\n':
                i=i+1
            word=text[j:i]
       
            if text[i]=='\n':
                i=i+1
            word1=word.lower()
        
            wd=final1.find(word1)
            if (final1.find(word1)!=-1):
                if (final1[wd-7:wd+8])!='troubleshooting':
                    
                    count=1+count
                    wordf=word
            
            
            
        

        if count==0 or count>1:
            print 'N/A'
        elif count==1:
            print wordf
        count=0
      
        print'------------------------------------------------------------'
    hg=raw_input('PRESS ANY KEY ')
except:
    print 'N/A'
    
    hn=raw_input('PRESS ANY KEY')
