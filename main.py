from flask import Flask, request, jsonify
import eng_to_ipa as ipa
import os


app = Flask(__name__)

@app.route('/transcribe', methods=['GET'])
def transcribe():
    text = request.args.get('text', '')  # Get text from query parameter
    if text:
        transcription = ipa.convert(text)
        return jsonify({'transcription': transcription}), 200
    else:
        return jsonify({'error': 'No text provided'}), 400


# Other code...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)

