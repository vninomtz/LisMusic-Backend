from uuid import uuid4

class Account:
    def __init__(self,idAccount,firstName,lastName,email,
        password,userName,gender,birthday,cover):
        self.idAccount =idAccount
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.userName = userName
        self.gender = gender
        self.birthday = birthday
        self.cover = cover

    @classmethod
    def create(cls, firstName, lastName, email, password, userName, gender, birthday, cover):
        newId = uuid4()
        newAccount = Account(newId,firstName,lastName,email,password,userName,gender,birthday,cover)
        return newAccount
    
    