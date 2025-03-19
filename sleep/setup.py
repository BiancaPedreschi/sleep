from setuptools import setup, find_packages

setup(
    name='sleep',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'mne',
        'whispers',
        'wonambi',
        'PyQt5',
        # Aggiungi altre librerie qui
    ],
    author='Bianca Pedreschi',
    author_email='bianca.pedreschi@imtlucca.it',
    description='Progetto per l\'analisi del sonno',
    url='https://github.com/biancapedreschi/sleep',  # URL del repository, se disponibile
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: IMTLUCCA License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)