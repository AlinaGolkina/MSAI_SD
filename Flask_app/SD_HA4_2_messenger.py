#SOLID Principles on classes

class user():
    def __init__(self, login, phone, gender, age):
        self.__login = login
        self.__phone = phone
        self.__gender = gender
        self.__age = age
        self.messages = []
        self.chats = []
    
    def __repr__(self):
        return self.login
        
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
        

class message():
    def __init__(self, user, messages):
        self.__user = user
        self.__messages = messages
        
    @property
    def user(self):
        return self.__user
    
    @user.setter
    def user(self, user: user):
        self.__user = user
        
    @user.deleter
    def user(self, name):
        del self.__user
        
    @property
    def messages(self):
        return self.__messages
    
    @messages.setter
    def messages(self, messages):
        self.__user = messages
        
    @messages.deleter
    def messages(self, messages):
        del self.__messages
        
        
class chat():
    def __init__(self, name, date):
        self.__name = name
        self.__date = date
        self.details = {}
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    @name.deleter
    def name(self, name):
        del self.__login
        
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        self.__date = date
        
    @date.deleter
    def date(self, date):
        del self.__date
        
    def add_users(self, user: user):
        self.details[user] = None
    
    def add_message(self, message: message):
        self.details[message.user] = message.messages
        message.user.messages.append(message.messages)
        
        
class messenger():
    def __init__(self):
        self.users = dict()
        self.phones = dict()
        self.chats = dict()
        self.messages = dict()
        self.chats = dict()
        
    def add_user(self, user: user, chat: chat):
        self.users[user] = user.login
        self.phones[user] = user.phone
        self.messages[user] = user.messages
        self.chats[user] = chat.name
            
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
    
    
user1 = user('Elena','7916000','female','21')
chat1 = chat('chat1','2022-01-01')
chat1.add_users(user1)

chat1.details
mes1 = message(user1, 'hello')
chat1.add_message(mes1)
chat1.details
user1.messages