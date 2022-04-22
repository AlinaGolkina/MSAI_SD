# Section 2. Classes
# Var2 (a messenger):
# Compare messengers by users (or chats, or messages) count (A > B = False)
# Get messengers unique users difference/union/intersection by phone (or email address) (A - B = {'+790324...', ...}

class user():
    def __init__(self, login, phone, gender, age, messages=list, chats=list):
        self.__login = login
        self.__phone = phone
        self.__gender = gender
        self.__age = age
        self.messages = messages
        self.chats = chats
        
    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self, login):
        self.__login = login
        
    @login.deleter
    def login(self, login):
        del self.__login
        
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self):
        self.__phone = phone
    
    @phone.deleter
    def phone(self):
        del self.__phone
    
    @property
    def gender(self):
        return self.__gender
    
    @gender.setter
    def gender(self):
        self.__gender = gender
        
    @gender.deleter
    def gender(self):
        del self.__gender
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self):
        self.__age = age
    
    @age.deleter
    def age(self):
        del self.__age

        
class messenger():
    def __init__(self):
        self.users = dict()
        self.phones = dict()
        self.chats = dict()
        self.messages = dict()
        self.chats = dict()
        
    def add_user(self, user):
        self.users[user] = user.login
        self.phones[user] = user.phone
        self.messages[user] = user.messages
        self.chats[user] = user.chats
            
    # Find messages with some word combination
    def find_message(self, key_word: str):
        find_messages = []
        for user in self.users:
            for message in self.messages[user]:
                if key_word in message:
                    find_messages.append(message)
        if len(find_messages) == 0:
            print('there is no messages with key_words {key_words}')
        return find_messages    
         
    def __eq__(self, other):
        return len(self.users.keys()) == len(other.users.keys())
    
    def __gt__(self, other):
        return len(self.users.keys()) > len(other.users.keys())
    
    def __lt__(self, other):
        return len(set(self.users)) < len(set(other.users))
    
    def __le__(self, other):
        return len(set(self.users)) <= len(set(other.users))
    
    def intersection(self, other):
        return set(self.phones.values()) & set(other.phones.values())
    
    def difference(self, other):
        return set(self.phones.values()) - set(other.phones.values())
    
    def union(self, other):
        return set(self.phones.values()) | set(other.phones.values())
 
# create users
user1 = user('Elena','7916000','female','18',['ok','no'])
user2 = user('Marina','7925000','female','20',['ok'])
user3 = user('Alina','7928000','female','30',['yes'])
user4 = user('Ekaterina','7925000','female','35',['ok'])

# create first messenger
mes1 = messenger()
mes1.add_user(user1)
mes1.add_user(user2)

# create second messenger
mes2 = messenger()
mes2.add_user(user3)
mes2.add_user(user4)
mes2.add_user(user1)

print('finding messages with key_word' ,mes1.find_message('ok'))
print(f'phones union, {mes1.union(mes2)}')
print(f'phones intersection, {mes1.intersection(mes2)}')