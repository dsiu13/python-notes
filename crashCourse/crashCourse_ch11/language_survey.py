from survey import anonSurvey

question = "what language did you first learn to code in?"
my_survey = anonSurvey(question)

my_survey.show_questions()
print("enter 'q' to quit anytime")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_res(response)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_all()
