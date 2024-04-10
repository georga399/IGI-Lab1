from .ISerializer import ISerializer
import pickle

class PickleSerializer(ISerializer):
    '''Serializer using pickle module.'''
    @staticmethod
    def SerializeToFile(objs:list, filename:str):
        with open(filename, "wb") as f:
            bts = pickle.dumps(objs)
            f.write(bts)
    
    @staticmethod
    def DeserializeFromFile(filename:str) -> list:
        try:
            with open(filename, "rb") as f:
                bts = f.read()
                return pickle.loads(bts)
        except FileNotFoundError:
            return []