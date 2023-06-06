import json

class Read_CV_Data:
    __instance = None
    cv_data = None
    
    @staticmethod
    def get_instance():
        if Read_CV_Data.__instance is None:
            Read_CV_Data()
        return Read_CV_Data.__instance

    def __init__(self):
        if Read_CV_Data.__instance is not None:
            raise Exception("Singleton class cannot be instantiated multiple times")
        else:
            Read_CV_Data.__instance = self
            self.data = None

    def retrive_data(self):
        if self.cv_data is None:
            self.cv_data =  json.load(open('data.json'))
        return self.cv_data




