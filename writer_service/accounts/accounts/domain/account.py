from uuid import uuid4
import datetime
import hashlib
class Account:
    TYPE_REGISTER = {
        "System": 1,
        "Facebook": 2
    }
    def __init__(self,idAccount=None,firstName=None,lastName=None,email=None,
        password=None,userName=None,gender=None,birthday=None,cover=None,
        created=None, updated=None,contentCreator:bool=False,typeRegister=None):
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
        self.contentCreator: bool = contentCreator
        self.typeRegister = typeRegister

    @classmethod
    def create(cls, firstName, lastName, email, password, userName, gender, birthday, cover,typeRegister):
        newId = str(uuid4())
        if typeRegister == "System":
            password_encoded = cls.encode(cls,password)

        created = datetime.datetime.utcnow()
        idtypeRegister = cls.TYPE_REGISTER[typeRegister]
        newAccount = Account(newId,firstName,lastName,email,password_encoded,userName,gender,birthday,cover,created,None,False,idtypeRegister)
        return newAccount

    def encode(self, password:str):
        print("Encoding password")
        pass_sha = hashlib.sha256(password.encode('utf-8'))
        pass_sha_hex = pass_sha.hexdigest()
        return pass_sha_hex
    
    def to_json(self):
        account_to_json = {
            "idAccount": self.idAccount,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "userName": self.userName,
            "gender": self.gender,
            "birthday": self.birthday,
            "created": self.createdDate
        }
        return account_to_json
    
    