# Impor
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Hasil formulir
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # mendapatkan gambar yang dipili
        selected_image = request.form.get('image-selector')

        # Tugas #2. Menerima teks
        text_top = request.form.get("textTop")
        text_bottom = request.form.get("textBottom")

        # Tugas #3. Menerima posisi teks
        textTop_position = request.form.get("textTop_y")
        textBottom_position = request.form.get("textBottom_y")
        # Tugas #3. Menerima warna teks
        text_color = request.form.get("color-selector")
        

        return render_template('index.html', 
                               # Menampilkan gambar yang dipilih
                                selected_image=selected_image, 

                               # Tugas #2. Menampilkan teks
                                text_top=text_top,
                                text_bottom=text_bottom,

                               # Tugas #3. Menampilkan warna
                                text_color=text_color,
                               
                               # Tugas #3. Menampilkan posisi teks
                                textTop_position=textTop_position,
                                textBottom_position=textBottom_position
                               )
    else:
        # Menampilkan gambar pertama secara default
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
