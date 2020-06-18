from uuid import uuid4
import datetime
class Account:
    def __init__(self,idAccount=None,firstName=None,lastName=None,email=None,
        password=None,userName=None,gender=None,birthday=None,cover=None,
        created=None, updated=None):
        self.idAccount =idAccount
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.userName = userName
        self.gender = gender
        self.birthday = birthday
        self.cover = cover
        self.createdDate = created
        self.updatedDate = updated

    @classmethod
    def create(cls, firstName, lastName, email, password, userName, gender, birthday, cover):
        newId = str(uuid4())
        created = datetime.datetime.utcnow()
        newAccount = Account(newId,firstName,lastName,email,password,userName,gender,birthday,cover,created,None)
        return newAccount
    
    