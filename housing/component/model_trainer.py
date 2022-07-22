import os,sys
from housing.logger import logging
from housing.exception import ExceptionHendler
from housing.constant import *
from housing.config.configuration import Configuration
from housing.component.data_ingestion import DataIngestion
from housing.component.data_validation import DataValidation
from housing.component.data_transformation import DataTransformation
from housing.util.util import read_yaml_file,load_data,load_numpy_array_data,load_preprocessing_object, save_preprocessing_object
from housing.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact, DataValidationArtifact, ModelTrainerArtifact
from housing.entity.model_factory import ModelFactory
from housing.entity.config_entity import ModelTrainerConfig
from housing.entity.model_factory import MetricInfoArtifact, ModelFactory,GridSearchedBestModel
from housing.entity.model_factory import evaluate_regression_model
from typing import List


class HousingEstimatorModel:
    def __init__(self, preprocessing_object, trained_model_object):
        """
        TrainedModel constructor
        preprocessing_object: preprocessing_object
        trained_model_object: trained_model_object
        """
        self.preprocessing_object = preprocessing_object
        self.trained_model_object = trained_model_object

    def predict(self, X):
        """
        function accepts raw inputs and then transformed raw input using preprocessing_object
        which gurantees that the inputs are in the same format as the training data
        At last it perform prediction on transformed features
        """
        transformed_feature = self.preprocessing_object.transform(X)
        return self.trained_model_object.predict(transformed_feature)

    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"

    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"


class ModelTraining:
    def __init__(self,model_training_config:ModelTrainerConfig,
                     data_transformation_artifact:DataTransformationArtifact
                 )->ModelTrainerArtifact:

        try:
            self.model_trainer_config = model_training_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def get_train_and_test_file(self):
        try:

            transformed_train_file_path = self.data_transformation_artifact.transformed_train_file_path
            transformed_test_file_paath = self.data_transformation_artifact.transformed_test_file_path

            train_file = load_numpy_array_data(file_path=transformed_train_file_path)

            test_file = load_numpy_array_data(file_path=transformed_test_file_paath)

            return train_file,test_file


        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def get_model_training_object(self):
        try:
            
            model_config_path = os.path.join(ROOT_DIR,CONFIG_DIR_NAME,MODEL_FILE_PATH)
            model_factory = ModelFactory(model_config_path=model_config_path)

            logging.info(f"model object created as : [{model_factory}]")

            return model_factory

        except Exception as e:
            raise ExceptionHendler(e,sys) from e


    def get_best_model_with_accuray(self):
        try:

            train_file,test_file = self.get_train_and_test_file()

            x_train,y_train,x_test,y_test = train_file[:,:-1],train_file[:,-1],test_file[:,:-1],test_file[:,-1]

            base_accuracy = self.model_trainer_config.base_accuracy

            model_object = self.get_model_training_object()

            best_model = model_object.get_best_model(X=x_train,y=y_train,base_accuracy=base_accuracy)

            logging.info(f"best model is :[{best_model}]")

            return best_model
            

        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def get_matric_info(self):
        try:

            logging.info("-----------get metric info log started--------------")

            train_file,test_file = self.get_train_and_test_file()

            x_train,y_train,x_test,y_test = train_file[:,:-1],train_file[:,-1],test_file[:,:-1],test_file[:,-1]

            base_accuracy = self.model_trainer_config.base_accuracy

            logging.info(f"base accuracy is ; [{base_accuracy}]")

            model_object = self.get_model_training_object()

            model_object.get_best_model(X=x_train,y=y_train,base_accuracy=base_accuracy)


            grid_searched_best_model_list:List[GridSearchedBestModel]=model_object.grid_searched_best_model_list

            logging.info(f"grid_searched_best_model_list is : [{grid_searched_best_model_list}]")

            model_list = [model.best_model for model in grid_searched_best_model_list ]

            logging.info(f"model list is : [{model_list}]")

            metric_info:MetricInfoArtifact = evaluate_regression_model(model_list=model_list,X_train=x_train,y_train=y_train,X_test=x_test,y_test=y_test,base_accuracy=base_accuracy)

            logging.info(f"metric_info is [{metric_info}]")

            return metric_info

        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def get_trained_model_file_path(self):
        try:
            
            metric_info = self.get_matric_info()

            logging.info(f"matric info is : [{metric_info}]")

            model_object = self.get_model_training_object()

            preprocessing_obj=  load_preprocessing_object(file_path=self.data_transformation_artifact.preprocessed_object_file_path)
            model_object = metric_info.model_object

            trained_model_file_path=self.model_trainer_config.trained_model_file_path

            housing_model = HousingEstimatorModel(preprocessing_object=preprocessing_obj,trained_model_object=model_object)
            logging.info(f"Saving model at path: {trained_model_file_path}")
            save_preprocessing_object(file_path=trained_model_file_path,obj=housing_model)

            logging.info(f"trained model file path is : [{trained_model_file_path}]")

            return trained_model_file_path

        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def initiate_model_training(self):
        try:

            logging.info("--------------model training initiated------------------------")

            trained_model_file_path = self.get_trained_model_file_path()

            metric_info = self.get_matric_info()


            model_training_artifact = ModelTrainerArtifact(is_trained=True,message="Model Trained successfully",
            trained_model_file_path=trained_model_file_path,
            train_rmse=metric_info.train_rmse,
            test_rmse=metric_info.test_rmse,
            train_accuracy=metric_info.train_accuracy,
            test_accuracy=metric_info.test_accuracy,
            model_accuracy=metric_info.model_accuracy
            )

            logging.info(f"model_training_artifact is : [{model_training_artifact}]")

            return model_training_artifact

        except Exception as e:
            raise ExceptionHendler(e,sys) from e