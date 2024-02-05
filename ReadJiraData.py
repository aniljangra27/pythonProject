# import the installed Jira library
from jira import JIRA

# Specify a server key. It is your domain
# name link.
jiraOptions = {'server': "https://txxxxxxpython.atlassian.net"}

# Get a JIRA client instance, Pass
# Authentication parameters
# and Server name.
# emailID = your emailID
# token = token you receive after registration
jira = JIRA(options = jiraOptions,
			basic_auth = ("anil.kumar@akqa.com",
						"bj9xxxxxxxxxxxxxxxxxxx5A"))

# While fetching details of a single issue,
# pass its UniqueID or Key.
singleIssue = jira.issue('MED-1')
print('{}: {}:{}'.format(singleIssue.key,
						singleIssue.fields.summary,
						singleIssue.fields.reporter.displayName))
