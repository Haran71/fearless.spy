from scrape import driver
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


@app.get('/')
def start_up():
    return render_template("index.html")

@app.post('/loader')
def loader():
    term = request.form["search_box"]
    return render_template("loader.html",term=term)

@app.get('/driver')
def main_driver():
    data = str(request.args.to_dict(flat=False)['data'][0])
    Driver = driver(data)

    # Scraping the data
    Driver.scrape()

    # Getting the data, converting it to a dtaframe, cleaning and performing sentimental analysis
    Driver.get_dataframe()
    Driver.clean_tweets()
    Driver.analysis()

    # Generating the wordcloud and saving the image on the disk
    word_cloud = Driver.generate_wordcloud()
    word_cloud = word_cloud.to_file("static/images/wordcloud.png")

    return "done"

    

if __name__ == "__main__":
    app.run(debug=True)
