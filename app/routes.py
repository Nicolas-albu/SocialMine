from scraper.Scraper import VSCOScraper
from fastapi import APIRouter

router = APIRouter()

def username_vsco_to_url(username: str) -> str:
    return f"https://vsco.co/{username}/gallery"

@router.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}

@router.get("/user_vsco/{username_vsco}")
async def get_images_vsco(username_vsco: str) -> dict[str, str]:
    url = username_vsco_to_url(username_vsco)
    return {
            "username": username_vsco, 
            "links_of_images": VSCOScraper(url).get_image_srcs()
        }