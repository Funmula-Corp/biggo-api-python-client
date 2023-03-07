"""This module defines data classes of video product"""

from typing import Optional, Union

from pydantic import BaseModel, Field


class BigGoVideoProductBase(BaseModel):
    """This class represents a base product in video."""
    image: str
    price: float
    symbol: str
    title: str
    pass


class BigGoVideoProduct(BigGoVideoProductBase):
    """This class represents a detailed product in video."""
    currency: str
    discount: list[str]
    gallery_count: int
    gallery_images: list[str]
    has_shop: bool = Field(alias='hasShop')
    has_store_page: bool = Field(alias='hasStorePage')
    history_id: str
    id: str
    index: str
    is_ad: bool = Field(alias='isAD')
    is_adult: bool
    is_multiple_product: bool = Field(alias='isMultipleProduct')
    is_not_found: bool = Field(alias='isNotFound')
    is_offline: bool = Field(alias='isOffline')
    more: bool
    online_notify: bool
    original_image: str = Field(alias='origimage')
    original_price: float
    original_symbol: str
    price_diff_real: float
    provide: str
    purl: str
    subscribe: bool
    type_: str = Field(alias='type')
    url: str
    location: Optional[str] = None
    m_max_price: Optional[str] = None
    m_text: Optional[str] = None
    seller_credit: Optional[int] = Field(None, alias='seller-credit')
    uid: Optional[str] = None
    username: Optional[str] = None
    pass


VideoProducts = Union[list[BigGoVideoProduct], list[BigGoVideoProductBase]]
