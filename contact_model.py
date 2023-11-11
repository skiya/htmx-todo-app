import json
import typing


class Contact:
    db: dict[int, typing.Self] = {}
    
    def __init__(self, id_: int=None, fullname: str=None, tel: str=None, email: str=None) -> None:
        self.id = id_
        self.fullname = fullname
        self.tel = tel
        self.email = email
    
    def __str__(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=False)
    
    @classmethod
    def all(cls) -> list[typing.Self]:
        return cls.db.values()
    
    @classmethod
    def search(cls, query: str) -> list[typing.Self]:
        result: list[typing.Self] = []
        for c in cls.db.values():
            match_name = c.fullname is not None and query in c.fullname
            match_tel = c.tel is not None and query in c.tel
            match_email = c.email is not None and query in c.email
            if match_name or match_tel or match_email:
                result.append(c)
        return result
    
    @classmethod
    def load_db(cls):
        with open('contacts.json', 'r') as contacts_persist:
            contacts = json.load(contacts_persist)
            cls.db.clear()
            for c in contacts:
                cls.db[c['id']] = Contact(c['id'], c['fullname'], c['tel'], c['email'])
