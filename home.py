from flask import Flask, render_template, request
from contact_model import Contact

Contact.load_db()

print(Contact.db.values())

app = Flask(__name__)

@app.route('/contacts')
def contacts():
    query = request.args.get('q')
    if query is not None:
        result_contacts = Contact.search(query)
    else:
        result_contacts = Contact.all()
    return render_template("index.html", contacts=result_contacts)

if __name__ == '__main__':
    app.run(debug=True)