from crewai import Crew, Process
#from crew_tasks import get_employee_id_task, get_employee_supervisor_task, get_employee_location_task, get_employee_skill_set_task
from crew_tasks import get_employee_id_task, get_employee_location_task, get_employee_skill_set_task

from crew_agent import employee_info_agent
import os
from crewai import LLM


os.environ["AZURE_API_KEY"] = "<your-azure-api-key-here>"  # e.g., "your-azure-api-key"
os.environ["AZURE_API_BASE"] = "<your-azure-api-base-url-here>"  # e.g., "https://<your-resource-name>.openai.azure.com/"
os.environ["AZURE_API_VERSION"] = "2024-10-21" # e.g., "2024-10-21"
os.environ["OPENAI_API_KEY"] = "dummy" # this needed to be dummy to avoid conflict with Azure API key

# llm
gpt_model = LLM(
    model="azure/gpt-4o",
    api_version="2023-05-15"
)

crew = Crew(
    agents=[employee_info_agent],
    #tasks= [get_employee_id_task, get_employee_supervisor_task, get_employee_location_task, get_employee_skill_set_task],
    tasks= [get_employee_id_task, get_employee_location_task, get_employee_skill_set_task],
    verbose=True,
    process= Process.hierarchical,
    memory=False,
    cache= True,
    max_rpm = 100,
    manager_llm= gpt_model)

result = crew.kickoff(inputs={'query': 'who is supervisor of employee named David?'})
print(result)



