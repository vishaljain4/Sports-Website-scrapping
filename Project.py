import urllib2
import fnmatch
import os
print 'enter the name of the file'
filenam=raw_input()
rootPath = "D:/"
pattern = filenam
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))
        hope=(os.path.join(root, filename))
fil1=open(hope)
print '-----file found-----'
text1=fil1.read()
text2=text1+'\n^\n'
word2=''
print text2

l=0
while '\n^\n' in text2:
    k=l
    
    while text2[l]!='\n':
        l=l+1
        m=l
    l=l+1
    word2=text2[k:m]
    
    if word2=='^':
        break
    if 'http://' in word2:
        word3=word2
        print word3
        resp=urllib2.urlopen(word3)
        result=resp.read()

    
        search='" name="description"></meta>'
        search1='meta name="description" content="'
    
        termination
        if search in result:
            print 'first one'
            end=result.find('" name="description">')
            start=end
            while result[start]!='"':
                start=start-1
            final=result[start:end]
        elif search1 in result:
            print 'second one'
            location=result.find('meta name="description" content="')
            print location
            start=location+33
            end=start
            while result[end]!=termination:
                end=end+1
            final=result[start:end]
        else:
            print 'last'
            final=result

    
        final1=final.lower()
    elif 'https://' in word2:
        word3=word2
        print word3
        resp=urllib2.urlopen(word3)
        result=resp.read()

    
        search='" name="description">'
        search1='meta name="description" content="'
    
        termination='\"'
        if search in result:
            print 'first one'
            end=result.find('" name="description">')
            start=end
            while result[start]!='"':
                start=start-1
            final=result[start:end]
        elif search1 in result:
            print 'second one'
            location=result.find('meta name="description" content="')
            print location
            start=location+33
            end=start
            while result[end]!=termination:
                end=end+1
            final=result[start:end]
        else:
            print 'last'
            final=result

    
        final1=final.lower()
    else:
        try:
            word3='http://'+word2
    
            print 'url begin'         
            #URL BEGIN
            print word3
            resp=urllib2.urlopen(word3)
            result=resp.read()

    
            search='" name="description">'
            search1='meta name="description" content="'
    
            termination='\"'
            if search in result:
                print 'first one'
                end=result.find('" name="description">')
                start=end
                while result[start]!='"':
                    start=start-1
                final=result[start:end]
            elif search1 in result:
                print 'second one'
                location=result.find('meta name="description" content="')
                print location
                start=location+33
                end=start
                while result[end]!=termination:
                    end=end+1
                final=result[start:end]
            else:
                print 'last'
                final=result

    
            final1=final.lower()
        except:
            word3='https://'+word2
    
            print 'url begin'         
        #URL BEGIN
            resp=urllib2.urlopen(word3)
            result=resp.read()
    
            search='" name="description">'
            search1='meta name="description" content="'
    
            termination='\"'
            if search in result:
                end=result.find('" name="description">')
                start=end
                while result[start]!='"':
                    start=start-1
                final=result[start:end]
            elif search1 in result:
                location=result.find('meta name="description" content="')
                print location
                start=location+33
                end=start
                while result[end]!=termination:
                    end=end+1
                final=result[start:end]
            else:
                final=result

    
            final1=final.lower()
            print final1
        
# FILE BEGIN
    fil=open('vishal1.txt')
    text=fil.read()
    fil.close()
    word=''

    i=0;

    while text[i]!='.':
        j=i
        while text[i]!='\n':
            i=i+1
        word=text[j:i]
        if text[i]=='\n':
            i=i+1
        word1=word.lower()
        if word1 in final1:
            print word
            count=1
            break
        else:
            count=0

    if count==0:
        print 'NA'
