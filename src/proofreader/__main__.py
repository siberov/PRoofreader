import os
import sys
from dotenv import load_dotenv
from proofreader import Proofreader

load_dotenv()
repo = sys.argv[1]
pull_request_id = int(sys.argv[2])
pr = Proofreader(os.getenv("GITHUB_PAT"), repo, pull_request_id)
suggestions = pr.check_pr(pull_request_id)
pr.make_suggestions()
print(suggestions)
