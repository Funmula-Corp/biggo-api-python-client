"""The models of video product"""

from dataclasses import dataclass
from typing import Optional

from biggo_api.model._base import Base


@dataclass
class DraftProduct(Base):
    """This class is used for setting up or updating video product list"""
    nindex: str
    oid: str
    pass


@dataclass
class Product(Base):
    """This class represents a product in video"""
    _ALIASES = {
        'has_shop': 'hasShop',
        'has_store_page': 'hasStorePage',
        'is_ad': 'isAD',
        'is_multiple_product': 'isMultipleProduct',
        'is_not_found': 'isNotFound',
        'is_offline': 'isOffline',
        'original_image': 'origimage',
        'seller_credit': 'seller-credit',
        'type_': 'type',
        'user_name': 'username',
        'view_counter': 'viewcounter',
    }
    currency: str
    gallery_count: int
    gallery_images: list[str]
    has_shop: bool
    has_store_page: bool
    id: str
    image: str
    index: str
    is_ad: bool
    is_adult: bool
    is_not_found: bool
    is_offline: str
    more: bool
    online_notify: bool
    original_image: str
    original_price: float
    price_diff_real: float
    provide: str
    subscribe: bool
    title: str
    type_: str
    cata: Optional[list] = None
    count_result_product: Optional[int] = None
    count_result_store: Optional[int] = None
    discount: Optional[list] = None
    history_id: Optional[str] = None
    is_multiple_product: Optional[bool] = None
    location: Optional[str] = None
    m_max_price: Optional[str] = None
    m_text: Optional[str] = None
    original_symbol: Optional[str] = None
    price: Optional[float] = None
    price_range_max: Optional[int] = None
    price_range_min: Optional[int] = None
    product_nindex_price: Optional[list] = None
    promo_btn: Optional[str] = None
    promo_title: Optional[str] = None
    promo_url: Optional[str] = None
    purl: Optional[str] = None
    seller_credit: Optional[int] = None
    symbol: Optional[str] = None
    target_app: Optional[str] = None
    uid: Optional[str] = None
    url: Optional[str] = None
    url_dynamic: Optional[str] = None
    url_scheme: Optional[str] = None
    user_name: Optional[str] = None
    view_counter: Optional[int] = None
    pass
