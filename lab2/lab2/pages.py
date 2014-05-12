class HTMLPage(object):
    def __init__(self):#contructor
        self.page_open='''
<!Doctype html>
<html>
    <head>
        <title>Name comparison!</title>
        <link href="css/style.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        <header>
            <id>
                <h1>Logo</h1>
            </id>
            <ul>
                <li>Home</li>
                <li>Display</li>
            </ul>
        </header>
        '''
        self.form_content='''
        <form method="get">
            <label for="firstName">First Name</label>
            <input name="firstName" type="text" placeholder="Your Name">
            <label for="name">Last Name</label>
            <input name="lastName" type="text" placeholder="Your Name">
            <label for="favColor">Favorite Color</label>
            <select name="favColor">
                <option>Red</option>
                <option>Green</option>
                <option>Blue</option>
            </select>
            <button type="submit">Submit</button>
        </form>
        '''
        self.page_close='''
    </body>
</html>
'''
        self.display_content='''
        <h2>Hello firstName+lastName</h2>
        <p>favorColor</p>
        <p>Color meaning</p>
        <p>This color has </p>
        '''
    def print_out(self,content=""):
        #if the content... is an empty string.. print the form
        #else dont
        return self.page_open+self.form_content+content+self.page_close