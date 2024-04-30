class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Please enter some name in here!!")
        
        self.__name = value
        
    @property
    def member_id(self):
        return self.__member_id
    
    @member_id.setter
    def member_id(self, value):
        if not value.strip():
            raise ValueError("Please enter some member_id!!")

        self.__member_id = value

    def representing_member(self):
        return f"This is member with name {self.name} and member_id: {self.member_id}"