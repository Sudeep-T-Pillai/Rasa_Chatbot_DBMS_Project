# Rasa Chatbot for DBMS Project

This project is a Rasa-based chatbot designed for a Database Management System (DBMS) application. The chatbot uses machine learning models to understand user queries and interact with a database backend to provide relevant responses.

## Features
- Natural language understanding and intent classification using Rasa.
- Integration with external APIs for enhanced chatbot responses.
- Database interactions managed through a backend API (PocketBase).

## Project Structure
- **actions/**: Contains custom action files.
- **data/**: Holds training data for Rasa intents and responses.
- **models/**: Stores trained Rasa models.
- **domain.yml**: Defines the chatbot's intents, responses, and entities.
- **config.yml**: Configuration for Rasa pipelines and policies.
- **credentials.yml**: Contains API credentials for external integrations.
- **endpoints.yml**: Specifies server endpoints for actions and webhook integrations.

## Requirements
To set up and run the Rasa chatbot locally, you need:
- Python 3.7+
- Rasa 2.x or higher
- PocketBase (for database backend integration)
- API keys for eBay (for product searches and responses)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Sudeep-T-Pillai/Rasa_Chatbot_DBMS_Project.git
cd Rasa_Chatbot_DBMS_Project
rasa train
rasa run actions
rasa shell

Note About API Keys
This project previously used API keys for eBay and PocketBase. Please note that these keys are now expired, and attempting to use them in this project will result in failures or limited functionality. You can:

Obtain a new API key from eBay’s Developer Program.
Set up a new instance of PocketBase with updated credentials.Or intstall pocketbase or other Baas locally.
Replace the expired keys in actions.py with your own if you wish to test the functionality.

Usage
Once the Rasa server is running, you can interact with the chatbot via the command line, or integrate it with a frontend.

#License
This project is licensed under the MIT License.
