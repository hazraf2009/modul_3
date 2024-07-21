from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

facts_list = ["Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten.", 
            "Menurut sebuah penelitian yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka ketergantungan pada ponsel pintar mereka.", 
            "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini.", 
            "Studi tentang kecanduan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan."]

@app.route("/random_fact")
def facts():
    fact = random.choice(facts_list)
    return render_template('random_fact.html', fact=fact)


pass_list = "1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*"

@app.route("/random_pass")
def passs():
    password = ""
    for i in range(20):
        password += random.choice(pass_list)
    return render_template('random_pass.html', password=password)

app.run(debug=True)

