# MLScraper
Web Scraper built with Selenium to extract site data and run through an SVM classifier to extract relevant text.

### How to Use :
Input the following commands in the terminal
`set FLASK_APP=flask_app.py`
`$env:FLASK_APP = "flask_app.py"`
`flask run`

### To add data for training :
Inject `js_click_content.js` in browser and manually select important text. 
Press right-alt to download CSV of the site text. Repeat for multiple sites.
Combine CSVs with csv_merger.py and add to existing `svm_training_data.csv`.
Retrain model and check stats for performance using `python .\model_trainer.py`.

### Others :
- Change values in `multiscript_config.py` to update broker URLs and SVM performance.
- Errors may arise later if scikit-learn package installed isn't same version as saved SVM model so retrain model as stated above
- Procfile `web: gunicorn --bind 0.0.0.0:$PORT flask_app:app` where flask_app is the file's name
