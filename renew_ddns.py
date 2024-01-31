from noip import no_ip as NP

headless_mode_active = False  # Change to True for headless mode (don´t show chrome)

renew = NP.NoIP(headless=headless_mode_active)
renew.start()
