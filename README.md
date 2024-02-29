# Twilio Usage Pricing Fetcher

This tool is designed to query the Twilio API for specific details about sent messages, notably the `SID`, `From`, and `Price` attributes of each message. It reads a list of message SIDs from a plain text file, fetches each message's details from Twilio, and then outputs the information into a CSV file named `UsagePricing.csv`.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python 3.x
- pip (Python Package Installer)

Additionally, you will need:

- Twilio Account SID
- Twilio Auth Token

### Installing

First, clone the repository to your local machine using git:

```bash
git clone https://github.com/aricday/twilio-billing-script.git
cd twilio-billing-script
```

Then, install the required Python packages:

```bash
pip install twilio pandas
```

### Configuration

Replace the placeholder values in the script `YOUR_ACCOUNT_SID` and `YOUR_AUTH_TOKEN` with your actual Twilio Account SID and Auth Token. These can be found in your Twilio console.

### Usage

1. Add your Message SIDs to a file named `MessageSIDs.txt`, ensuring each SID is on a new line.
2. Run the script with the command:

```bash
python twilio_script.py
```

3. Upon completion, a new file named `UsagePricing.csv` will be generated in your working directory with the details of each message.

## Contributing

If you would like to contribute to the development of this tool, please feel free to fork the repository, make your changes, and then submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Hat tip to the Twilio API for making communication data readily accessible.
* Thanks to all contributors who have helped to improve this tool.
```

Remember to replace `https://github.com/yourgithubusername/twilio-usage-pricing-fetcher.git` with the actual URL of your GitHub repository. Also, if you use a license different from MIT, make sure to update the License section accordingly, including the `LICENSE.md` file in your repository if it's not already included.

This README provides a basic structure including sections like 'Getting Started', 'Prerequisites', 'Installing', 'Usage', 'Contributing', and 'License'. Tailoring it to the specifics of your project will help others understand how to properly setup, use, and contribute to your project.