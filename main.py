from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from smolagents import CodeAgent, HfApiModel
from gitpush_code_tool import GitPushCodeTool
from file_reader_tool import FileReaderTool
from code_file_tool import CodeFileTool

app = FastAPI()

# Define the request model
class TaskRequest(BaseModel):
    github_username: str
    github_token: str
    repo_name: str
    task: str

@app.post("/run-task")
def run_task(request: TaskRequest):
    try:
        # Set base directory for consistency across tools
        base_dir = f"/tmp/{request.repo_name}"

        # Instantiate tools with dynamic parameters
        git_tool = GitPushCodeTool(
            github_username=request.github_username,
            github_token=request.github_token,
            repo_name=request.repo_name
        )
        file_reader = FileReaderTool(base_directory=base_dir)
        code_file_tool = CodeFileTool(base_directory=base_dir)

        # Create agent with tools and model
        agent = CodeAgent(
            tools=[git_tool, code_file_tool, file_reader],
            model=HfApiModel(),
            additional_authorized_imports=
            ['random',
             'datetime',
             'time',
             'statistics',
             'collections',
             'streamlit',
             'unicodedata',
             're',
             'stat',
             'itertools',
             'math',
             'queue'
             ]
        )

        # Run the agent with the task
        result = agent.run(f"create a well defined well structured streamlit app for {request.task} create any file needed and save to github")
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")