#use pandas as a way to load questions into a dataframe
import pandas as pd

def load_questions(file_path)
    return pd.read_csv(file_path)


def get_next_question(questions_df, current_question_id, answer):
    #will retrieve next question based on answer
    if answer.lower() == 'yes':
        next_question_id = questions_df.loc[questions_df['question_id'] == current_question_id, 'yes_next_question'].values[0]
    else:
        next_question_id = questions_df.loc[questions_df['question_id'] == current_question_id, 'no_next_question'].values[0]
    return next_question_id if pd.notna(next_question_id) else None


def run_survey(questions_df):
    #run survey with the most updated csv file when script is ran
    current_question_id = questions_df['question_id'].iloc[0] #starts off with the first question
    results = {} #stores answers

    while current_question_id is not None:
        #Retrieves the current question
        question = questions_df.loc[questions_df['question_id'] == current_question_id]
        question_text = question['question_text'].values[0]
        result_key = question['result_key'].values[0]

        #ask the user
        print(question_text)
        answer = input("Enter 'yes' or 'no': ").strip().lower()

        #Store the result based on result_key
        results[result_key] = answer

        #Determine next quesion
        current_question_id = get_next_question(questions_df, current_question_id, answer)
    return results


#Main function for survey script
if __name__ == "__main__":
    #Load questions from CSV
    file_path = 'survey_questions.csv' 
    questions_df = load_questions(file_path)

    #running the survey in order to capture results
    results = run_survey(questions_df)

    #Display survey results, (could potentially export results to desired location as well)
    display_results(results) #customize display_results() function to desired function
    save_results_to_csv(results, output_file='survey_results.csv')
