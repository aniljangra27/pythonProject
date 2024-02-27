# RandomUser is an open-source, free API providing developers with randomly generated users to be used as placeholders for testing purposes
# ref: https://randomuser.me/documentation
# Install randomuser first: pip install randomuser and then use it
# load the necessary libraries

from randomuser import RandomUser
import pandas as pd

# create a random user object, r.
r = RandomUser()

# generate 10 user using generate_users() function
userList1 = r.generate_users(10)
print(r.get_full_name())    # get full name
print(userList1.__getitem__(0).get_age())

# print name and age from the user list
for user in userList1:
    print(user.get_full_name(), "", user.get_age())

# Display data in tabular structure
print("\n -----------Import in Table structure------------------")
def get_Users():
    users = []
    for user in RandomUser.generate_users(5):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob()})

    return pd.DataFrame(data= users)

print(get_Users())

