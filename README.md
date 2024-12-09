# Gaming Network Connection Tester

A real-time network connectivity tester specifically designed for gamers to check their connection to various gaming services, platforms, and communities.

![image](https://github.com/user-attachments/assets/a3b74f2b-04e3-459f-9122-6f2a179fce2e)


## Features

- **Real-time Connection Testing**

  - Tests connectivity to major gaming platforms
  - Measures response times
  - Monitors connection quality
  - Displays detailed network statistics

- **Supported Services**

  - Game Launchers (Steam, Epic, Battle.net, etc.)
  - Popular Games (World of Warcraft, League of Legends, etc.)
  - Game Development Platforms
  - Gaming Communities
  - Voice Chat Services

- **Network Information**
  - Connection Type Detection
  - Latency Status
  - Network Quality Metrics
  - IP Location

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/gaming-network-tester.git
cd gaming-network-tester
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:

```bash
python app.py
```

2. Open your browser and navigate to:

```
http://localhost:5000
```

3. The application will automatically:
   - Detect your network configuration
   - Test connections to gaming services
   - Display real-time results
   - Auto-refresh every 60 seconds (optional)

## Technical Details

### Backend

- Flask web framework
- Multi-threaded connection testing
- Socket-based connectivity checks
- Real-time network diagnostics

### Frontend

- Modern responsive design
- Bootstrap 5 UI framework
- Font Awesome icons
- Real-time updates via JavaScript

### Network Tests

- TCP connection testing
- Response time measurement
- DNS resolution checking
- Service availability monitoring

## Requirements

- Python 3.7+
- Flask
- Modern web browser with JavaScript enabled
- Network connection

## Configuration

The application tests connections to predefined gaming services. You can modify the `gaming_services` dictionary in `app.py` to add or remove services:

```python
gaming_services = {
    "Game Launchers": {
        "Steam": ("store.steampowered.com", 443),
        # Add more services...
    }
}
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask framework
- Bootstrap team
- Font Awesome
- Gaming service providers for their platform documentation

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.
