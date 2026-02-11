# Media File Faker

import os

# Define directories for Movies and TV Shows
MOVIE_DIR = os.path.expanduser("~/movies")
TV_DIR = os.path.expanduser("~/tv_shows")

# Lists of dummy movies and TV shows with underscores instead of spaces
MOVIES = [
    'The_Dark_Knight.md',
    'Inception.md',
    'Pulp_Fiction.md',
    'The_Shawshank_Redemption.md',
    'The_Green_Mile.md',
    'Fight_Club.md',
    'Forrest_Gump.md',
    'The_Matrix.md',
    'Gladiator.md',
    'Titanic.md',
    'Avatar.md',
]

TV_SHOWS = [
    'Breaking_Bad.md',
    'Friends.md',
    'The_Wire.md',
    'Game_of_Thrones.md',
    'The_Sopranos.md',
    'Stranger_Things.md',
    'The_Office.md',
    'Mad_Men.md',
    'Westworld.md',
    'Fargo.md'
]

def create_directory_if_not_exists(directory):
    """Create a directory if it does not already exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
    else:
        print(f"Directory '{directory}' already exists.")

def create_dummy_files(directory, file_list):
    """Create empty Markdown files in the specified directory."""
    for file_name in file_list:
        file_path = os.path.join(directory, file_name)
        try:
            with open(file_path, 'w') as f:
                pass # Create an empty file
            print(f"Created file: {file_path}.")
        except Exception as e:
            print(f"Failed to create file {file_path}: {e}.")

def main():
    """Main function to create directories and dummy files"""
    # Create directories if they don't exist
    create_directory_if_not_exists(MOVIE_DIR)
    create_directory_if_not_exists(TV_DIR)

    # Create dummy movie and TV show files
    create_dummy_files(MOVIE_DIR, MOVIES)
    create_dummy_files(TV_DIR, TV_SHOWS)

    print("Dummy file creation completed.")

if __name__ == "__main__":
    main()
