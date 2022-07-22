from collections import namedtuple

## Data Ingestion Artifact Configuration:-

DataIngestionArtifact = namedtuple("DataIngestionArtifact",["train_file_path","test_file_path","is_ingested",
                                                            "message"])


## Data Validation Artifact Configuration:-


DataValidationArtifact = namedtuple("DataValidationArtifact",["schema_file_path","report_file_path",
                                     "report_page_file_path","is_validated","message"])

## Data Transformation Artifact Configuration:-

DataTransformationArtifact = namedtuple("DataTransformationArtifact",["is_transformed",
"transformed_train_file_path","transformed_test_file_path","message","preprocessed_object_file_path"])

## Model Trainer Artifact Configuration :-

ModelTrainerArtifact = namedtuple("ModelTrainerArtifact",["is_trained", "message", 
"trained_model_file_path","train_rmse", "test_rmse", "train_accuracy", "test_accuracy",
                "model_accuracy"])

