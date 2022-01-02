import time
class User:
    def __init__(self,nom,email):
        self.nick=nom
        self.email=email
        self.fans={}
        self.posts=[]
        self.__blocked=[]
    def show(self):
        return "nick-->"+self.nick+"\n"+"email-->"+self.email+"\n"+"Fans_list_nicks -->"+",".join([nick for nick in self.fans]) if len(self.fans)!=0 else "no fans yet" +"\n"+"\n".join(self.posts) if len(self.posts)!=0 else "no posts yet"
    def addFan(self,p):
        if p.nick not in self.__blocked:
            self.fans[p.nick]=p
    def checkFanInfo(self,fan):
        pass
    def listFans(self):
        return "\n".join([fan.show()+"\n----" for fan in self.fans.values()])
    def blockUser(self, user):
        if user in self.fans:       
            del self.fans[user]
        self.__blocked.append(user)
    def listBlocked(self):
        return "blocked users --> "+",".join(self.__blocked) if len(self.fans)!=0 else "no blocked users yet"

class Post: # apartat b)
    def __init__(self,text,date):
        self.content=text
        self.date=date
        self.hashtags=[] 
        self.friends=[]
        
    def show(self):
        return "Content --> "+self.content+"\n""Date --> "+self.date+"\n"+"Hashtags --> "+" ".join(self.hashtags) if len(self.hashtags)!=0 else "Not hastags yet"+"\n"+" ".join(self.friends) if len(self.friends)!=0 else " No friends Yet"
    def addHashtag(self,h):
        self.hashtags+=[h]
    def addFriend(self,f):
        self.friends+=[f]