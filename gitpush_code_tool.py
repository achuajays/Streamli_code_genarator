from smolagents import Tool
import git
import os
import requests

class GitPushCodeTool(Tool):
    name = "git_push_code_tool"
    description = """
    Stages all files in the local repository, commits them with the provided commit message,
    and pushes them to the GitHub repository. Assumes files are created in the repo directory.
    """

    inputs = {
        "commit_message": {
            "type": "string",
            "description": "Commit message for the Git commit. Defaults to 'Update files' if empty.",
        }
    }
    output_type = "string"

    def __init__(self, github_username: str, github_token: str, repo_name: str, **kwargs):
        super().__init__(**kwargs)
        self.github_username = github_username
        self.github_token = github_token
        self.repo_name = repo_name
        self.repo_path = f"/tmp/{repo_name}"  # Consistent directory structure
        self.branch = "main"
        self.GITHUB_API_URL = "https://api.github.com"

    def create_github_repo(self):
        """Checks if a GitHub repo exists and creates it if not."""
        repo_url = f"{self.GITHUB_API_URL}/repos/{self.github_username}/{self.repo_name}"
        headers = {"Authorization": f"token {self.github_token}"}

        response = requests.get(repo_url, headers=headers)
        if response.status_code == 200:
            return True

        create_repo_url = f"{self.GITHUB_API_URL}/user/repos"
        data = {"name": self.repo_name, "private": False}
        response = requests.post(create_repo_url, json=data, headers=headers)
        return response.status_code == 201

    def forward(self, commit_message: str):
        if not commit_message:
            commit_message = "Update files"

        try:
            if not self.create_github_repo():
                return "Failed to create GitHub repository. Check credentials."

            github_repo_url = f"https://{self.github_username}:{self.github_token}@github.com/{self.github_username}/{self.repo_name}.git"
            os.makedirs(self.repo_path, exist_ok=True)
            os.chdir(self.repo_path)

            repo = git.Repo(self.repo_path) if os.path.exists(os.path.join(self.repo_path, ".git")) else git.Repo.init(self.repo_path)

            readme_path = os.path.join(self.repo_path, "README.md")
            if not os.path.exists(readme_path):
                with open(readme_path, "w") as f:
                    f.write(f"# {self.repo_name}\n")

            repo.git.add(all=True)
            repo.index.commit(commit_message)
            repo.git.branch("-M", self.branch)

            if "origin" in [remote.name for remote in repo.remotes]:
                repo.remote("origin").set_url(github_repo_url)
            else:
                repo.create_remote("origin", github_repo_url)

            repo.remote("origin").push(self.branch, force=True)
            return f"Files pushed to '{self.repo_name}' with message: '{commit_message}'."
        except Exception as e:
            return f"Failed to push files: {str(e)}"