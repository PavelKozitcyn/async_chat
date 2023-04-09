from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from tables import Client, Contact

Base = declarative_base()

class Storage:
    def __init__(self, app):
        self._engine = create_engine(f'sqlite:///{app}_db.sqlite')
        self._Session = sessionmaker(self._engine)

    def insert(self, BaseObject, *args):
        try:
            session = self._Session()
            obj = BaseObject(*args)
            session.add(obj)
            session.commit()
        except Exception as e:
            pass

    def delete(self, BaseObject, id):
        try:
            session = self._Session()
            session.query(BaseObject).filter_by(id=id).delete()
            session.commit()
        except Exception as e:
            pass

    def get_list(self, BaseObject):
        try:
            list = self._Session().query(BaseObject).all()
            return list
        except Exception as e:
            pass

class StorageServer(Storage):
    def __init__(self):
        super().__init__('server_pack')

class StorageClient(Storage):
    def __init__(self):
        super().__init__('client')

class ContactStorage(StorageServer):
    def __init__(self):
        super().__init__()

    def get_for_client(self, account_name):
        try:
            contacts = self._Session().query(Contact).filter(Contact.client.has(login=account_name)).all()
            return contacts
        except Exception as e:
            pass

    def get_by_client_and_contactee(self, client_id, contactee_client_id):
        try:
            contact = self._Session().query(Contact).filter(Contact.client_id==client_id, Contact.contactee_client_id==contactee_client_id).first()
            return contact
        except Exception as e:
            pass

class ClientStorage(StorageServer):
    def __init__(self):
        super().__init__()

    def get_by_account_name(self, account_name):
        try:
            client = self._Session().query(Client).filter(Client.login==account_name).first()
            return client
        except Exception as e:
            pass
