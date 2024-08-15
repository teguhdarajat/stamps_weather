# stamps_weather
This Python program retrieves and displays the weather forecast for Jakarta for the next five days using the OpenWeatherMap API.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/teguhdarajat/stamps_weather.git
   ```

2. **Navigate into the project directory:**

   ```bash
   cd stamps_weather
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the project root directory and add your OpenWeatherMap API details:

   ```
   BASE_URL=https://api.openweathermap.org
   API_KEY=your_openweathermap_api_key
   ```

## Usage

To run the program and display the weather forecast, execute the following command:

```bash
python main.py
```

This will show the temperature forecast for Jakarta for the next five days in Celsius.
