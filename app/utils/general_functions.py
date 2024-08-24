from fastapi import HTTPException

def get_item_by_id(id, session, model):
    track = session.query(model).filter(model.id == id).first()
    if track is None:
        raise HTTPException(status_code=404, detail=f"{model.__name__} not found.")
    return track

def update_fields(instance, data):
    for key, value in data.items():
            setattr(instance, key, value)
    return