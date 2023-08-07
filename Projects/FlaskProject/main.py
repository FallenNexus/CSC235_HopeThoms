#Flask website

from flask import Flask

#Create a web server object that handles requests to the web server
#Creates an instance of the flask library class
#__name__ is a special variable that gets the name of the file that is running
web_app = Flask(__name__)

#This is the pattern for routes and pages

#Creating the home page
#Creating the route to the page and then a function that handles requests and respinds with a webpage

@web_app.route('/')

def home_page():
    #Whatever is returned in this function will appear in the browser
    #This will return a string that will be HTML code for the webpage
    #Using multi-line string to make it easier to write the HTML
    #Use triple quotes
    return '''
    <br><br><br><h1>Welcome to the blog of Hope T<h1><br><br><br>
    <a href="/blog">Blog Posts</a>
    <a href="/camp">Python Camp</a>
    '''

#Where the blog posts will be coded
list_of_blog_posts = [
    {"Title": "How To Make Your First Game With Little Coding Experience", "Author": "Hope T., Morgan S.", "Date": "04-07-2023", "Content": "View our video here: https://youtu.be/5ilA4Eg1j-E"},
    {"Title": "Featured Indie", "Author": "Hope T.", "Date": "07-21-2022", "Content": "Have you ever wanted to babysit the anti-christ? Well now you can in the 'Baby in Yellow', watch my playthrough here: https://youtu.be/-UFNqttyD9s"},
]

#Page that displays a list of all blog entries
@web_app.route('/blog')

#Function to handle the requests and responses
def blog():
    #Starts with an empty string
    output = ''
    #Title
    output += f'<br><br><br><h1>Blog Posts<h1><br><br><br>'
    #Loop through all blog posts
    for post in list_of_blog_posts:
        output += f'<h2>{post["Title"]}<h2>'
        output += f'<h3>{post["Author"]}<h2>'
        output += f'<h4>{post["Date"]}<h2>'
        output += f'<h5>{post["Content"]}<h2>'
    #Return the output string
    return output

#Page that displays camp advert
@web_app.route('/camp')

#Function to handle the requests and responses
#I used chatGPT to create the advertisment since that is far from my specialty
#Here is the link to the convo: https://chat.openai.com/share/b57415e4-7bd0-4f9a-b69b-dfde2191250d
def camp():
    return'''
    <br><br><br><h1>Join Camp Python!<h1><br><br><br>
    <br>
    <h2>Calling all aspiring coding enthusiasts! Unlock the power of Python and embark on a transformative journey at our exhilarating Python Coding Camp. If you've ever dreamt of creating cutting-edge applications, solving complex problems, or delving into the world of data science, this camp is your gateway to success! Join us for an unforgettable learning experience, where innovation meets fun, and ignite your passion for coding like never before.<h2>
    <br>
    <br>
    <h2> In our Python Coding Camp, you will acquire an impressive array of skills that will set you apart in the digital realm. Here are ten essential skills you will master:<h2>
    <h3>Fundamentals of Python: Gain a solid foundation in Python programming, understanding its syntax and unique features.<h3>
    <h3>Web Development: Dive into web technologies with Flask and Django, and build captivating web applications.<h3>
    <h3>Data Analysis: Learn to process and analyze data using Python's powerful libraries like NumPy and Pandas.<h3>
    <h3>Game Development: Create engaging games using Python's Pygame library and bring your ideas to life.<h3>
    <h3>Machine Learning: Explore the fascinating world of Machine Learning with popular libraries like TensorFlow and Scikit-learn.<h3>
    <h3>API Integration: Learn how to interact with APIs, enabling seamless data exchange between applications.<h3>
    <h3>Automation and Scripting: Automate repetitive tasks and write efficient scripts to simplify your workflow.<h3>
    <h3>Database Management: Master SQL and work with databases like SQLite to store and retrieve information.<h3>
    <h3>Version Control: Collaborate effectively with Git, tracking changes and managing your code efficiently.<h3>
    <h3>Real-world Projects: Apply your newfound skills to create impressive projects and showcase your expertise.<h3>
    <br>
    <br>
    <h2>To make this enriching experience accessible to all, we have thoughtfully designed the camp to be affordable and rewarding. For the valuable knowledge, personalized attention, and hands-on practice you'll receive, the camp fee is just $200. With this investment, you will receive:<h2>
    <h3>Expert-led Sessions: Our seasoned instructors will guide you through every step of the learning process, providing valuable insights and resolving doubts.<h3>
    <h3> Interactive Learning: Engage in practical exercises, group discussions, and collaborative projects to enhance your problem-solving abilities<h3>
    <h3>Certificate of Completion: Receive a prestigious certificate upon successful completion of the camp, validating your newfound Python prowess.<h3>
    <br>
    <br>
    <h2>Sign up today!<h2>
    '''
    
#This is the starting point for the website
if __name__ == '__main__':
    #Run the web app
    web_app.run()
