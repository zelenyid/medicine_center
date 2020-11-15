import json
import shutil
import uuid
import os

from fastapi import APIRouter, File, UploadFile

from app.validators.schemes.user_schemes import DiseaseHistoryScheme
from app.disease_storage.upload_file import FileUploader

router = APIRouter()