import uuid
class user:
    def __init__(self,name, phone, email, aadhar, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.aadhar = aadhar
        self.address = address
        self.name=None
    
    def validate_user(self):
        self.name.isalpha(),
        self.phone.isdigit() and len(self.phone) == 10,
        "@" in self.email,
        self.aadhar.isdigit() and len(self.aadhar) == 12


        return True
   
    def add_user(self, users_data):
        data = {
            "id": uuid.uuid1(),
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "aadhar": self.aadhar,
            "address": self.address,
            
            "status": 1}
        users_data.append(data)
        return True
   