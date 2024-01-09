from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.time import now_utc
import re
from tzlocal import get_localzone

class MuxlisaDateTime(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.display_tz = None

    @intent_file_handler('what.time.is.it.intent')
    def handle_time_date_muxlisa(self, message):
        utt = message.data.get('utterance', "")
        hour, minute = self.get_spoken_current_time(location=None)
        if not hour or not minute:
            return
        self.log.warning("nimalar bo'ldi")
        self.speak_dialog('time.current', data={
            'minute': minute,
            'hour': hour
        })

    def get_spoken_current_time(self, location=None,
                                dtUTC=None, force_ampm=False):
        # Get a formatted spoken time based on the user preferences
        dt = self.get_local_datetime(location, dtUTC)
        if not dt:
            return

        return dt.hour, dt.minute

    def get_local_datetime(self, location, dtUTC=None):
        if not dtUTC:
            dtUTC = now_utc()
        tz = get_localzone()
        if not tz:
            self.speak_dialog("time.tz.not.found", {"location": location})
            return None

        return dtUTC.astimezone(tz)

def create_skill():
    return MuxlisaDateTime()

