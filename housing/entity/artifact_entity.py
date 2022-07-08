from collections import namedtuple

## Data Ingestion Artifact Configuration:-

DataIngestionArtifact = namedtuple("DataIngestionArtifact",["train_file_path","test_file_path","is_ingested",
                                                            "message"])


