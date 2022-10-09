import flask as f
from pandas import DataFrame
from pickle import load

# Create a web application and load contents of pickle file
app = f.Flask(__name__)
model = load(open("model.pkl", "rb"))


# Load template on opening app home page
@app.route("/")
def home():
    """
    Desc: This the home api whenever you will click in the link.
    It will redirect you to index.html
    :return: render_template
    """
    return f.render_template("index.html")


# Create predictions and show it on page
@app.route("/result", methods=["POST"])
def predict():
    """
    Desc: This api takes the data on the basis of form.
    After clicking the submit button it will redirect you to result.html
    Where you can see your prediction
    :return: render_template of result.html
    """
    A = [] # this contains the list of values which we will pass through the form.
    for i in f.request.form.values():
        A.append(int(i))
    predicted_profit = round(model.predict(DataFrame([[A[0], A[1]]]))[0][0], 2) # this will make prediction value
    return f.render_template("result.html", pred=predicted_profit)


if __name__ == "__main__":
    app.run(debug=True)

