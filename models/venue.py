from pydantic import BaseModel


class Venue(BaseModel):
    """
    Represents the data structure of a Venue.
    """

    name: str
    price: str
    discount: str
    rating: str
    category: str
    stock_availability: str
    description: str

