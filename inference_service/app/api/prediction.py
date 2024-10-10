from flask import abort, Blueprint, request
from pydantic import ValidationError

from schema.apartment import Apartment
from services import model_inference_service

bp=Blueprint('prediction', __name__, url_prefix='/pred')


@bp.get('/')
def get_prediction():

    # get and check input parameters
    try:
        apartment_features=Apartment(**request.args)
    except ValidationError:
        abort(code=400,description='Bad Input Parameters')

    # # load an existing model
    # model_inference_service=ModelInferenceService()
    # model_inference_service.load_model()

    # feed input parameters to the loaded ml model to get a prediction
    prediction = model_inference_service.predict(
        list(apartment_features.model_dump().values()),)
    # return prediction value
    return {'prediction': prediction}

@bp.post('/')
def get_prediction_post():

    # get and check input parameters
    apartment_features=Apartment(**request.json)

    # load an existing model
    # model_inference_service=ModelInferenceService()
    # model_inference_service.load_model()

    # feed input parameters to the loaded ml model to get a prediction
    prediction = model_inference_service.predict(
        list(apartment_features.model_dump().values()),)
    # return prediction value
    return {'prediction': prediction}
