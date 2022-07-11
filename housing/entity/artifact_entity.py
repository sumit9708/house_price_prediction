from collections import namedtuple

## Data Ingestion Artifact Configuration:-

DataIngestionArtifact = namedtuple("DataIngestionArtifact",["train_file_path","test_file_path","is_ingested",
                                                            "message"])


## Data Validation Artifact Configuration:-


DataValidationArtifact = namedtuple("DataValidationArtifact",["schema_file_path","report_file_path",
                                     "report_page_file_path","is_validated","message"])