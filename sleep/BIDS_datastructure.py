import os
import shutil

def create_structure(base_dir, num_subjects=60):
    for i in range(1, num_subjects + 1):
        subject_id = f"RY{i:03}"
        for session in ["N0", "N1", "N2"]:
            session_path = os.path.join(base_dir, subject_id, session)
            os.makedirs(os.path.join(session_path, "actigraphy"), exist_ok=True)
            os.makedirs(os.path.join(session_path, "xenxor"), exist_ok=True)
            os.makedirs(os.path.join(session_path, "eeg"), exist_ok=True)
            if session in ["N1", "N2"]:
                os.makedirs(os.path.join(session_path, "recordings"), exist_ok=True)
                # Crea la struttura aggiuntiva per recall
                recall_path = os.path.join(session_path, "eeg", "recall")
                # Rimuovi le cartelle 1 e 2 se esistono
                old_folders = ["1", "2"]
                for folder in old_folders:
                    old_path = os.path.join(recall_path, folder)
                    if os.path.exists(old_path):
                        shutil.rmtree(old_path)
                # Crea le nuove cartelle
                os.makedirs(os.path.join(recall_path, "evening"), exist_ok=True)
                os.makedirs(os.path.join(recall_path, "morning"), exist_ok=True)
            print(f"Created structure for {subject_id} {session}")

def copy_actigraphy(source_dir, dest_dir):
    for file in os.listdir(source_dir):
        if file.startswith("RY") and file.endswith(".mtn"):
            parts = file.split('_')
            subject_id = parts[0]
            session = parts[1]
            dest_path = os.path.join(dest_dir, subject_id, session, "actigraphy")
            os.makedirs(dest_path, exist_ok=True)
            src_file = os.path.join(source_dir, file)
            dest_file = os.path.join(dest_path, file)
            shutil.copy(src_file, dest_file)
            print(f"Copied {src_file} to {dest_file}")

def copy_eeg(source_dir, dest_dir):
    for subject in os.listdir(source_dir):
        subject_path = os.path.join(source_dir, subject)
        if os.path.isdir(subject_path) and subject.startswith("RY"):
            for session in os.listdir(subject_path):
                session_path = os.path.join(subject_path, session)
                if os.path.isdir(session_path) and session.startswith("N"):
                    for date_folder in os.listdir(session_path):
                        date_path = os.path.join(session_path, date_folder)
                        if os.path.isdir(date_path):
                            dest_path = os.path.join(dest_dir, subject, session, "eeg")
                            os.makedirs(dest_path, exist_ok=True)
                            for file in os.listdir(date_path):
                                if file.endswith((".eeg", ".vhdr", ".vmrk")):
                                    src_file = os.path.join(date_path, file)
                                    dest_file = os.path.join(dest_path, file)
                                    shutil.copy(src_file, dest_file)
                                    print(f"Copied {src_file} to {dest_file}")

def copy_recordings(source_dir, dest_dir):
    for subject in os.listdir(source_dir):
        subject_path = os.path.join(source_dir, subject)
        if os.path.isdir(subject_path) and subject.startswith("RY"):
            for session in os.listdir(subject_path):
                session_path = os.path.join(subject_path, session)
                if os.path.isdir(session_path) and session.startswith("N"):
                    dest_path = os.path.join(dest_dir, subject, session, "recordings")
                    os.makedirs(dest_path, exist_ok=True)
                    for file in os.listdir(session_path):
                        src_file = os.path.join(session_path, file)
                        dest_file = os.path.join(dest_path, file)
                        shutil.copy(src_file, dest_file)
                        print(f"Copied {src_file} to {dest_file}")

def copy_xensor(source_dir, dest_dir):
    for file in os.listdir(source_dir):
        if file.startswith("RY") and file.endswith(".elc"):
            parts = file.split('_')
            subject_id = parts[0]
            session = parts[1]
            dest_path = os.path.join(dest_dir, subject_id, session, "xenxor")
            os.makedirs(dest_path, exist_ok=True)
            src_file = os.path.join(source_dir, file)
            dest_file = os.path.join(dest_path, file)
            shutil.copy(src_file, dest_file)
            print(f"Copied {src_file} to {dest_file}")

def rename_folders(base_dir, num_subjects=60):
    for i in range(1, num_subjects + 1):
        subject_id = f"RY{i:03}"
        for session in ["N0", "N1", "N2"]:
            old_path = os.path.join(base_dir, subject_id, session, "xenxor")
            new_path = os.path.join(base_dir, subject_id, session, "xensor")
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                print(f"Renamed {old_path} to {new_path}")

if __name__ == "__main__":
    elements_dir = "/Volumes/Elements/remedy"
    remedy_dataset_dir = "/Volumes/Elements/remedy_dataset"
    
    # Crea la struttura per 60 partecipanti
    # create_structure(remedy_dataset_dir, num_subjects=60)
    
    # Copia i dati esistenti
    # copy_actigraphy(os.path.join(elements_dir, "actigraphy"), remedy_dataset_dir)
    # copy_eeg(os.path.join(elements_dir, "eeg"), remedy_dataset_dir)
    # copy_recordings(os.path.join(elements_dir, "recordings"), remedy_dataset_dir)
    # copy_xensor(os.path.join(elements_dir, "xensor"), remedy_dataset_dir)

    # Rinomina le cartelle xenxor in xensor
    rename_folders(remedy_dataset_dir, num_subjects=60)