from flask import Flask
import json
import mimerender
import urllib
import recommendation
mimerender = mimerender.FlaskMimeRender()

render_xml = lambda message: '<message>%s</message>'%message
render_json = lambda **args: json.dumps(args)
render_html = lambda message: '<html><body>%s</body></html>'%message
render_txt = lambda message: message

app = Flask(__name__)

@app.route('/')
@app.route('/<tweet>')
@mimerender(
    default = 'html',
    html = render_html,
    xml  = render_xml,
    json = render_json,
    txt  = render_txt
    )
def greet(tweet='world'):
    # Given a tweet, we need to find out the recommended mentions here
    # for not returning a dummy recommendation
    tweet = urllib.unquote(tweet)
    tweet = tweet.replace("+"," ")
    return {
            'message': {
                'tweet':tweet,
                'recommendations':recommendation.get(tweet)
                }
            }

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
