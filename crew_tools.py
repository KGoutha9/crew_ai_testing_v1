from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import random
from typing import Type

class emp_name_tools(BaseModel):
    employee_name: str = Field(..., description="The name of the employee.")
class emp_id_tools(BaseModel):
    employee_ID: str = Field(..., description="The ID of the employee.")

class Input(BaseModel):
    user_query: str = Field(..., description="The user query to process.")


class EmployeeSupervisorTool(BaseTool):
    name: str = "get_employee_supervisor"
    description: str = "Returns the supervisor for a given employee ID."
    args_schema: Type[BaseModel]  = emp_id_tools
    
    def _run(self, employee_ID: str) -> str:
        if not employee_ID:
            return "internal processing error :Employee ID is required."
        list_of_supervisors = ['Michael', 'Jessica', 'David', 'Ashley', 'Christopher']
        supervisor = random.choice(list_of_supervisors)
        return f"The supervisor for the given employee is {supervisor}"
    
class get_employee_locationTool(BaseTool):
    name: str = "get_employee_location"
    description: str = "Returns the location of a given employee."
    args_schema: Type[BaseModel] = emp_name_tools

    def _run(self, employee_name: str) -> str:
        if not employee_name:
            return "internal processing error :Employee name is required."
        list_of_locations = ["Hyderbad", "Bangalore", "Chennai", "Mumbai"]
        location = random.choice(list_of_locations)
        return f"The location for {employee_name} is {location}"

class get_employee_IDTool(BaseTool):
    name:str = "get_employee_ID"
    description:str = "Returns the employee ID for a given employee name."
    args_schema: Type[BaseModel] = emp_name_tools

    def _run(self, employee_name: str) -> str:
        if not employee_name:
            return "internal processing error :Employee name is required."
        list_of_ids = ['abd104', '3ni3n', '93jnj', 'ikh2k']
        employee_ID = random.choice(list_of_ids)
        return f"The employee ID for {employee_name} is {employee_ID}"
    

class get_employee_skill_setTool(BaseTool):
    name: str = "get_employee_skill_set"
    description: str = "Returns the skill set of a given employee ID."
    args_schema: Type[BaseModel] = emp_id_tools

    def _run(self, employee_ID: str) -> str:
        if not employee_ID:
            return "internal processing error :Employee ID is required."
        skill = random.choice(["Machine Learning", "Generative AI", "ML Ops", "Image Analysis"])
        return f"The primary skill for the employee with ID {employee_ID} is {skill}"