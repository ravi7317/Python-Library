# NYC Weather Analysis

This project analyzes weather data from NYC. The dataset includes information on temperature, wind speed, and events like rain.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed Python 3.x
* You have installed the following Python libraries:
  - pandas

## Installation

To install the required libraries, you can use pip:

```bash
pip install pandas
Usage
Download the dataset and place it in your working directory. The dataset file should be named nyc_weather.csv.

Use the following script to analyze the weather data:

python
Copy code
import pandas as pd

# Load the dataset
df = pd.read_csv(r"D:\kausik\BHP\Python\PANDADAY1\nyc_weather.csv")

# Display the first few rows of the dataframe
print(df.head())

# Find the maximum temperature
max_temperature = df['Temperature'].max()
print("Maximum Temperature:", max_temperature)

# Find the dates when it rained
rainy_days = df['EST'][df['Events'] == 'Rain']
print("Rainy Days:")
print(rainy_days)

# Fill missing values with 0
df.fillna(0, inplace=True)

# Calculate the average wind speed
average_wind_speed = df['WindSpeedMPH'].mean()
print("Average Wind Speed:", average_wind_speed)

# Display the first few rows of the dataframe again to see changes
print(df.head())
Run the script:
bash
Copy code
python your_script_name.py
Replace your_script_name.py with the name of your Python script file.

Explanation of the Script
Loading the Dataset: The dataset is loaded using pd.read_csv.
Displaying Data: The first few rows of the dataset are displayed using df.head().
Maximum Temperature: The maximum temperature in the dataset is found using df['Temperature'].max().
Rainy Days: The dates when it rained are extracted using df['EST'][df['Events'] == 'Rain'].
Handling Missing Data: Missing values in the dataset are filled with 0 using df.fillna(0, inplace=True).
Average Wind Speed: The average wind speed is calculated using df['WindSpeedMPH'].mean().
Displaying Changes: The first few rows of the dataset are displayed again to show the changes made.
Contributing
If you want to contribute to this project, follow these steps:

Fork this repository.
Create a branch: git checkout -b <branch_name>.
Make your changes and commit them: git commit -m '<commit_message>'.
Push to the original branch: git push origin <project_name>/<location>.
Create the pull request.
Alternatively, see the GitHub documentation on creating a pull request.

License
This project is open source and available under the MIT License.

markdown
Copy code

### Notes:

1. Save this content in a file named `README.md` in your project directory.
2. Ensure the paths and descriptions match your actual project setup.
3. If your project has additional dependencies or setup steps, include them in the `Prerequis