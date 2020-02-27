class TuringMachine:
    def __init__(self, states, array=[' ']*99000):
        self.states = states
        self.array = array

    def run_transitions(self, state, index):
    # states -> {'initial': [{'symbol':None, 'write':'X', 'direction':+1, 'return':'initial'}]}
        array_index = index
        stage_to_go = state
        array_length = len(self.array)
        while array_index <= array_length:
            try:
                actual_state = self.states[stage_to_go]
                for transition in actual_state:
                    if not transition['symbol']:
                        return
                    if self.array[array_index] == transition['symbol']:
                        to_write = transition['write']
                        if to_write:
                            self.array[array_index] = to_write
                        direction_to_go = transition['direction']
                        array_index += direction_to_go
                        stage_to_go = transition['return']
                        break
            except IndexError:
                return

    def print_array(self):
        print(self.array)


if __name__ == '__main__':
    machine1 = TuringMachine(states={'initial': [{'symbol': '|', 'write': None, 'direction': +1, 'return': 'initial'},
                      {'symbol': ' ', 'write': '|', 'direction': 0, 'return': 'end'}],
          'end': [{'symbol': None, 'write': None, 'direction': 0, 'return': None}]},
                             array=['|', '|', '|', '|']+[' ']*5000)
    machine1.run_transitions('initial', 0)
    machine1.print_array()

    machine2 = TuringMachine(states={'initial': [{'symbol': ' ', 'write': 'X', 'direction': 1, 'return': 'initial'}]})
    machine2.run_transitions('initial', 0)
    machine2.print_array()


















