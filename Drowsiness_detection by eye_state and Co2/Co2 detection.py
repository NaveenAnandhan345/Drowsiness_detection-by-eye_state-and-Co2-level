import csv
import re
import pygame
import time
# Initialize pygame
pygame.init()

# Specify the path to your music file (replace 'music.mp3' with your file)
music_file = 'co2_level_command.mp3'

csv_file_path = 'co2_dataset.csv'
column_name = 'data'
threshold = 1100  # Define the threshold value
delay_seconds = 0.005
try:
    with open(csv_file_path, mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csv_reader:
            time.sleep(delay_seconds)
            try:
                # Extract numeric portions using regular expressions
                cell_value = row[column_name]
                numeric_portions = re.findall(r'\d+\.\d+|\d+', cell_value)

                # Check if any numeric portion is greater than or equal to the threshold
                for numeric_portion in numeric_portions:
                    numeric_value = int(numeric_portion)
                    print(numeric_value)
                    if numeric_value >= threshold:
                        print(f"Co2 level is {threshold}.")

                        # Initialize the mixer module to handle audio playback
                        pygame.mixer.init()
                        try:
                            # Load the music file
                            pygame.mixer.music.load(music_file)

                            # Play the music
                            pygame.mixer.music.play()

                            # Wait for the music to finish (or you can add a specific duration)
                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)
                        finally:
                            # Quit pygame (optional)
                            pygame.quit()
                        # Break the loop after finding the first value that meets the condition
                        raise StopIteration
            except (ValueError, KeyError):
                # If conversion fails or the column doesn't exist, ignore the cell
                pass
except FileNotFoundError:
    print(f"The file '{csv_file_path}' was not found.")
except StopIteration:
    pass  # StopIteration is raised to break the loop
except Exception as e:
    print(f"An error occurred: {str(e)}")