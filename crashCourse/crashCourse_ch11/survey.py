class anonSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_questions(self):
        print(self.question)

    def store_res(self, new_res):
        self.responses.append(new_res)

    def show_all(self):
        print("Survey Results: ")
        for response in responses:
            print('- ' + response)
