import json
import os

def convert_to_rmd():
    source_file = r'd:\Temp\MOVEL AI 2025-2026\input-docs\quiz.json'
    output_dir = r'd:\Temp\MOVEL AI 2025-2026\quiz'
    
    if not os.path.exists(source_file):
        print(f"Error: {source_file} not found.")
        return

    with open(source_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    question_files = []
    
    for i, q in enumerate(data):
        filename = f"question-{i+1}.Rmd"
        filepath = os.path.join(output_dir, filename)
        question_files.append(filename)
        
        prompt = q.get('prompt', '').strip()
        q_type = q.get('type', '')
        options = q.get('options', [])
        
        extype = "schoice" if q_type == "Single Answer" else "mchoice"
        exsolution = "".join(["1" if opt.get('correct') else "0" for opt in options])
        
        rmd_content = "Question\n========\n"
        rmd_content += prompt + "\n\n"
        rmd_content += "Answerlist\n----------\n"
        for opt in options:
            rmd_content += f"* {opt.get('text', '').strip()}\n"
        
        rmd_content += "\nSolution\n========\n"
        # Combine feedbacks for solution or just use a generic one
        for opt in options:
            if opt.get('correct') and opt.get('feedback'):
                rmd_content += opt.get('feedback').strip() + "\n"
        
        rmd_content += "\nAnswerlist\n----------\n"
        for opt in options:
            is_correct = "True" if opt.get('correct') else "False"
            rmd_content += f"* {is_correct}\n"
            
        rmd_content += "\nMeta-information\n================\n"
        rmd_content += f"exname: question-{i+1}\n"
        rmd_content += f"extype: {extype}\n"
        rmd_content += f"exsolution: {exsolution}\n"
        
        with open(filepath, 'w', encoding='utf-8') as f_out:
            f_out.write(rmd_content)
        print(f"Generated {filename}")

    # Create a vector-style Rmd for multiple questions if needed, 
    # but exams2forms can often take a vector directly in the R call.
    # We will update quiz.qmd to point to the list of files or a master file.
    
    return question_files

if __name__ == "__main__":
    files = convert_to_rmd()
    print(f"Total questions generated: {len(files)}")
    # Print the list of files to be used in Quarto
    files_str = ", ".join([f'"{f}"' for f in files])
    print(f"FILE_LIST: c({files_str})")
