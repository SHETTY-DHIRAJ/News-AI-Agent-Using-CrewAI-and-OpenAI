import os
from crewai import Agent, LLM
from dotenv import load_dotenv
from tools import tool
import datetime

# load environment variables
load_dotenv()

# Note: Please make sure to set the following environment variables in your .env file
api_key= os.getenv("azure_openai_api_key") # Here you have to mention your azure openai api key.
api_version= os.getenv("azure_api_version") # Here you have to mention your azure openai api version
azure_endpoint= os.getenv("azure_endpoint") # Here you have to mention your azure openai endpoint
azure_deployment= os.getenv("azure_deployment_name") # Here you have to mention your azure openai deployment name

# As the current llm model might have trained in the past, we can use the current date to get the latest information.
current_date = datetime.date.today().strftime("%d-%m-%Y")

llm = LLM(
    api_key= api_key,
    base_url= azure_endpoint,
    model="azure/"+ azure_deployment,
    api_version= api_version,
    temperature= 0.7
)

# Initialize a senior researcher agent with memory and verbose mode.
news_researcher=Agent(
    role= "Senior Researcher",
    goal= "Unccover ground breaking technologies in {topic}",
    verbose= True,
    memory= True,
    backstory= (
        "You're a seasoned researcher with a keen eye for detail. You have a knack for uncovering groundbreaking news and trends in the field of {topic}. Note: current date is " + current_date
    ),
    tools= [tool],
    llm= llm,
    allow_delegation= True
)

# creating a write agent with custom tools responsible in writing news blog
news_writer= Agent(
    role= "Writer",
    goal= "Write an engaging blog post about {topic}",
    verbose= True,
    memory= True,
    backstory= (
        "You're a skilled writer with a passion for storytelling. You have a knack for turning complex ideas into compelling narratives that captivate readers. Note: current date is " + current_date
    ),
    tools= [tool],
    llm= llm,
    allow_delegation= False
)