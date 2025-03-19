import mne

# Specifica il percorso del file .vhdr
vhdr_file = '/Volumes/Blind2025/remedy_dataset/RY002/N0/eeg/RY002__N0_2025-01-13.vhdr'

# Carica i dati usando MNE
raw = mne.io.read_raw_brainvision(vhdr_file, preload=True)

# Specifica il percorso per il file EDF di output
edf_file = '//Volumes/Blind2025/remedy_dataset/RY002/N0/eeg/RY002__N0_2025-01-13.edf'

# Salva i dati in formato EDF
raw.export(edf_file, fmt='edf', overwrite=True)