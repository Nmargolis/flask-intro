from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """
    <!doctype html>
        <html>
            <head>
                <title>Home Page</title>
            </head>

            <body>
            <h1>Hi this is home page</h1>
            <a href="/hello">Click here to say hello</a>
            </body>
        </html>
        """


# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet" method="POST">
                <label>What's your name? <input type="text" name="person"></label>
                <br>
                <label>Choose a compliment:
                    <input type="radio" name="compliment" value="{0}">{0} 
                    <input type="radio" name="compliment" value="{1}">{1}  
                    <input type="radio" name="compliment" value="{2}">{2}
                    <input type="radio" name="compliment" value="{3}">{3}
                    <input type="radio" name="compliment" value="{4}">{4}
                    <input type="radio" name="compliment" value="{5}">{5}
                    <input type="radio" name="compliment" value="{6}">{6}
                    <input type="radio" name="compliment" value="{7}">{7}
                    <input type="radio" name="compliment" value="{8}">{8}
                    <input type="radio" name="compliment" value="{9}">{9}
                    <input type="radio" name="compliment" value="{10}">{10}
                    <input type="radio" name="compliment" value="{11}">{11}
                    <input type="radio" name="compliment" value="{12}">{12}
                    <input type="radio" name="compliment" value="{13}">{13}


                </label>
                <input type="submit">
            </form>
            <br> <br>
            <form action="/diss">
                <label>What's your name? <input type="text" name="person"></label>
                <br>
                <label>Choose a diss:
                    <input type="radio" name="diss" value="{14}">{14} 
                    <input type="radio" name="diss" value="{15}">{15}  

                </label>
                <input type="submit">
            </form>


        </body>
    </html>

    """.format('awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely', 'stinky', 'yucky')

@app.route('/greet', methods=["POST"])
def greet_person():
    player = request.form.get("person")
    compliment = request.form.get("compliment")

    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    # compliment = choice(AWESOMENESS)

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s!
        </body>
    </html>""" % (player, compliment)

@app.route('/diss')
def diss_person():
    player = request.args.get("person")
    diss = request.args.get("diss")
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>diss</title>
        </head>
        <body>
            Hi %s I think you're %s!
        </body>
    </html>""" % (player, diss)



        

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
