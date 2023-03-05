import logging
import requests
from github import Github

def foo():
    return 2

class Proofreader:
    def __init__(self, pat: str, repo: str, pull_request_id: int):
        self.g = Github(pat)
        self.pull_request = self.g.get_repo(repo).get_pull(pull_request_id)
        self.latest_commit = self.pull_request.get_commits().reversed[0]


    def get_user(self) -> str:
        return self.g.get_user().login
    
    def check_pr(self, pull_request_id: int) -> list[str]:
        #if self.g.get_repo("repo")
        return ["test"]
    
    def make_suggestions(self):
        self.pull_request.create_review_comment("the body", self.latest_commit, "./README.md", 1)
