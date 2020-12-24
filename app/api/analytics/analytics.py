from fastapi import APIRouter

from app.data.repository import Repository


router = APIRouter()


@router.get('/analytics')
async def get_analytics():
    """
    Get data for analytics
    """
    histories = Repository.get_all_histories()

    illness_count = dict()
    status_count = dict()
    for history in histories:
    	status_count[history['status']] = status_count.get(history['status'], 0) + 1
    	illness_count[history['diagnosis']] = illness_count.get(history['diagnosis'], 0) + 1
    data = {
    	'illness_count': illness_count,
    	'status_count': status_count
    }

    return {'data': data, 'result': bool(histories)}
