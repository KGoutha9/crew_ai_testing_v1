from crewai import Task
from crew_tools import EmployeeSupervisorTool, get_employee_locationTool, get_employee_IDTool, get_employee_skill_setTool


# tasks for crewagent

#get empoyee id

get_employee_id_task = Task(
    name="get_employee_id and supervisor",
    description="helps to get the employee ID and supervisor based on the employee name",
    tools=[get_employee_IDTool(), EmployeeSupervisorTool()],
    async_execution=False,
    expected_output="The employee ID/supervisor is extracted sucessfully")

# get employee supervisor task
# get_employee_supervisor_task = Task(
#     name="get_employee_supervisor",
#     description= "get the supervisor for the given employee ID",
#     tools= [EmployeeSupervisorTool()],
#     context=[get_employee_id_task],
#     async_execution=False,
#     expected_output="The supervisor for the given employee has extracted successfully")


#get employee location task
get_employee_location_task = Task(
    name="get_employee_location",
    description= "get the location of the employee based on the employee name",
    tools=[get_employee_locationTool()],
    async_execution=False,
    expected_output="The location for the employee is extracted successfully")

#get employee skill set task
get_employee_skill_set_task = Task(
    name="get_employee_skill_set",
    description= "get the primary skill set of the employee based on the employee ID",
    tools=[get_employee_skill_setTool()],
    expected_output="The primary skill associated with the employee has been extracted successfully",
    async_execution=False
)

