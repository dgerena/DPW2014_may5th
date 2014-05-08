class HTMLPage(object):
    def __init__(self):#contructor
        self.page_open='''
<!Doctype html>
<html>
    <head>
        <title>Welcome to my page!</title>
        <link href="css/style.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        '''
        self.page_content='''
        <form method="get">
            <label for="firstName">First Name</label>
            <input name="firstName" type="text" placeholder="Your Name">
            <label for="name">Last Name</label>
            <input name="lastName" type="text" placeholder="Your Name">
            <button type="submit">Submit</button>
        </form>
        '''
        self.page_close='''
    </body>
</html>
'''
    def print_out(self,content=""):
        #if the content... is an empty string.. print the form
        #else dont
        return self.page_open+self.page_content+content+self.page_close