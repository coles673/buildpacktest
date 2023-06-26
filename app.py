from flask import Flask, render_template
from photos import images
import os
import random

app = Flask(__name__)


yep = os.listdir("photos")

ple = random.choice(yep)


@app.route("/")
def Greeting():
    test = images()
    html = """\
<html>
  <head></head>
  <body>
    <p>Thank you for being a loyal customer.<br>
       Here is your unique code to unlock exclusive content:<br>
       <br><br><h1>{code}</h1><br>
       <img src="{code}">
    </p>
  </body>
</html>
""".format(
        code=ple
    )

    return html


app.run(port=8910)
