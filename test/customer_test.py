from controller import CustomerController

# todo : error
#CustomerController.save("ali","abedi","aliiiabedi","ali123",
            #            "gharb",123456789,12345678)

CustomerController.save("reza","rezaii","rez","reza123",
                        "shargh",123456788,12345677)

CustomerController.save("hamed","hamedi","hm","hamed123",
                        "gharb",123456778,12342677)

CustomerController.save("sara","nazemi","snazemi","sara123",
                        "jonob",123336778,13332677)


CustomerController.edit(2,"hassan","hasani","hsan","hamed123",
                        "gharb",123456778,12342677)


CustomerController.remove(3)

CustomerController.find_all()

CustomerController.find_by_id(2,)

CustomerController.find_by_family("rezaii")

CustomerController.find_by_name("reza")

CustomerController.find_by_username("rez")
CustomerController.find_by_password("reza123")

# todo : find by username, usernameandpassword,