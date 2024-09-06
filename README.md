# CloudBYP

**CloudBYP** is a tool designed to find the origin IP addresses of Cloudflare-protected websites using the Censys search API. It also retrieves the site title for each discovered IP address.

## Features

- Fetch exposed IP addresses for a specified domain.
- Retrieve and display the site title for each IP address.
- Output results in a human-readable format.
- Optionally save results to a file.

## Requirements

- Python 3.x
- Required Python packages:
  - `requests`
  - `beautifulsoup4`

You can install the necessary packages using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

### Basic Usage

To run the tool, use the following command:

```bash
python3 CloudBYP.py <domain> --api-id <your_censys_api_id> --api-secret <your_censys_api_secret>
```

Replace `<domain>`, `<your_censys_api_id>`, and `<your_censys_api_secret>` with your desired domain and your Censys API credentials.

### Options

- `--api-id`: Your Censys API ID. (Required)
- `--api-secret`: Your Censys API secret. (Required)
- `--output`: Path to the output file. If specified, results will be saved to this file. Otherwise, results will be printed to the console.

### Example

```bash
python3 CloudBYP.py example.com --api-id YOUR_API_ID --api-secret YOUR_API_SECRET --output results.txt
```

This command will search for exposed IP addresses for `example.com` and save the results, including site titles, to `results.txt`.

## License

This tool is provided under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

The use of this tool should comply with all applicable laws and terms of service of the APIs and websites being accessed.

For any issues or contributions, please open an issue or pull request on the GitHub repository.
