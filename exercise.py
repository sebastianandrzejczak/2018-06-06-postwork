'''
Poniżej znajduje się implementacja CLI (command line interface) do modułu
turtle, czyli Pythonowego odpowiednika LOGO. Wykorzystano tutaj wzorzec Template
Method (metoda szablonowa).
W pierwszym, obowiązkowym zadaniu, należy dodać wsparcie dla makr, tak aby można
było nagrać ciąg komend, a następnie odtworzyć ten sam ciąg przy pomocy
komendy "playback". W tym celu, należy dodać następujące komendy: 
- record -- rozpoczyna nagrywanie makra
- stop -- kończy nagrywanie makra
- playback -- wykonuje makro, tzn. wszystkie komendy po komendzie "record", aż
  do komendy "stop". 
Podpowiedź: Użyj wzorca Command (polecenie).
W drugim, nieobowiązkowym zadaniu, zastanów się, jak można zastosować wzorzec
Composite (kompozyt) do tych makr i spróbuj zastosować go.
Rozwiązania wysyłamy tak samo, jak prework, tylko że w jednym Pull Requeście.
'''

import cmd, sys
import turtle

class TurtleCommand(object):
    def __init__(self, arg):
        self.arg = arg

    def execute(self):
        pass

class MoveForwardCommand(TurtleCommand):
    def execute(self):
        turtle.forward(int(self.arg))       

class MoveBackwardCommand(TurtleCommand):
    def execute(self):
        turtle.backward(int(self.arg))
        
class TurnRightCommand(TurtleCommand):
    def execute(self):
        turtle.right(int(self.arg))

class TurnLeftCommand(TurtleCommand):
    def execute(self):
        turtle.left(int(self.arg))         

class HomeCommand(TurtleCommand):
    def execute(self):
        turtle.home()

class DrawCircleCommand(TurtleCommand):
    def execute(self):
        turtle.circle(int(self.arg))  

class PositionCommand(TurtleCommand):
    def execute(self):
        print('Current position is %d %d\n' % turtle.position())

class HeadingCommand(TurtleCommand):
    def execute(self):
        print('Current heading is %d\n' % (turtle.heading(),))

class ResetCommand(TurtleCommand):
    def execute(self):
        turtle.reset()

class ByeCommand(TurtleCommand):
    def execute(self):
        print('Thank you for using Turtle')
        turtle.bye()        

class MacroCommand(TurtleCommand):
    def execute(self):
        for command in self.arg:
            command.execute()


class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '
    recording = False

    # ----- basic turtle commands -----
    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        self._execute(MoveForwardCommand(arg))

    def do_backward(self, arg):
        #additional command
        'Move the turtle backward by the specified distance:  BACKWARD 10'
        self._execute(MoveBackwardCommand(arg))

    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        self._execute(TurnRightCommand(arg))

    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        self._execute(TurnLeftCommand(arg))

    def do_home(self, arg):
        'Return turtle to the home position:  HOME'
        self._execute(HomeCommand(arg))

    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        self._execute(DrawCircleCommand(arg))

    def do_position(self, arg):
        'Print the current turtle position:  POSITION'
        self._execute(PositionCommand(arg))

    def do_heading(self, arg):
        'Print the current turtle heading in degrees:  HEADING'
        self._execute(HeadingCommand(arg))

    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        self._execute(ResetCommand(arg))

    def do_bye(self, arg):
        'Close the turtle window, and exit:  BYE'
        self._execute(ByeCommand(arg))
        return True

    def do_record(self, arg):
        'Start commands recording: RECORD'
        self.recording = True
        self._commands = []

    def do_stop(self, arg):
        'STOP commands recording: STOP'
        self.recording = False
        self._macro = MacroCommand(self._commands)

    def do_playback(self, arg):
        'Execute recorded commands: PLAYBACK'
        self._execute(self._macro)

    def _execute(self, command):
        if (self.recording == True):
            self._commands.append(command)
        else:
            command.execute()

if __name__ == '__main__':
    TurtleShell().cmdloop()
