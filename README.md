## 🔗 Links
Follow on 
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/debendra-bakhati/)

# PDF Chatbot

This is a FastAPI application that serves as an intelligent assistant for handling banking-related queries. The application utilizes Google Generative AI for generating conversational responses and a Chroma vector store for retrieving relevant information from a dataset.


### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Debendra62/Bank_Assistant.git
```

### Set Up the Virtual Environment

Create and activate a virtual environment:

```bash
conda create -p venv python==3.11
conda activate /Bank_Assistant/venv   
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a .env file in the root directory of the project and add your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key
HOST=your_host
PORT=your_port
```

## Get the API key
  https://aistudio.google.com/app/u/1/apikey

### Run the Application

To run the application, use the following command:

```bash
python main.py
```
