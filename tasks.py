from crewai import Task
from tools import tool
from agents import news_researcher, news_writer
import datetime

# As the current llm model might have trained in the past, we can use the current date to get the latest information.
current_date = datetime.date.today().strftime("%d-%m-%Y")

# Research Task
research_task= Task(
    description= (
        "Identify the latest trends and breakthroughs in {topic}. Focus on providing detailed insights and analysis on the most important developments in the field."
        "Also focus on identifying pros and cons and the overall narrative of the topic. Your final output should be a comprehensive report that should clearly articulate all the key points and aspects of the topic."
        "You should provide recommendations, market opportunities (future outlook) and potential risks based on your analysis. Note: current date is " + current_date
    ),
    expected_output= "A comprehensive 5 paragraphs long report detailing the latest trends, breakthroughs, pros and cons, recommendations, market opportunities and potential risks in the field of {topic}.",
    tools= [tool],
    agent= news_researcher
)

# Writing Task with languate model configuration.
write_task= Task(
    description= (
        "Write an engaging blog post about the latest developments in {topic}. Focus on crafting a compelling narrative that captures the essence of the topic and engages the readers."
        "Your blog post should be informative, engaging, and well-structured to keep the readers interested throughout. Make sure to include key insights, trends, and analysis in your blog post. Note: current date is " + current_date
    ),
    expected_output= "A conprehensive 5 paragraphs long engaging blog post that covers the latest developments, key insights, trends, and analysis in {topic}. Formatted as markdown.",
    tools= [tool],
    agent= news_writer,
    async_execution= False,
    output_file= "blog_post.md" # Output file name for the blog post. This will be saved in the current working directory.
)