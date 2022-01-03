import re
import string

def preprocessing(documents):
    documents_clean = []
    for d in documents:
        # Remove Unicode
        document_test = re.sub(r'[^\x00-\x7F]+', ' ', d)
        # Remove Mentions
        document_test = re.sub(r'@\w+', '', document_test)
        # Lowercase the document
        document_test = document_test.lower()
        # Remove punctuations
        document_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', document_test)
        # Lowercase the numbers
        document_test = re.sub(r'[0-9]', '', document_test)
        # Remove the doubled space
        document_test = re.sub(r'\s{2,}', ' ', document_test)
        documents_clean.append(document_test)   
    return documents_clean  