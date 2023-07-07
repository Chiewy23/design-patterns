from abc import abstractmethod


class MeetingState:
    @abstractmethod
    def is_meeting_online(self):
        pass


class StateOffline(MeetingState):
    def is_meeting_online(self):
        return False


class StateOnline(MeetingState):
    def is_meeting_online(self):
        return True


class StateContext:
    def __init__(self):
        # default state is offline
        self.current_state = StateOffline()

    def set_current_state(self, state):
        self.current_state = state

    def is_meeting_online(self):
        self.current_state.is_meeting_online()
