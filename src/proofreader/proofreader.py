import logging
import os
import json
import requests

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
        self.chatgpt_system_command = "You are a proofreader helping to improve the README.md file for a GitHub repository. You are given a paragraph from the README.md file and asked to write a better version of it. The README.md file is written in Markdown. You can use Markdown syntax to format your text."
        self.chatgpt_user_message_intro = "Help me improve the following paragraph. Answer with your improvements, followed by the special token <###> on a separate line, followed by a brief explanation of what you have changed. Only make suggestions if you find obvious improvements. If you don't find any, reply '###NO_SUGGESTION###'. The paragraph is as follows:"

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
        response = requests.post(url, headers=self.headers, data=json.dumps(body))
        logging.info(response.json())
        print(response.json())
        logging.info(response.status_code)
        print(response.status_code)

    def preprocess(self, readme: str):
        """Preprocesses the README.md file to make it easier to parse.
        Split the readme into paragraphs and treat the code blocks as paragraphs.
        Save start and end line numbers for each paragraph.
        """
        paragraphs = []
        current_paragraph = ""
        current_line = 0
        current_paragraph_start = 0
        for line in readme.splitlines():
            current_line += 1
            if line.startswith("#"):
                paragraphs.append(
                        {
                        "start": current_line,
                        "end": current_line, 
                        "text": line
                        }
                    )
            else:
                # new paragraph
                if current_paragraph == "":
                    current_paragraph_start = current_line
                    current_paragraph += line + "\n"
                # end of paragraph
                elif line == "" and current_paragraph:
                    paragraphs.append(
                        {
                            "start": current_paragraph_start, 
                            "end": current_line, 
                            "text": current_paragraph
                            }
                        )
                    current_paragraph = ""
                else:
                    current_paragraph += line + "\n"
        # Edge case for last paragraph if it does not end in new line
        if current_paragraph:
            paragraphs.append(
                    {
                    "start": current_paragraph_start, 
                    "end": current_line, 
                    "text": current_paragraph
                    }
                )
        return paragraphs
    
    def make_corrections(self, processed_readme):
        """Makes corrections to the README.md file.
        processed_readme: list of paragraphs
        """
        corrected_readme = []
        # Iterate through the paragraphs, and make an API call to ChatGPT for each one
        # Save the suggestions in corrected_readme
        for paragraph in processed_readme:
            suggestion, motivation = self._get_suggestion(paragraph["text"])
            if suggestion == "###NO_SUGGESTION###":
                continue
            corrected_readme.append({
                "start": paragraph["start"],
                "end": paragraph["end"],
                "text": suggestion,
                "motivation": motivation
                })
        return corrected_readme

    def _get_suggestion(self, paragraph: str) -> str:
        """Makes an API call to ChatGPT to get a suggestion for the paragraph.
        paragraph: the paragraph to get a suggestion for
        """
        api_key = os.getenv('OPENAI_API_KEY')
        url = "https://api.openai.com/v1/chat/completions"

        headers = {
            "Authorization": "Bearer " + api_key,
            "Content-Type": "application/json"
        }

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": self.chatgpt_system_command
                },
                {
                    "role": "user",
                    "content": self.chatgpt_user_message_intro + "\n" + paragraph
                }
            ]
        }
        print("Asking for improvement on: " + paragraph)
        response = requests.post(url, headers=headers, json=data)
        print("Got response: " + response.json()["choices"][0]["message"]["content"])
        # Todo: Handle error response
        suggestion = response.json()["choices"][0]["message"]["content"]
        if "<###>" in suggestion:
            return suggestion.split("<###>")[0], suggestion.split("<###>")[1]
        else:
            return "###NO_SUGGESTION###", "###NO_SUGGESTION###"
    
    def test_readme(self, readme):
        preprocessed = self.preprocess(readme)
        corrected = self.make_corrections(preprocessed)
        print(corrected)



