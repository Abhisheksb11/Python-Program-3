class Wordplay:
    def __init__(self,l):
        self.words=l

 

    def words_with_length(self,length):
        l =[]
        for word in self.words:
            if(len(word)==length):
                l.append(word)
        return l

 

    def starts_with(self,s):
        l=[]
        s= s.lower()
        for word in self.words:
            i = word[0].lower()
            if(i==s):
                l.append(word)
        return l

 

    def ends_with(self,s):
        l=[]
        s=s.lower()
        for word in self.words:
            i= word[-1].lower()
            if(i==s):
                l.append(word)
        return l

 

    def palindromes(self):
        l=[]
        for word in self.words:
            if(word == word[::-1]):
                l.append(word)
        return l

 

    def only(self,L):
        l=[]
        for word in self.words:
            addword = True
            for letter in word:
                if(letter not in L):
                    addword = False
                break
            if(addword):
                l.append(word)
        return l

 

    def avoids(self,L):
        l=[]
        for word in self.words:
            addword = True
            for letter in word:
                if(letter in L):
                    addword = False
                break
            if(addword):
                l.append(word)
        return l

 

w1=Wordplay(["manipal","bengaluru","mangalore","Udupi","sirsi","Delhi","madam"])
l=w1.words_with_length(9)
print("A)")
print("Words with length {0} is {1}".format(9,l))
l = w1.starts_with('m')

print("B)")
print("Words which start with letter {0} is {1}".format('M',l))
l=w1.ends_with('i')

print("C)")
print("The words which ends with {0} is {1}".format('i',l))


print("D)")
l = w1.palindromes()

print("The words which are palindromes are {0}".format(l))
print("E)")
l = w1.only(['i','r','s'])

print(l)
print("F)")
l= w1.avoids(['s'])
print(l)
