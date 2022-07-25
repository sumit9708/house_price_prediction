from collections import namedtuple

## Data Ingestion  Configuration:-

DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_url","raw_data_dir",
                                "tgz_download_dir","ingested_dir","ingested_train_dir","ingested_test_dir"])

## Data Validation  Configuration:-
DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path","report_file_path","report_page_file_path"])

## Data Transformation  Configuration :-
DataTransformationConfig = namedtuple("DataTransformationConfig",["add_bedroom_per_room",
         "transformed_train_dir","transformed_test_dir","preprocessed_object_file_name"])

## Model Trainer Configuration:-

ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])

## Model Evaluation Configuration :-
ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])

## Model Pusher Configuration :-
ModelPusherConfig = namedtuple("ModelPusherConfig",["model_export_dir"])

## Training Pipeline Configuration:-
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",["artifact_dir"])