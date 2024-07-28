LANGUAGE_RU = "ru"
LANGUAGE_EN = "en"
LANGUAGES = [LANGUAGE_RU, LANGUAGE_EN]

THEME_DARK = "dark"
THEME_LIGHT = "light"
THEME_DEFAULT = "default"
THEMES = [THEME_LIGHT, THEME_DARK, THEME_DEFAULT]

INVALID_THEME = "Invalid theme"
INVALID_LANGUAGE = "Invalid language"


class DatabasePassedInvalidTheme(Exception):
    print(f"Invalid theme passed to database. Theme parameter must be in {THEMES}")
    pass


class DatabasePassedInvalidLanguage(Exception):
    print(f"Invalid language passed to database. Language parameter must be in {LANGUAGES}")
    pass


class DatabaseConfigUserNotExists(Exception):
    print("User not exists in database db.py user_config table")
