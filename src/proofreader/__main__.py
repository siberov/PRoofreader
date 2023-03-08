import os
import sys
from dotenv import load_dotenv
from proofreader import Proofreader

load_dotenv()
owner = sys.argv[1]
repo = sys.argv[2]
pull_request_id = int(sys.argv[3])
pr = Proofreader(os.getenv("GITHUB_PAT"), owner, repo, pull_request_id)
#suggestions = pr.check_pr(pull_request_id)
#pr.make_suggestions()
#print(suggestions)
with open('TEST_README.md', 'r') as f:
    readme = f.read()
    pr.test_readme(readme)
