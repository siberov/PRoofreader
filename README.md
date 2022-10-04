# PRoofreader
Automated language correction through Git

## What is PRoofreader?
PRoofreader is a tool that allows you to automatically correct the language of your code. It does this by using a set of rules that are defined in a configuration file. These rules are then applied to your code and the corrections are committed to your repository.

## How does it work?
PRoofreader is a GitHub Action that runs on every push to your repository. It will then apply the rules defined in your configuration file to your code, commit the corrections to your repository and open a pull request with all suggested changes.

## How do I use it?
To use PRoofreader, you need to create a configuration file. This file is a YAML file that contains the rules that PRoofreader will apply to your code. The configuration file is then added to your repository and the PRoofreader Action is added to your workflow.

### Configuration file
The configuration file is a YAML file that contains the rules that PRoofreader will apply to your code. The configuration file is then added to your repository and the PRoofreader Action is added to your workflow.

#### Example

* [Language tool's API](https://languagetool.org/http-api/#!/default/post_check)

* Langueage (ex `en-US`) complete list here:

<details>
<summary>Click to expand</summary>

* en-US
* en-GB
* en-AU
---
</details>

* Ignore words (ex `["musicnn", "Gorwind"]`) to reduce false positives

### Workflow
The workflow is a YAML file that contains the steps that GitHub will run when a push is made to your repository. The workflow file is then added to your repository and GitHub will run the steps defined in the workflow file.