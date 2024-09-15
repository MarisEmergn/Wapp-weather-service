from flask import Flask, request, jsonify
from weather import get_weather_data

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def weather():
    location = request.args.get('location')

    # Basic validation to check if location is provided
    if not location:
        return jsonify({'error': 'Location is required'}), 400

    # Call the function to get weather data
    weather_data = get_weather_data(location)
    if weather_data:
        return jsonify(weather_data), 200
    else:
        return jsonify({'error': 'Could not retrieve weather data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
