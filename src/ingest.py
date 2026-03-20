"""
    This is the ingest portion of the code, allowing for Archie to look through files.
"""

import os
from PyPDF2 import PdfReader
import docx
from sentence_transformers import SentenceTransformer
import chromadb
from tqdm import tqdm
