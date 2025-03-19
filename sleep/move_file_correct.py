import os
import shutil

def move_files(base_path, target_base_path):
    for folder in ["dream_reports", "recall"]:
        source_path = os.path.join(base_path, folder)
        target_path = os.path.join(target_base_path, folder)
        
        if os.path.exists(source_path):
            for subject in os.listdir(source_path):
                subject_source_path = os.path.join(source_path, subject)
                subject_target_path = os.path.join(target_path, subject)
                
                if os.path.isdir(subject_source_path):
                    os.makedirs(subject_target_path, exist_ok=True)
                    
                    for file in os.listdir(subject_source_path):
                        file_source_path = os.path.join(subject_source_path, file)
                        file_target_path = os.path.join(subject_target_path, file)
                        
                        if os.path.isfile(file_source_path):
                            shutil.move(file_source_path, file_target_path)
                            print(f"Mosso {file_source_path} a {file_target_path}")

if __name__ == "__main__":
    base_path = "/Users/foscagiannotti/Desktop/python_projects"
    target_base_path = "/Users/foscagiannotti/Desktop/python_projects/sleep"
    move_files(base_path, target_base_path)