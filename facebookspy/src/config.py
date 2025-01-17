import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Configuration class for the application.
    """

    # Scrolling
    SCROLL_PAUSE_TIME = 1
    MAX_CONSECUTIVE_SCROLLS = 1

    # Facebook login
    FACEBOOK_EMAIL = os.getenv("FACEBOOK_EMAIL")
    FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")
    COOKIES_FILE_PATH = "cookies.json"

    # logs
    LOG_FILE_PATH = "logs.log"

    # Json
    JSON_FILE_PATH = "scraped_data/"

    # images
    IMAGE_PATH = "images/"
    DOCKER_IMAGE_PATH = "/app/facebookspy"

    # videos
    VIDEO_PATH = "videos/"
    DOCKER_VIDEO_PATH = "/app/facebookspy"

    # Facebook paths
    FRIEND_LIST_URL = "friends"
    WORK_AND_EDUCATION_URL = "about_work_and_education"
    PLACES_URL = "about_places"
    FAMILY_URL = "about_family_and_relationships"
    CONTACT_URL = "about_contact_and_basic_info"
