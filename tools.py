from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# Note: Please make sure to set the following environment variables in your .env file
os.environ['SERPER_API_KEY'] = os.getenv('serper_api_key')

# Initialize the SerperDevTool for internet searching capabilities
tool= SerperDevTool()