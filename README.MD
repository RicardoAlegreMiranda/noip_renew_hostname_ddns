## No IP renew ddns
This package is used to automate ddns renewal with the NOIP provider using: python, selenium and chromedriver

## Install
- Install Python https://phoenixnap.com/kb/how-to-install-python-3-windows
- Install selenium (pip install selenium)
- Install webdriver_manager (pip install webdriver_manager)
- edit the Json "config.json", 

![300929613-ae2ce70a-d18b-4a3d-b16a-8e0641c2297b](https://github.com/RicardoAlegreMiranda/noip_renew_hostname_ddns/assets/40073353/55d0169a-0676-4ecd-aa04-f24239d13244)


## Use
- run the file: renew_ddns.py in python console

or 

```python
from noip import no_ip as NP

headless_mode_active = False  # Change to True for headless mode (don´t show chrome)

renew = NP.NoIP(headless=headless_mode_active)
renew.start()


```

Example of use (console):

![300929727-724a3cc4-6071-48f0-b396-db71720122e7](https://github.com/RicardoAlegreMiranda/noip_renew_hostname_ddns/assets/40073353/621afc5c-076a-467b-ab9f-bc3569469823)


## Disclaimer
> __DISCLAIMER:__ This library is not affiliated, endorsed, or sponsored by www.noip.com or any of its affiliates.  
> All trademarks related to www.noip.com and its affiliates are owned by the relevant companies.  
> The author(s) of this library assume no responsibility for any consequences resulting from the use of this library.  
> The author(s) of this library also assume no liability for any damages, losses, or expenses that may arise from the use of this library.  
> Any use of this library is entirely at the user's own risk.  
> It is solely the user's responsibility to ensure compliance with www.noip.com terms of use and any applicable laws 
> and regulations.  

