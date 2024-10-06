import os
from openai import OpenAI
import sqlite3

fdir = os.path.dirname(__file__)
def getPath(fname):
    return os.path.join(fdir, fname)

DBPath = getPath("CS452NaturalLanguageSQLProjectDB.db")
setupSqlPath = getPath("SqlSetup.txt")
setupSqlDataPath = getPath("SqlSetupData.txt")

if os.path.exists(DBPath):
    os.remove(DBPath)

openAiClient = OpenAI(
    api_key = "placeholder",
    organization = "placeholder"
)

with (
        open(setupSqlPath) as setupSqlFile,
        open(setupSqlDataPath) as setupSqlData
    ):
    setupSqlScript = setupSqlFile.read()
    setupSqlDataScript = setupSqlData.read()

sqliteCon = sqlite3.connect(DBPath)
sqliteCursor = sqliteCon.cursor()

sqliteCursor.executescript(setupSqlScript)
sqliteCursor.executescript(setupSqlDataScript)

def runSql(query):
    result = sqliteCursor.execute(query).fetchall()
    return result

def getChatGptResponse(content):
    stream = openAiClient.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[{"role": "user", "content": content}],
        stream=True,
    )

    responseList = []
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            responseList.append(chunk.choices[0].delta.content)

    result = "".join(responseList)
    return result

strategies = {
    "zero_shot": setupSqlScript + "That was the create statements for my SQL database. Answer the following question with the correct SQL select statement and ONLY the SQL and nothing else(no begin or ending sql ''' markers): ",
    "single_domain_double_shot": (setupSqlScript + 
                   " That was the create statements for my SQL database. I want you to answer a question with the correct SQL select statement and ONLY the SQL and nothing else(no begin or ending sql ''' markers). Here is an example of what I'm looking for:  " +
                   " Question: Which player has the highest level? " + 
                   " Answer: SELECT Username FROM Player WHERE Level = (SELECT Max(Level) FROM Player)" +
                   " Here is the question I want you to answer: ")
}

print("Natural Language Database Assistant Running ...")
running = True
while running:
    question = input("What do you want to know?(type X to close)\n")
    if question == "X":
        running = False
    else:
        for strategy in strategies:
            try:
                sqlSyntaxResponse = getChatGptResponse(strategies[strategy] + " " + question)
                print(sqlSyntaxResponse)
                queryRawResponse = str(runSql(sqlSyntaxResponse))
                print(queryRawResponse)
                friendlyResultsPrompt = "I asked a question \"" + question +"\" and the response was \""+queryRawResponse+"\" Please, just give a concise response in a more friendly way? Please do not give any other suggests or chatter."
                friendlyResponse = getChatGptResponse(friendlyResultsPrompt)
                print(friendlyResponse)
            except Exception as err:
                error = str(err)
                print(err)

