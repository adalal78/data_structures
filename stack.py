class my_stack():
    
    def __init__(self):
        
        self.items = []
    
    def show(self):
        
        print (self.items)
        
    def push(self,item):
        
        self.items.insert(0, item)
        
    def pop(self):
        if (self.items == []):
            return self.items
        
        else:
            return self.items.pop(0)
        
    def peek(self):
        if (self.items == []):
            return
        else:
            return self.items[0]
        
    def isEmpty(self):
        return(self.items == [])

    def size(self):
        return len(self.items)
           
def dec_to_binary(decimal):
    
    remstack = my_stack()
    
    quot = decimal // 2
    rem = decimal % 2
    
    remstack.push(rem)
    
    while(quot > 0):
        rem = quot % 2
        quot = quot // 2
        remstack.push(rem)
        
    binstring = ""
    while (not remstack.isEmpty()):
        binstring += str(remstack.pop())
        
    return binstring

def base_converter(decimal, base):
    
    digits = "0123456789ABCDEF"
    
    remstack = my_stack()
    
    quot = decimal // base
    rem = decimal % base
    
    remstack.push(rem)
    
    while(quot > 0):
        rem = quot % 2
        quot = quot // 2
        remstack.push(rem)
        
    base_string = ""
    while (not remstack.isEmpty()):
        base_string += str(digits[remstack.pop()])
        
    return base_string

def in_to_post(expr):
    
    opstack = my_stack()
    post = []
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    prec[")"] = 1
    
    operands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    operators = "*/+-"
    
    for c in expr:
        if (c in operands):
            post.insert(len(post), c)
        
        if (c == "("):
            opstack.push(c)
            
        if (c == ")"):
            
            popped = opstack.pop()
            while (popped != "("):
                if (popped in operators):
                    post.insert(len(post),popped)
                    
                popped = opstack.pop()
            
        if (c in operators):
            if (not opstack.isEmpty()):
                print (prec[opstack.peek()], prec[c])
                
            while ((not opstack.isEmpty()) and (prec[opstack.peek()] > prec[c])):
                post.insert(len(post), opstack.pop())
                
            opstack.push(c)
    
    while(not opstack.isEmpty()):
        post.insert(len(post), opstack.pop())
        
    print post
    post_stack = my_stack()
    for i in range(len(post)-1, -1, -1):
        post_stack.push(post[i])
    
    return post_stack

def post_process(post):
    
    operations = "*/+-"
    numberstack = my_stack()
    answer = 0
    
    while (not post.isEmpty()):
        pop = post.pop()
        #print pop
        
        if (pop in operations):
            numb = numberstack.pop()
            #print numb
            numb1 = int(numb)
            numb = numberstack.pop()
            #print numb
            numb2 = int(numb)
            
            if (pop == "*"):
                answer = (numb2 * numb1)
                numberstack.push(answer)
                
            if (pop == "/"):
                answer = (numb2 // numb1)
                numberstack.push(answer)
            
            if (pop == "+"):
                answer = (numb2 + numb1)
                numberstack.push(answer)
                
            if (pop == "-"):
                answer = (numb2 - numb1)
                numberstack.push(answer)
            
        else:
            numberstack.push(pop)
            
    return numberstack.peek()
    
    def parbalchk(expr):
    
    par_stack = my_stack()
    balanced = True
    
    for c in expr:
        if (c == "("):
            par_stack.push(c)
            
        elif (c == ")"):
            if (par_stack.isEmpty()):
                balanced = False
                break
            else:
                par_stack.pop()
                
    if ( par_stack.isEmpty() and balanced):
        print ("Balanced")
        
    elif (not par_stack.isEmpty() and balanced):
        print ("Unbalanced")
            
def balchk(expr):
    
    par_stack = my_stack()
    balanced = True
    
    left_symbol = "({["
    right_symbol = ")}]"
    
    for c in expr:
        if (c in left_symbol):
            par_stack.push(c)
            
        elif (c in right_symbol):
            if (par_stack.isEmpty()):
                print ("Unbalanced")
                balanced = False
                break
            elif ((c == "]" and par_stack.peek() == "[") or (c == "}" and par_stack.peek() == "{") or (c == ")" and par_stack.peek() == "(")):
                par_stack.pop()
            else:
                print("Unbalanced")
                balanced = False
                break
                
    if ( par_stack.isEmpty() and balanced):
        print ("Balanced")
        
    elif (not par_stack.isEmpty() and balanced):
        print ("Unbalanced")
 
def balchk(expr):
    
    myStack = my_stack()
    balanced = True
    
    leftExpr = "([{"
    rightExpr = ")]}"
    
    for c in expr:
        if c in leftExpr:
            myStack.push(c)
            
        elif c in rightExpr:
            if (myStack.isEmpty()):
                balanced = False
                break
                
            elif ( (c == ")" and myStack.peek() == "(") or (c == "]" and myStack.peek() == "[") or (c == "}" and myStack.peek() == "{") ):
                myStack.pop()
                
            else:
                balanced = False
                break
                
    if (not myStack.isEmpty()):
        print("Unbalanced")
        return False
    else:
        print ("Balanced")
        return True
