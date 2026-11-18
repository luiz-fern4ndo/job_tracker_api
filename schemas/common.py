from pydantic import BaseModel, ConfigDict


class ApplicationSummary(BaseModel):
    id: int
    company: str
    job_title: str
    model_config = ConfigDict(from_attributes=True)
