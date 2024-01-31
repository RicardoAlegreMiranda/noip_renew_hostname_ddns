# Internal
import noip.funcions as funcions
import noip.user
from noip.funcions_driver import Funcions_Driver
from noip.paths import Paths


class DateProcessingError(Exception):
    pass


class NoIP:

    def __init__(self, headless: bool = None):
        user_password_json = noip.user.load_json()
        self.user = user_password_json.get("user")
        self.password = user_password_json.get("password")
        self.ddns = user_password_json.get("ddns")
        self.functions_driver = Funcions_Driver(headless)  # Create the object

    def start(self):
        self.functions_driver.get_url(Paths.URL)  # Open the URL
        self.functions_driver.clic(Paths.BTN_LOGIN)  # clic in login
        self._login()

    def _login(self):
        self.functions_driver.write(Paths.TEXT_AREA_USERNAME, self.user)  # Introduce the user
        self.functions_driver.write(Paths.TEXT_AREA_PASSWORD, self.password)  # Introduce the password
        self.functions_driver.clic(Paths.BTN_SUBMIT)  # Clic in login button

        # Check if pass the login page
        if not self.functions_driver.find_element(Paths.DASHBOARD):
            if self.functions_driver.find_element(Paths.LOGIN_ERROR):  # Check if the error message is present
                raise DateProcessingError("user or password incorrect")
        else:
            self._renew_ddns()

    def _renew_ddns(self):

        xpath_ddns = "//a[contains(.,'" + self.ddns + "')]"  # Get the xpath of ddns

        self.functions_driver.clic(xpath_ddns)  # Clic in XPATH_DDNS
        self.functions_driver.clic(Paths.BTN_HOST_NAME)  # Close the modal
        self.functions_driver.clic(Paths.BTN_CONFIRM)  # confirm the name

        # Confirm that the update date is the same date as today
        label_date = self.functions_driver.read(Paths.LABEL_LAST_UPDATE)

        if funcions.compare_date(label_date):
            self.functions_driver.driver_close()  # Is OK, close the driver
        else:
            raise DateProcessingError(f"The date read in Last Update: {label_date} "
                                      f"is not the same date as today: {funcions.today_date()}")
