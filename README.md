
# Screen-Summarizer

Screen-Summarizer is a tool designed to simplify the process of creating meeting minutes from video recordings, such as online meetings or webinars. It utilizes AI tools to automatically generate concise and clear meeting notes, making the note-taker's job easier and more efficient.

## Features

- Converts video recordings into well-structured meeting minutes.
- Supports various video formats, including `.mkv` and `.mp4`.
- Integrates with AI models for natural language processing and summarization.
- Configurable through a YAML file for easy setup and deployment.

## Getting Started

Follow these steps to set up and run the Screen-Summarizer on your local machine.

### Prerequisites

- Python 3.x
- OpenAI API Key
- AWS Credentials (if required for video storage/processing)

### Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/bayupermadi/screen-summarizer.git
    cd screen-summarizer
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **Set up the configuration file:**

   - Rename the `config.yaml-template` file to `config.yaml`:
     ```bash
     mv config.yaml-template config.yaml
     ```
   - Open `config.yaml` and set your credentials for AWS and OpenAI. Ensure that all required fields are correctly filled in based on your environment.

### Usage

To run the code and generate meeting minutes, use the following command:

```bash
python3 main.py --config "your config file" --source "your video file"
```

- Replace `"your config file"` with the path to your `config.yaml` file.
- Replace `"your video file"` with the path to the video file you want to process.

### Additional Notes

- The tool is designed to be extensible, so feel free to customize and improve it to fit your specific needs.
- If you find this project helpful, please consider giving it a star to show your appreciation!

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenAI for providing the API used for summarization.
- The open-source community for the libraries and tools that made this project possible.
