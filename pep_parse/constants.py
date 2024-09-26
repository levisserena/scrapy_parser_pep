from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
NAME_FOLDER_SAVING_FILES = 'results'

NAME_FILE_PEP = 'pep'
FORMAT_FILE = 'csv'

FIELDS = ['number', 'name', 'status']
NAME_FILE_SUM_STATUS = 'status_summary'
TOTAL_SUM_STATUS = 'Total'
FIELD_STATUS_SUM_STATUS = 'Статус'
FIELD_QUANTITY_SUM_STATUS = 'Количество'
FORMAT_DATETIME = '%Y-%m-%d_%H-%M-%S'

PROJECT_NAME = 'pep_parse'
MODULE_NAME_SPIDERS = f'{PROJECT_NAME}.spiders'
CLASS_NAME_PIPELINES = f'{PROJECT_NAME}.pipelines.PepParsePipeline'
