from mycroft import MycroftSkill, intent_file_handler


class LocationFinder(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('finder.location.intent')
    def handle_finder_location(self, message):
        places = message.data.get('places')
        place = ''

        self.speak_dialog('finder.location', data={
            'place': place,
            'places': places
        })


def create_skill():
    return LocationFinder()

