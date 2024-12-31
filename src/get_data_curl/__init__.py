from .model.curl import request
from .model.header import header
from .model.lop_hoc_phan import lop_hoc_phan
from .model.thoi_gian_lop_hoc_phan import thoi_gian_lop_hoc_phan
from .model.url_ds_lhp import url_ds_lhp 
from .model.url_tg_lhp import url_tg_lhp
from .main import main as get_data

__all__ = [ "get_data", "request", "header", "lop_hoc_phan", "thoi_gian_lop_hoc_phan", "url_ds_lhp", "url_tg_lhp"]