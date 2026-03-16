import json
import os
import re

def strip_tags(text):
    if not text:
        return ""
    # Remove HTML tags using a simple regex
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text).strip()

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
        
        # Strip tags for everything that goes into Rmd to avoid line break issues
        prompt = strip_tags(q.get('prompt', ''))
        q_type = q.get('type', '')
        options = q.get('options', [])
        
        extype = "schoice" if q_type == "Single Answer" else "mchoice"
        exsolution = "".join(["1" if opt.get('correct') else "0" for opt in options])
        
        rmd_content = "Question\n========\n"
        rmd_content += prompt + "\n\n"
        rmd_content += "Answerlist\n----------\n"
        for j, opt in enumerate(options):
            letter = chr(65 + j) # A, B, C...
            rmd_content += f"* {letter}. {strip_tags(opt.get('text', ''))}\n"
        
        # Removed the 'A. ' replacement hack as it was skipping the first label correctly provided by the loop.
        
        rmd_content += "\nSolution\n========\n"
        rmd_content += "Feedback op de opties:\n\n"
        rmd_content += "Answerlist\n----------\n"
        for opt in options:
            feedback = strip_tags(opt.get('feedback', ''))
            if not feedback:
                feedback = "Geen specifieke feedback beschikbaar."
            rmd_content += f"* {feedback}\n"
        
        rmd_content += "\nMeta-information\n================\n"
        rmd_content += f"exname: question-{i+1}\n"
        rmd_content += f"extype: {extype}\n"
        rmd_content += f"exsolution: {exsolution}\n"
        
        with open(filepath, 'w', encoding='utf-8') as f_out:
            f_out.write(rmd_content)
        print(f"Generated {filename}")

    return question_files

if __name__ == "__main__":
    files = convert_to_rmd()
    print(f"Total questions generated: {len(files)}")
