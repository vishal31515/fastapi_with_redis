from app.api.v1 import crud
from app.logs.log_handler import LibLogger
from fastapi import APIRouter, HTTPException, Response, status


router = APIRouter()
log = LibLogger()


@router.get("/get_data")
def get_data(response: Response):
    try:
        response_data = crud.final_data()
        if not response_data:
            raise HTTPException(status_code=404, detail="Data not found")
        response.status_code = status.HTTP_200_OK
        return response_data
    except Exception as error:
        log.error(error)
        return {"message": str(error)}
