# Cole Logan

from psItems import Value, ArrayValue, FunctionValue
class Operators:
    def __init__(self):
        #stack variables
        self.opstack = []  #assuming top of the stack is the end of the list
        self.dictstack = []  #assuming top of the stack is the end of the list
        
        #The builtin operators supported by our interpreter
        self.builtin_operators = {
             # TO-DO in part1
             # include the key value pairs where he keys are the PostScrip opertor names and the values are the function values that implement that operator. 
             # Make sure **not to call the functions** 
             "add": self.add,
             "sub": self.sub,
             "mul": self.mul,
             "mod": self.mod,
             "lt": self.lt,
             "gt": self.gt,
             "eq": self.eq,
             "length": self.length,
             "getinterval": self.getinterval,
             "putinterval": self.putinterval,
             "aload": self.aload,
             "astore": self.astore,
             "dup": self.dup,
             "copy": self.copy,
             "count": self.count,
             "pop": self.pop,
             "clear": self.clear,
             "exch": self.exch,
             "roll": self.roll,
             "stack": self.stack,
             "dict": self.psDict,
             "begin": self.begin,
             "end": self.end,
             "def": self.psDef,
             "array": self.array,
             "cleanTop": self.cleanTop,
             "if": self.psIf,
             "ifelse": self.psIfelse,
             "for": self.psFor,
             "repeat": self.repeat,
             "forall": self.forall
        }
    #-------  Operand Stack Operators --------------
    """
        Helper function. Pops the top value from opstack and returns it.
    """
    def opPop(self):
        # check if opstack is empty, return none if it is
        if self.opstack:
            return self.opstack.pop()
        else:
            return None

    """
       Helper function. Pushes the given value to the opstack.
    """
    def opPush(self,value):
        self.opstack.append(value)
        
    #------- Dict Stack Operators --------------
    
    """
       Helper function. Pops the top dictionary from dictstack and returns it.
    """   
    def dictPop(self):
        # check if dictstack is empty, return none if it is
        if self.dictstack:
            return self.dictstack.pop()
        else:
            return None

    """
       Helper function. Pushes the given dictionary onto the dictstack. 
    """   
    def dictPush(self,d):
        self.dictstack.append(d)

    """
       Helper function. Adds name:value pair to the top dictionary in the dictstack.
       (Note: If the dictstack is empty, first adds an empty dictionary to the dictstack then adds the name:value to that. 
    """   
    def define(self,name, value):
        # check if dictstack is empty
        if self.dictstack:
            dct = self.dictstack.pop() # get top dict then add name value pair
            dct[name] = value
            self.dictstack.append(dct) # put dict back on top of stack
        else:
            newDict = {} # create new dict and add name value pair
            newDict[name] = value
            self.dictstack.append(newDict) # put new dict on top of stack


    """
       Helper function. Searches the dictstack for a variable or function and returns its value. 
       (Starts searching at the top of the dictstack; if name is not found returns None and prints an error message.
        Make sure to add '/' to the begining of the name.)
    """
    def lookup(self,name):
        slash = '/' + name # append / to the beginning of the name
        self.dictstack.reverse()
        for dct in self.dictstack:
            if slash in dct.keys(): # search for name in keys, return value if found
                self.dictstack.reverse()
                return dct[slash]
        self.dictstack.reverse()
        print("Error: given name does not exist in dictstack")
        return None
    
    #------- Arithmetic Operators --------------
    
    """
       Pops 2 values from opstack; checks if they are numerical (int); adds them; then pushes the result back to opstack. 
    """   
    def add(self):
        if len(self.opstack) > 1:
            op1 = self.opPop() # top value
            op2 = self.opPop() # bottom value
            if isinstance(op1,int) and isinstance(op2,int):
                self.opPush(op1 + op2)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op2)  # bottom value
                self.opPush(op1)   # top value
        else:
            print("Error: add expects 2 operands")
 
    """
       Pop 2 values from opstack; checks if they are numerical (int); subtracts them; and pushes the result back to opstack. 
    """   
    def sub(self):
        if len(self.opstack) > 1:
            op1 = self.opPop() # top value
            op2 = self.opPop() # bottom value
            if isinstance(op1, int) and isinstance(op2, int):
                self.opPush(op2 - op1)
            else:
                print("Error: sub - one or both of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)
        else:
            print("Error: sub expects 2 operands")

    """
        Pops 2 values from opstack; checks if they are numerical (int); multiplies them; and pushes the result back to opstack. 
    """    
    def mul(self):
        if len(self.opstack) > 1:
            op1 = self.opPop() # top value
            op2 = self.opPop() # bottom value
            if isinstance(op1, int) and isinstance(op2, int):
                self.opPush(op1 * op2)
            else:
                print("Error: mul - one or both of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)
        else:
            print("Error: mul expects 2 operands")

    """
        Pops 2 values from stack; checks if they are int values; calculates the remainder of dividing the bottom value by the top one; 
        pushes the result back to opstack.
    """ 
    def mod(self):
        if len(self.opstack) > 1:
            op1 = self.opPop() # top value
            op2 = self.opPop() # bottom value
            if isinstance(op1, int) and isinstance(op2, int):
                self.opPush(op2 % op1)
            else:
                print("Error: mod - one or both of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)
        else:
            print("Error: mod expects 2 operands")
    #---------- Comparison Operators  -----------------
    """
       Pops the top two values from the opstack; pushes "True" is they are equal, otherwise pushes "False"
    """ 
    def eq(self):
        if len(self.opstack) > 1:
            op1 = self.opPop() # top value
            op2 = self.opPop() # bottom value
            self.opPush(op1 == op2)
        else:
            print("Error: eq expects 2 operands")

    """
       Pops the top two values from the opstack; pushes "True" if the bottom value is less than the top value, otherwise pushes "False"
    """ 
    def lt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop() # top value
            op2 = self.opPop() # bottom value
            self.opPush(op2 < op1)
        else:
            print("Error: lt expects 2 operands")

    """
       Pops the top two values from the opstack; pushes "True" if the bottom value is greater than the top value, otherwise pushes "False"
    """ 
    def gt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop() # top value
            op2 = self.opPop() # bottom value
            self.opPush(op2 > op1)
        else:
            print("Error: gt expects 2 operands")

    # ------- Array Operators --------------
    """ 
       Pops the array length (an int value) from the opstack and initializes an array constant (ArrayValue) having the given length. 
       Initializes the elements in the value of the ArrayValue to None. Pushes the ArrayValue to the opstack.
    """
    def array(self):
        if len(self.opstack) > 0:
            length = self.opPop()
            arr = []
            for i in range(length):
                arr.append(None)
            #arr.reverse()
            self.opPush(ArrayValue(arr))
        else:
            print("Error: array expects an operand")

    """ 
       Pops an array value from the operand opstack and calculates the length of it. Pushes the length back onto the opstack.
       The `length` method should support ArrayValue values.
    """
    def length(self):
        if len(self.opstack) > 0:
            arrval = self.opPop()
            if isinstance(arrval, ArrayValue):
                self.opPush(len(arrval.value))
            else:
                self.opPush(len(arrval))
        else:
            print("Error: length expects an operand")

    """ 
        Pops the `count` (int), an (zero-based) start `index`, and an array constant (ArrayValue) from the operand stack.  
        Pushes the slice of the array of length `count` starting at `index` onto the opstack.(i.e., from `index` to `index`+`count`) 
        If the end index of the slice goes beyond the array length, will give an error. 
    """
    def getinterval(self):
        if len(self.opstack) > 2:
            count = self.opPop()
            index = self.opPop()
            arr = self.opPop()
            if len(arr.value) > (index+count-1):
                newarr = arr.value[index:index+count]
                self.opPush(ArrayValue(newarr))
            else:
                print("Error: getinterval - end index goes beyond array length")
        else:
            print("Error: getinterval expects 3 operands")

    """ 
        Pops an array constant (ArrayValue), start `index` (int), and another array constant (ArrayValue) from the operand stack.  
        Replaces the slice in the bottom ArrayValue starting at `index` with the top ArrayValue (the one we popped first). 
        The result is not pushed onto the stack.
        The index is 0-based. If the end index of the slice goes beyond the array length, will give an error. 
    """
    def putinterval(self):
        if len(self.opstack) > 2:
            arr1 = self.opPop()
            index = self.opPop()
            arr2 = self.opPop()
            if len(arr2.value) > (len(arr1.value)-index-1):
                arr2.value[index:index+len(arr1.value)] = arr1.value
            else:
                print("Error: putinterval - index goes beyond array length")
        else:
            print("Error: putinterval expects 3 operands")
            

    """ 
        Pops an array constant (ArrayValue) from the operand stack.  
        Pushes all values in the array constant to the opstack in order (the first value in the array should be pushed first). 
        Pushes the orginal array value back on to the stack. 
    """
    def aload(self):
        if len(self.opstack) > 0:
            arr = self.opPop()
            for item in arr.value:
                self.opPush(item)
            self.opPush(arr)
        else:
            print("Error: aload expects an operand")
        
    """ 
        Pops an array constant (ArrayValue) from the operand stack.  
        Pops as many elements as the length of the array from the operand stack and stores them in the array constant. 
        The value which was on the top of the opstack will be the last element in the array. 
        Pushes the array value back onto the operand stack. 
    """
    def astore(self):
        if len(self.opstack) > 0:
            arr = self.opPop()
            if isinstance(arr, ArrayValue):
                if len(arr.value) <= len(self.opstack):
                    arr.value.reverse()
                    for i in range(len(arr.value)):
                        arr.value[i] = self.opPop()
                    arr.value.reverse()
                    self.opPush(arr)
                else:
                    print("Error: astore - more elements in array than opstack")
                    self.opPush(arr)
            else: 
                print("Error: astore - operand is not an ArrayValue")
                self.opPush(arr)
        else:
            print("Error: astore expects an operand")

    #------- Stack Manipulation and Print Operators --------------

    """
       This function implements the Postscript "pop operator". Calls self.opPop() to pop the top value from the opstack and discards the value. 
    """
    def pop (self):
        self.opPop()

    """
       Prints the opstack. The end of the list is the top of the stack. 
    """
    def stack(self):
        for item in self.opstack:
            print(item)

    """
       Copies the top element in opstack.
    """
    def dup(self):
        if len(self.opstack) > 0:
            top = self.opPop()
            self.opPush(top)
            self.opPush(top)
        else:
            print("Error: dup expects an operand")

    """
       Pops an integer count from opstack, copies count number of values in the opstack. 
    """
    def copy(self):
        if len(self.opstack) > 0:
            count = self.opPop() # pop count off top of opstack
            if len(self.opstack) > (count-1):
                temp = []
                for i in range(count): # remove specified amount of values from stack to array
                    temp.append(self.opPop())
                temp.reverse()
                for i in range(2): # push items in array to opstack twice
                    for item in temp:
                        self.opPush(item)
            else:
                print("Error: copy - opstack has less elements than specified")
        else:
            print("Error: copy expects an operand")

    """
        Counts the number of elements in the opstack and pushes the count onto the top of the opstack.
    """
    def count(self):
        self.opPush(len(self.opstack))

    """
       Clears the opstack.
    """
    def clear(self):
        self.opstack.clear()
        
    """
       swaps the top two elements in opstack
    """
    def exch(self):
        if len(self.opstack) > 1:
            op1 = self.opPop() # top value
            op2 = self.opPop() # bottom value
            self.opPush(op1) # push first 
            self.opPush(op2) # push second, completing exchange
        else:
            print("Error: exch expects 2 operands")

    """
        Implements roll operator.
        Pops two integer values (m, n) from opstack; 
        Rolls the top m values in opstack n times (if n is positive roll clockwise, otherwise roll counter-clockwise)
    """
    def roll(self):
        if len(self.opstack) > 1:
            op1 = self.opPop() # top value (num of rotations)
            op2 = self.opPop() # bottom value (num of elements rolled)
            if len(self.opstack) > (op2 - 1): # make sure opstack has enough elements
                temp = []
                for i in range(op2):
                    temp.append(self.opPop())
                if op1 > 0:
                    temp.reverse()
                for i in range(abs(op1)):
                    t = temp.pop()
                    temp.reverse()
                    temp.append(t)
                    temp.reverse()
                if op1 > 0:
                    temp.reverse()
                temp.reverse()
                for item in temp:
                    self.opPush(item)
            else:
                print("Error: roll - opstack has less elements than specified")
        else:
            print("Error: roll expects 2 operands")

    """
       Pops an integer from the opstack (size argument) and pushes an  empty dictionary onto the opstack.
    """
    def psDict(self):
        if len(self.opstack) > 0:
            self.opPop()
            emptydict = {}
            self.opPush(emptydict)
        else:
            print("Error: psDict expects an operand")

    """
       Pops the dictionary at the top of the opstack; pushes it to the dictstack.
    """
    def begin(self):
        if len(self.opstack) > 0:
            self.dictPush(self.opPop())
        else:
            print("Error: begin expects an operand")

    """
       Removes the top dictionary from dictstack.
    """
    def end(self):
        if len(self.dictstack) > 0:
            self.dictPop()
        else:
            print("Error: end requires dictstack not to be empty")
        
    """
       Pops a name and a value from opstack, adds the name:value pair to the top dictionary by calling define.  
    """
    def psDef(self):
        if len(self.opstack) > 1:
            value = self.opPop()
            name = self.opPop()
            self.define(name, value)
        else:
            print("Error: psDef expects 2 operands")

    """
       Clean the top of the opstack (remove None value)
    """
    def cleanTop(self):
        if len(self.opstack)>1:
            if self.opstack[-1] is None:
                self.opstack.pop()



    # ------- if/ifelse Operators --------------
    """
       Implements if operator. 
       Pops the `ifbody` and the `condition` from opstack. 
       If the condition is True, evaluates the `ifbody`.  
    """
    def psIf(self):
        ifbody = self.opPop()
        condition = self.opPop()  
        if condition:
            if isinstance(ifbody, FunctionValue):
                ifbody.apply(self)
            else:
                ifbody.evaluate(self)

    """
       Implements ifelse operator. 
       Pops the `elsebody`, `ifbody`, and the condition from opstack. 
       If the condition is True, evaluate `ifbody`, otherwise evaluate `elsebody`. 
    """
    def psIfelse(self):
        elsebody = self.opPop()
        ifbody = self.opPop()
        condition = self.opPop()
        if condition:
            if isinstance(ifbody, FunctionValue):
                ifbody.apply(self)
            else:
                ifbody.evaluate(self)
        else:
            if isinstance(ifbody, FunctionValue):
                elsebody.apply(self)
            else:
                elsebody.evaluate(self)

    #------- Loop Operators --------------
    """
       Implements repeat operator.   
       Pops the `loop_body` (FunctionValue) and loop `count` (int) arguments from opstack; 
       Evaluates (applies) the `loopbody` `count` times. 
       Will be completed in part-2. 
    """  
    def repeat(self):
        loopbody = self.opPop() # FunctionValue
        loopcount = self.opPop() # int
        for i in range(loopcount):
            loopbody.apply(self)
        
    """
       Implements forall operator.   
       Pops a `codearray` (FunctionValue) and an `array` (ArrayValue) from opstack; 
       Evaluates (applies) the `codearray` on every value in the `array`.  
       Will be completed in part-2. 
    """ 
    def forall(self):
        codearray = self.opPop() # FunctionValue
        arr = self.opPop() # ArrayValue
        newarr = []
        for item in arr.value:
            self.opPush(item) # push value to stack
            codearray.apply(self) # apply FunctionValue to the value on the stack

    """
       Implements for operator. 
       Pops a CodeArrayValue object, the end index (end), the increment (inc), and the begin index (begin) and
       executes the code array for all loop index values ranging from `begin` to `end`.
       Pushes the current loop index value to opstack before each execution of the CodeArrayValue. 
       Will be completed in part-2. 
    """
    def psFor(self):
        obj = self.opPop() # CodeArrayValue object
        end = self.opPop() # end index 
        inc = self.opPop() # increment
        begin = self.opPop() # begin index
        for i in range(begin, end+inc, inc): # implement for loop
            self.opPush(i) # push current loop index to opstack
            obj.apply(self) # execute CodeArrayValue

    #--- used in the setup of unittests 
    def clearBoth(self):
        self.opstack[:] = []
        self.dictstack[:] = []
