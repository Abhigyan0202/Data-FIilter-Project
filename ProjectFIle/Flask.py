from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)
#Path needs to be updated as per the location of the excel file
dataframe = pd.read_excel('data2.xlsx')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    name = request.form['input1']
    fname = request.form['input2']
    mask = (dataframe.Name_English.str.contains(name, case=False)) & (dataframe.Fname_English.str.contains(fname, case=False))
    new_dataframe = dataframe[mask]
    table = new_dataframe.to_html(index=False)

    return render_template('table.html',table_html=table)


if __name__ == '__main__':
    app.run(debug=True)
