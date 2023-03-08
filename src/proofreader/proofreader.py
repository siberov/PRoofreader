import logging
import json
import requests
from github import Github

def foo():
    return 2

class Proofreader:
    def __init__(self, pat: str, owner: str, repo: str, pull_number: int):
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {pat}",
            "X-GitHub-Api-Version": "2022-11-28"
        }
        self.pat = pat
        self.owner = owner
        self.repo = repo
        self.pull_number = pull_number

    def get_user(self) -> str:
        return self.g.get_user().login
    
    def check_pr(self, pull_request_id: int) -> list[str]:
        #if self.g.get_repo("repo")
        return ["test"]

    def _is_readme_modified(self) -> bool:
        # From schema in https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#list-pull-requests-files
        modified_statuses = ["added", "removed", "modified", "renamed", "copied", "changed"]
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls/{self.pull_number}/files"
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            logging.error(f"Could not get files for pull request {self.pull_number}")
            raise Exception(f"Could not get files for pull request {self.pull_number}")
        files = response.json()
        for file in files:
            if file["filename"] == "README.md" and file["status"] in modified_statuses:
                return True
        return False

    def _get_latest_commit_sha(self) -> str:
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls/{self.pull_number}"
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            logging.error(f"Could not get latest commit sha for pull request {self.pull_number}")
            raise Exception(f"Could not get latest commit sha for pull request {self.pull_number}")
        return response.json()["head"]["sha"]
    
    def make_suggestions(self):
        message = "```suggestion\ndu borde göra så här ist"
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls/{self.pull_number}/comments"
        body = {
            "body": message,
            "path": "README.md",
            "start_line": 1,
            "start_side": "RIGHT",
            "line": 2,
            "side": "RIGHT",
            "commit_id": self._get_latest_commit_sha()
        }
        # response = requests.post(url, headers=self.headers, data=json.dumps(body))
        # logging.info(response.json())
        # print(response.json())
        # logging.info(response.status_code)
        # print(response.status_code)