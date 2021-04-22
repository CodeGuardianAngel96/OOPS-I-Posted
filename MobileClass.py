'''

    Write a class with name Mobile. 
    It contains a method called hi() which contains two
    parameters msg and app which is initialized to None. 
    If no parameter is sent then hi() should print hai ,
    if a parameter is sent then it should print hai and the parameter also.
'''

class Mobile:

    def hi(self, msg = None, app = None):

        if msg == None:

            msg = ""
        if app == None:

            app = ""

        string = "hai " + str(msg) + " " + str(app)
        print(string)

if __name__ == "__main__":

    mobile = Mobile()
    
    mobile.hi()
    mobile.hi("roshan")
    mobile.hi("oops", "!")