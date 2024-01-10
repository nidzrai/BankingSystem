# Banking System Application

## Overview
This Banking System application is a simplified model designed to demonstrate the implementation of clean architecture in a software project. The application is divided into three primary layers: Domain, Use Case, and Infrastructure. Each layer has its distinct responsibilities and operates independently of the others.

## Structure
The application is structured as follows:

- `domain/`: Contains the core business logic and entities (`Account` and `Customer`).
- `usecases/`: Contains the application-specific business rules (`CreateAccount`, `MakeTransaction`, and `GenerateAccountStatement`).
- `infrastructure/`: Manages external concerns and interactions (`AccountRepository`).
- `tests/`: Includes unit tests for each component of the application.

## Setup
To set up the application, follow these steps:

1. Clone the repository:  git clone https://github.com/nidzrai/cleanCode.git
2. Navigate to the project directory:
cd codeVyasaBankingSysClean
3. Install dependencies (if any):
pip install -r requirements.txt
## Running the Application
To run the application, execute the main script:
python main.py
### Refer main.py to get better understanding
This script demonstrates:
1. The creation of a new account.
2. Making a deposit into the account.
3. Generating an account statement.

## Testing
The application comes with a comprehensive suite of tests. To run the tests, navigate to the project root and execute:
python -m unittest
Each test file corresponds to a component of the application and is structured to cover a range of scenarios, including edge cases.
    
## Contributing
Contributions to the project are welcome. Please follow the standard fork, branch, and pull request workflow.

## License
MIT

## Contact
For any inquiries or contributions, please contact nidhi.rai94@gmail.com .

