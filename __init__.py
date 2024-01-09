from mycroft import MycroftSkill, intent_file_handler


class MuxlisaDateTime(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('time.date.muxlisa.intent')
    def handle_time_date_muxlisa(self, message):
        hour = ''
        minute = ''

        self.speak_dialog('time.date.muxlisa', data={
            'minute': minute,
            'hour': hour
        })


def create_skill():
    return MuxlisaDateTime()

