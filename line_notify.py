# Klipper plugin line notify

# import sys
# sys.path.append("/usr/lib/python3/dist-packages")
import urllib.request
import urllib.parse
import json

class LineNotify:
    def __init__(self, config) -> None:
        self.name = config.get_name().split()[-1]
        self.printer = config.get_printer()
        self.gcode = self.printer.lookup_object('gcode')

        # Get configuration
        self.access_token = config.get('access_token')
        self.timeout = config.get('timeout', 10)

        # Register commands
        self.gcode.register_command(
            "PUSH_LINE_NOTIFY", 
            self.PUSH_LINE_NOTIFY, 
            desc=self.CMD_PUSH_LINE_NOTIFY_HELP)

    CMD_PUSH_LINE_NOTIFY_HELP = "Sending message to Line Notify"
    def PUSH_LINE_NOTIFY(self, params):
        message = params.get('MSG', '')
        silent = params.get('SILENT', 'False').lower() == 'true'

        # Function usage
        if message == '':
            self.gcode.respond_info("""
              Line Notify
              USAGE: PUSH_LINE_NOTIFY MSG="message" [SILENT=False]
              Parameters:
                MSG: string (required) - The message to send
                SILENT: boolean (optional) - If set to True, don't send notification when send message
              Examples:
                PUSH_LINE_NOTIFY MSG="Print completed"
                PUSH_LINE_NOTIFY MSG="Print progress: 50%"
                PUSH_LINE_NOTIFY MSG="Print started" SILENT=True
            """)
            return

        url = 'https://notify-api.line.me/api/notify'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer ' + self.access_token
        }
        data = urllib.parse.urlencode({'message': message, 'notificationDisabled': silent}).encode('utf-8')

        try:
            req = urllib.request.Request(url, data=data, headers=headers, method='POST')
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                if response.status == 200:
                    response_data = json.loads(response.read().decode('utf-8'))
                    message = response_data.get('message')
                    self.gcode.respond_info(f"Message from LINE Notify: {message}")
                else:
                    raise self.gcode.error(f"Message from LINE Notify: HTTP error {response.status}")
        except urllib.error.URLError as e:
            raise self.gcode.error(f"Message from LINE Notify: Connection error - {str(e)}")
        except Exception as e:
            raise self.gcode.error(f"Message from LINE Notify: Unexpected error - {str(e)}")

def load_config(config):
    return LineNotify(config)