import os
import os.path as op
import whisper


def transcribe_audio(file_path, model):
    """
    Transcribes an audio file using a transcription model.

    Args:
        file_path (str): The path to the audio file to be transcribed.
        model: The transcription model to use.

    Returns:
        str: The transcribed text from the audio.
    """
    print(f"Transcribing {file_path}...")
    result = model.transcribe(file_path)
    return result['text']

def process_subjects(base_path, model, subject_ids):
    """
    Manages transcription for a set of subjects.

    Args:
        base_path (str): The base path where the subjects' data is located.
        model: The transcription model to use.
        subject_ids (list): A list of subject IDs to process.

    """
    subject_ids = sorted(subject_ids)  # Sort subject_ids to ensure correct order

    for subject in subject_ids:
        subject_path = op.join(base_path, subject)
        print(f"Checking subject path: {subject_path}")
        if op.isdir(subject_path):
            for session in ["N1", "N2"]:
                session_path = op.join(subject_path, session)
                print(f"Checking session path: {session_path}")
                if op.exists(session_path):
                    for task in ["task_D", "task_E"]:
                        task_path = op.join(session_path, task)
                        print(f"Checking task path: {task_path}")
                        if op.exists(task_path):
                            for file in os.listdir(task_path):
                                if file.endswith(".wav"):
                                    file_path = op.join(task_path, file)
                                    print(f"Found file: {file_path}")
                                    output_file = get_output_file(subject, session, task, file)
                                    if not op.exists(output_file):
                                        transcription = transcribe_audio(file_path, model)
                                        save_transcription(transcription, output_file)
                                        print(f"Saved transcription for {file_path}")
                                    else:
                                        print(f"Transcription already exists for {file_path}")

def get_output_file(subject, session, task, file_name):
    """
    Generates the output file path for a transcription.

    Args:
        subject (str): The subject ID.
        session (str): The session (e.g., "N1", "N2").
        task (str): The task (e.g., "task_D", "task_E").
        file_name (str): The original audio file name.

    Returns:
        str: The full path to the output text file.
    """
    base_dir = "sleep/recall" if task == "task_D" else "sleep/dream_reports"
    output_dir = op.join(base_dir, subject, session)
    op.makedirs(output_dir, exist_ok=True)
    return op.join(output_dir, file_name.replace(".wav", ".txt"))

def save_transcription(text, output_file):
    """
    Saves the transcribed text to a file.

    Args:
        text (str): The transcribed text to save.
        output_file (str): The path to the output file where the text will be saved.
    """
    with open(output_file, "w") as f:
        f.write(text)

if __name__ == "__main__":
    # This block is executed only if the script is run directly.
    # Sets the base path, loads the transcription model, and defines the subjects to process.
    base_path = "/Users/foscagiannotti/Desktop/python_projects/sleep/behavior"
    model = whisper.load_model("medium")  
    subject_ids = ["RY006", "RY007", "RY008"]  # Filter only the subjects to transcribe
    process_subjects(base_path, model, subject_ids)
