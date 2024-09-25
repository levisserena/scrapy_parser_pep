import csv
from collections import defaultdict
from datetime import datetime

from .constants import (BASE_DIR, FIELD_QUANTITY_SUM_STATUS,
                        FIELD_STATUS_SUM_STATUS, FORMAT_DATETIME,
                        NAME_FILE_SUM_STATUS, NAME_FOLDER_SAVING_FILES,
                        TOTAL_SUM_STATUS)


class PepParsePipeline:
    def open_spider(self, spider):
        self.counts_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.counts_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        FOLDER_SAVING_FILES = BASE_DIR / NAME_FOLDER_SAVING_FILES
        FOLDER_SAVING_FILES.mkdir(exist_ok=True)
        with open(
            FOLDER_SAVING_FILES / '{name}_{time}.csv'.format(
                name=NAME_FILE_SUM_STATUS,
                time=datetime.now().strftime(FORMAT_DATETIME),
            ),
            'w', newline='', encoding='utf-8'
        ) as csv_file:
            writer = csv.writer(
                csv_file, dialect=csv.unix_dialect, quoting=csv.QUOTE_MINIMAL
            )
            writer.writerows([
                (FIELD_STATUS_SUM_STATUS, FIELD_QUANTITY_SUM_STATUS),
                *self.counts_statuses.items(),
                (TOTAL_SUM_STATUS, sum(self.counts_statuses.values())),
            ])
