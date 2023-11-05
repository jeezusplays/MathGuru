from .agents import *
import json

def textToQuestions(text_list,level:int):
    """
    Converts OCR text to list of dicts

    returns:
    [
        {
            "ocr_question": list["Original question"],
            "metadata" : {
                            "level": 5,
                            "enoughContext": bool,
                            "topics": ["Word Problems", "Multiplication", "Division"],
                            "difficulty": "Medium"
                         }
        }
    ]
    """
    question_list = get_questions(text_list)
    refined_questions = clean_questions(json.dumps(question_list['question_list']))
    refined_questions = json.loads(refined_questions['refined_questions'])['questions']

    question_dict_list = []
    for question_list in refined_questions:
        meta = get_metadata({
            "question_text":question_list,
            "primary_level":level
            })
        
        meta = meta['question_metadata']
        question_dict_list.append({
            "ocr_question":question_list,
            "metadata":json.loads(meta)
        })

    return question_dict_list

def _getNewQuestion(question_dict):
        question_list = question_dict['ocr_question']
        meta = question_dict['metadata']
        if not meta.get("enoughContext", False):
             return None
        new_question = generate_question({
            "question_text":question_list,
            "question_metadata":meta
        })

        new_question=json.loads(new_question['regenerated_question'])['question']

        return {
            "ocr_question":question_list,
            "metadata":meta,
            "new_question":new_question
        }

# Consider multi treading
def generateQuestions(questions_dict_list:list):
    """
    Generate new question from a list of scanned question

    questions_dict_list structure:
    [
        {
            "ocr_question": list["Original question"],
            "metadata" : {
                            "level": 5,
                            "enoughContext": bool,
                            "topics": ["Word Problems", "Multiplication", "Division"],
                            "difficulty": "Medium"
                         }
        }
    ]

    returns:
    [
        {
            "ocr_question": list["Original question"],
            "metadata" : {
                            "level": 5,
                            "topics": ["Word Problems", "Multiplication", "Division"],
                            "difficulty": "Medium"
                         },
            "new_question": list["New generated question"]
        }
    ]
    """
    
    return list(map(_getNewQuestion,questions_dict_list))



if __name__ == "__main__":

    LEVEL = 5
    # Opening JSON file
    f = open('app\\test.json')
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    data_string = json.dumps(data)
    print(data)
    question_list = get_questions(data_string)
    refined_questions = clean_questions(json.dumps(question_list['question_list']))
    refined_questions = json.loads(refined_questions['refined_questions'])['questions']

    final_questions=[]
    for question_list in refined_questions:
        print(question_list)
        meta = get_metadata({
            "question_text":question_list,
            "primary_level":LEVEL
            })
        
        meta = meta['question_metadata']
        print(meta)
        new_question = generate_question({
            "question_text":question_list,
            "question_metadata":meta
        })
        new_question=json.loads(new_question['regenerated_question'])['question']

        final_questions.append({
            "ocr_question":question_list,
            "metadata":meta,
            "new_question":new_question
        })

        print(f"Old questions: {question_list}\nMeta: {meta} \nNew Question: {new_question}")

    print([i['new_question'] for i in final_questions ])