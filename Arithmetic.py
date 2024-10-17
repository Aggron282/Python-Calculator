import math;
class Arithmetic :
    def __init__(self):
        self.name = "arithmetic"
        self.choices = [
            {
            "name":"basic",
             "prompt":"Enter a basic equation",
             "exec":self.solve
            },
            {
                "name": "distance",
                "prompt": "Enter 4 numbers in this order: x1, x2, y1, y2",
                "exec": self.solve_distance
            },

        ]

    def solve(self,equation):
        eq = None
        try:
            eq = eval(equation)
        except:
            eq = "Invalid Equation"

        return eq

    def solve_distance(self,eq):

        coef = eq.split();
        new_c = [];
        if(len(coef) < 4):
            return None;
        for c in coef:
            try:
                new_c.append(float(c));
            except:
                return None;
        answer = math.sqrt((new_c[0] - new_c[1]) ** float(2) + (new_c[2]-new_c[3]) ** float(2));

        return answer;

    def show_choices(self):

        problem = input("Input any basic arithmetic statement!");
        answer = self.solve(problem);

        print("Your answer is: "+answer);

    def execute_choice(self,choice):

        for choice_ in self.choices:

            if choice_.get("name").strip().lower() == choice.strip().lower():
                prompt = input(choice_.get("prompt") + "\n")
                exec_ = choice_.get("exec")
                answer = exec_(prompt)

                print("The answer is: "+ str(answer))




