import calendar_service
import config_parser
import media_downloader


if __name__ == "__main__":
    calendar_service.get_home_controller_events()
    config_parser.read_config()