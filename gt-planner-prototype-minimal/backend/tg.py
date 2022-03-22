from fastapi.responses import JSONResponse

from data import default_curriculums
print(JSONResponse(default_curriculums['ME']))
