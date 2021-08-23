import json
import requests

def create_pull_request(project_name, repo_name, title, description, head_branch, base_branch, git_token):
   # """Creates the pull request for the head_branch against the base_branch"""
    git_pulls_api = "https://api.github.com/repos/{0}/{1}/pulls".format(
        project_name,
        repo_name)
    headers = {
        "Authorization": "token {0}".format(git_token),
        "Content-Type": "application/json"}

    payload = {
        "title": title,
        "body": description,
        "head": head_branch,
        "base": base_branch,
    }

    r = requests.post(
        git_pulls_api,
        headers=headers,
        data=json.dumps(payload))

    if not r.ok:
        print("Request Failed: {0}".format(r.text))

create_pull_request(
    "karthikaseleskannan", # project_name
    "gitpr", # repo_name
    "My pull request from python", # title
    "My pull request description", # description
    "karthikaseleskannan:testrepo", # head_branch
    "main", # base_branch
    "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", # git_token
)