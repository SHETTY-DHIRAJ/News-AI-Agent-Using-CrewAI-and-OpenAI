from crewai import Crew, Process
from agents import news_researcher, news_writer
from tasks import research_task, write_task

# Forming the crew with some enhanced configuration.
crew= Crew(
    agents= [news_researcher, news_writer],
    tasks= [research_task, write_task],
    process= Process.sequential
)

# Starting the tasks execution process with enhanced feedback.
user_input= input("Enter the topic you want to research and write about: ")
result= crew.kickoff(inputs= {"topic": user_input})