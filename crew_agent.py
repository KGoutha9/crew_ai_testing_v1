from crewai import Agent
from crewai import LLM
import os
from crew_tools import EmployeeSupervisorTool, get_employee_locationTool, get_employee_IDTool, get_employee_skill_setTool



os.environ["AZURE_API_KEY"] = "<your-azure-api-key-here>" # e.g., "your-azure-api-key"
os.environ["AZURE_API_BASE"] = "<your-azure-api-base-url-here>"  # e.g., "https://<your-resource-name>.openai.azure.com/"
os.environ["AZURE_API_VERSION"] = "2024-10-21" # e.g., "2024-10-21"
os.environ["OPENAI_API_KEY"] = "dummy" #this needed to be dummy to avoid conflict with Azure API key
# llm

gpt_model = LLM(
    model="azure/gpt-4o",
    api_version="2023-05-15"
)

## Employee details provider agent
employee_info_agent = Agent(
    role='employee info agent',
    goal="give the exact information about the employee based on the user query",
    verbose=True,
    memoryview=True,
    backstory="""You are an employee information agent. Your task is to provide accurate and relevant information about employees.""",
    tools=[EmployeeSupervisorTool(), get_employee_locationTool(), get_employee_IDTool(), get_employee_skill_setTool()],
    llm=gpt_model,
    allow_delegation= False)