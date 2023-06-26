from flask import Flask, jsonify, request

app = Flask(__name__)
campus = [
    {
        'universitas': 'gunadarma',
        'jurusan': [
            {
                'fakultas': 'FTI',
                'jumlah_mahasiswa': 10000
            } 
        ]
    },
    {
        'universitas': 'binus',
        'jurusan': [
            {
                'fakultas': 'ilkom',
                'jumlah_mahasiswa': 900
            }    
        ]
    }
]

@app.route('/univ/<string:name>')
def get_univ(name):
    for univ in campus:
        if univ['universitas'] == name:
            return jsonify(univ['universitas'])
    return jsonify({'message': 'univ not found'})


@app.route('/univ/<string:name>/jurusan')
def get_univ_jurusan(name):
    for univ in campus:
        if univ['universitas'] == name:
            return jsonify(univ['jurusan'])
    return jsonify({'message': 'univ not found'})

@app.route('/univ', methods=["POST"])
def create_univ():
    req_data = request.get_json()
    new_univ = {
        'universitas': req_data.get('universitas'),
        'jurusan': []
    }
    campus.append(new_univ)
    return jsonify(new_univ)

@app.route('/univ/<string:name>/jurusan', methods=['POST'])
def create_univ_jurusan(name):
    for univ in campus:
        if univ['universitas'] == name:
            req_data = request.get_json()
            new_jurusan = {
                'fakultas': req_data['fakultas'],
                'jumlah_mahasiswa': req_data['jumlah_mahasiswa']
            }
            univ['jurusan'].append(new_jurusan)
            return jsonify(new_jurusan)
    return jsonify({'message': 'univ not found'})

@app.route('/')
def home():
    return "haii nama saya irfan tri atsal, dan saya dari kelas 1IA04"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
