#function is a first class object

def double_decker():
    print('Starting the double decker')
    def inner_fun():
        print('inside the inner')
        return 5000
    return inner_fun

# print(double_decker()())

def do_something(work):
    print('work started')
    work()
    print('work ended')
    
# do_something(2)
# do_something('ami busy')

def Coding():
    print('coding in python')

# Coding()
# print(Coding())

# do_something(Coding)
def slepping():
    print('sleeping and dreaming ')

do_something(slepping)