# CTF Platform

Welcome to the CTF Platform repository! This is a web application designed for hosting Capture The Flag (CTF) events, where participants can solve cybersecurity challenges and compete against each other.

## Technologies Used
- **Backend Framework**: FastAPI
- **Frontend Framework**: Bootstrap
- **Database**: MySQL (for production)
- **Authentication**: JWT (JSON Web Tokens)
- **Development Tools**: Python, JavaScript, HTML, CSS

## Current Features
- **User Authentication**: Participants can securely log in to track their progress and submit flags.
- **Challenge Management**: Organizers can create, manage, and delete challenges manually.
- **Leaderboard**: View a leaderboard showing the scores and rankings of participants.
- **Flag Submission**: Participants can submit flags for challenges to earn points.
- **Event Hosting**: Host a single event with a set of predefined challenges.

## Getting Started
To get started with the CTF Platform, follow these steps:
1. Clone the repository: `git clone https://github.com/santhosh-vairamuthu/CTF-Platform.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables: Update the `.env` file with your settings.
4. Run the application: `uvicorn main:app --reload`

## Contributing
Contributions are welcome! If you'd like to contribute to the CTF Platform, please follow these guidelines:
- Fork the repository and create a new branch for your feature or bug fix.
- Make your changes and test them thoroughly.
- Create a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License - see the [MIT License](LICENSE) file for details.
