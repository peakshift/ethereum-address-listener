from tinydb import TinyDB


class Database:
    def __init__(self):
        self.db = TinyDB('./db.json')

    def insert(self, collection: str, data: dict) -> bool:
        try:
            project_id: int = self.db.table(collection).insert(data)
            return True
        except:
            return None

    def get(self, collection: str) -> list:
        try:
            projects: list = self.db.table(collection).all()
            return projects
        except:
            return None

    def get_by_id(self, collection: str, project_id: int) -> dict:
        try:
            project: dict = self.db.table(collection).get(doc_id=project_id)
            return project
        except:
            return None

    def update(self, collection: str, data: dict, project_id: int) -> bool:
        try:
            self.db.table(collection).update(data, doc_ids=[project_id])
            return True
        except:
            return False

    def delete(self, collection: str, project_id: int) -> bool:
        try:
            self.db.table(collection).remove(doc_ids=[project_id])
            return True
        except:
            return False
