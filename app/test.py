from AIHelper import *
import json
 
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