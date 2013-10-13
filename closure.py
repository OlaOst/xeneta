# A closure is a nested function that can access variables that have gone out
# of scope when it is called


# TODO: make more meaningful example
def makeClosure(text):
    textlength = len(text)
    def closure():
        print text + " is " + str(textlength) + " characters long"
    return closure

myClosure = makeClosure("hello world")
myClosure()
# at this point the textlength variable in the makeClosure function is out of
# scope, but myClosure can still access it - it 'encloses' the scope or context
# it was defined in
