# Import required module
import phonenumbers
from phonenumbers import geocoder,carrier

class phoneNumbers:
    '''Class to give the user's country using country code also to give the name of service provider'''

            
    def country_name(self,your_number):
        self.Your_number = your_number

        phone_object = phonenumbers.parse(your_number, 'CH')
        print(geocoder.description_for_number(phone_object, 'en'))

        
    def service_provider(self,your_number):
        self.Your_number = your_number

        serviceProvider = phonenumbers.parse(your_number, 'RO')
        print(carrier.name_for_number(serviceProvider, 'en'))

    

# instance of class 
user = phoneNumbers()

if __name__ == "__main__":

    try:
        user.country_name(your_number='#')
        user.service_provider(your_number='#')
        print("Code Completed 🔥")
    
    except Exception as e:
        print('Something Went Wrong 💢', e)