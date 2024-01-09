from mycroft import MycroftSkill, intent_file_handler
import re

class MuxlisaDateTime(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('what.time.is.it.intent')
    def handle_time_date_muxlisa(self, message):
        utt = message.data.get('utterance', "")
        location = self._extract_location(utt)
        hour, minute = self.get_spoken_current_time(location)
        if not hour or not minute:
            return

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

    def _extract_location(self, utt):
        # if "Location" in message.data:
        #     return message.data["Location"]
        rx_file = self.find_resource('location.rx', 'regex')
        if rx_file:
            with open(rx_file) as f:
                for pat in f.read().splitlines():
                    pat = pat.strip()
                    if pat and pat[0] == "#":
                        continue
                    res = re.search(pat, utt)
                    if res:
                        try:
                            return res.group("Location")
                        except IndexError:
                            pass
        return None

def create_skill():
    return MuxlisaDateTime()

