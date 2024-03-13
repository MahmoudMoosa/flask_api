from flask import Flask, request, jsonify
import eng_to_ipa as ipa

app = Flask(__name__)

@app.route('/transcribe', methods=['GET'])
def transcribe():
    text = request.args.get('text', '')  # Get text from query parameter
    if text:
        transcription = ipa.convert(text)
        return jsonify({'transcription': transcription}), 200
    else:
        return jsonify({'error': 'No text provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
