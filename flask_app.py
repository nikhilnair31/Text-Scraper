import js2svm
import jsinfo
from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object("multiscript_config")

def result2output(result):
    return render_template("output.html",result = result)

def jsdata2svm(url, scaled_df, text_list, meta_titles, meta_info):
    return js2svm.main(url, scaled_df, text_list, meta_titles, meta_info)

@app.route('/')
def student():
    return render_template('input.html')

@app.route('/result',methods = ['POST'])
def result():
    result = request.form
    url = result['URL']
    scaled_df, text_list, meta_titles, meta_info = jsinfo.main(url)

    result = jsdata2svm(url, scaled_df, text_list, meta_titles, meta_info)
    return render_template("output.html", result = result)

if __name__ == '__main__':
    app.run()
    # app.jinja_env.auto_reload = True
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    # app.run(debug = True, host="0.0.0.0")