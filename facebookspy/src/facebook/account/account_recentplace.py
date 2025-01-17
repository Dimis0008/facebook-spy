from typing import List, Dict

from rich import print as rprint
from selenium.webdriver.common.by import By

from ..facebook_base import BaseFacebookScraper
from ..scroll import scroll_page
from ...logs import Logs
from ...repository import person_repository, recent_place_repository
from ...utils import output, save_to_json

logs = Logs()


class AccountRecentPlaces(BaseFacebookScraper):
    """
    Scrape user's pictures
    """

    def __init__(self, user_id: str) -> None:
        super().__init__(
            user_id, base_url=f"https://www.facebook.com/{user_id}/places_recent"
        )
        self.success = False

    def _load_cookies_and_refresh_driver(self) -> None:
        """Load cookies and refresh driver"""
        self._load_cookies()
        self._driver.refresh()

    @property
    def is_pipeline_successful(self) -> bool:
        return self.success

    def extract_recent_places(self) -> List[Dict[str, str]]:
        """
        Return data about recent places
        """
        extracted_image_urls = []
        try:
            data = {}
            div_element = self._driver.find_element(
                By.CSS_SELECTOR,
                "div.xyamay9.x1pi30zi.x1l90r2v.x1swvt13",
            )
            span_elements = div_element.find_elements(
                By.CSS_SELECTOR,
                "span.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x676frb.x1lkfr7t.x1lbecb7.x1s688f.xzsf02u",
            )

            div_inside_elements = div_element.find_elements(
                By.CSS_SELECTOR, "div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1vvkbs"
            )

            for i in range(len(span_elements)):
                data = {}
                data["localization"] = span_elements[i].text
                data["date"] = div_inside_elements[i].text

                extracted_image_urls.append(data)

            extracted_image_urls.append(data)
        except Exception as e:
            logs.log_error(f"Error extracting image URLs: {e}")

        return extracted_image_urls

    def pipeline(self) -> None:
        """
        Pipeline to run the scraper
        """
        try:
            rprint("[bold]Step 1 of 3 - Load cookies[/bold]")
            self._load_cookies_and_refresh_driver()

            rprint("[bold]Step 2 of 3 - Scrolling page[/bold]")
            scroll_page(self._driver)

            rprint("[bold]Step 3 of 3 - Extracting recent places[/bold]")
            recent_places = self.extract_recent_places()

            if not any(recent_places):
                output.print_no_data_info()
                self._driver.quit()
                self.success = False
            else:
                output.print_data_from_list_of_dict(recent_places)

                rprint(
                    "[bold red]Don't close the app![/bold red] Saving scraped data to database, it can take a while!"
                )

                save_to_json.SaveJSON(
                    self._user_id, recent_places,
                ).save()

                if not person_repository.person_exists(self._user_id):
                    person_repository.create_person(self._user_id)

                person_id = person_repository.get_person(self._user_id).id

                for place in recent_places:
                    if not recent_place_repository.recent_places_exists(
                        place["localization"], place["date"], person_id
                    ):
                        recent_place_repository.create_recent_places(
                            place["localization"], place["date"], person_id
                        )

                self._driver.quit()
                self.success = True

        except Exception as e:
            logs.log_error(f"An error occurred: {e}")
            rprint(f"An error occurred {e}")
