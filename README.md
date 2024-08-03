# Contact:
- **Mail**: *lytranvinh.work@gmail.com*
- **Github**: *https://github.com/Youknow2509*

# Usage:
- Python, lib use in 'requirements.txt'
- Google api, google calendar, ...

# Description:
- Create a calendar create schedule in `UTC`.
- How to activate:
    - It read file `data.xlsx` in path `data/data.xlsx`
    - Data after creation same: [data.json](https://github.com/Youknow2509/Calendar_UTC/blob/main/data/data.json)
    - Use api google calendar create event

# How to use:
- [Enable google calendar api](https://support.google.com/googleapi/answer/6158841?hl=en) :
    - **Note:**
        - Choses `SCOPES` use in google console. (Ex: https://www.googleapis.com/auth/calendar, https://www.googleapis.com/auth/calendar.events)
        - Add **Authorized redirect URIs** in your project.(Ex: my red url in code: http://localhost:3300/oauth2callback)

- Install `requirements.txt`:
  ```python
        pip install -r requirements.txt
  ```
- Get Client Secrets in google console and save file `client_secrets.json` in path `src/gg_auth/`
- Create file 'credentials.json' in path `src/gg_auth`
- Oauth 2 get credentials
- -> ok !!! run 
```python
python src/main.py
```