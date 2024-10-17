import Arithmetic;
import SimpleShapes;
import ascii_custom

from ascii_custom import *;

arithmetic = Arithmetic.Arithmetic();
simple_shapes = SimpleShapes.SimpleShapes();

class ChoiceMenu:

    def __init__(self):
        self.choices = [];
        self.solvers = [arithmetic,simple_shapes];

        for solve in self.solvers:
            self.choices.append(solve.name);

    def initiate(self):
        print("---------------------------------------------------------------------------------- \n")
        option_str = ("Select from the following options (Must be correct spelling) \n");

        for choice in self.choices:
            option_str += " | " +choice;

        prompt = input(option_str + "\n");

        if(prompt):
           found_solver = self.find_solver(prompt);

           if(found_solver):
                print("-------------Choose Type of Equation to Solve--------- \n");
                print("Select Choice: \n");

                for choice_ in found_solver.choices:
                    print(choice_.get("name") + "\n");

                choice = input()
                chosen_choice = self.find_choice(choice, found_solver.choices);
                if chosen_choice == None or chosen_choice == False:
                    print("Invalid Input")
                    self.initiate();
                print("You have chosen the "+chosen_choice.get("name") + " " + found_solver.name + "\n");
                found_solver.execute_choice(chosen_choice.get("name"));
                self.initiate();
           else:

               print("Could not find solver");
               self.initiate();

        else:

            print("Invalid Input");
            self.initiate();

    def find_solver(self,prompt):

        for solver in self.solvers:

            if solver.name.lower().strip() == prompt.lower().strip():

                return solver;

        return None;

    def find_choice(self,choice,choices):

        for choice_ in choices:

            if choice_.get("name").lower().strip() == choice.lower().strip():

                return choice_

        return None


print(ascii_custom.app_name);
choice_menu = ChoiceMenu();
choice_menu.initiate();