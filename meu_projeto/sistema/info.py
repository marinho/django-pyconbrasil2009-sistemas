from djangoplus.model_info import ModelInfo

from models import Empresa

class InfoEmpresa(ModelInfo):
    class Meta:
        model = Empresa

