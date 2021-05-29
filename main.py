from subprocess import run, PIPE

import os
import argparse

SOLUTIONS_PATH = "solutions"
solved_problems = sorted(map(int, os.listdir(SOLUTIONS_PATH)))

parser = argparse.ArgumentParser(description='Project Euler')
parser.set_defaults(which='default')
subparsers = parser.add_subparsers()

execute_parser = subparsers.add_parser("run", help="Execute the solutions.")
execute_parser.add_argument("solutions", metavar="s", nargs="*", default=solved_problems,
                            type=int, help="the solution to run.")
execute_parser.set_defaults(which='execute')

list_parser = subparsers.add_parser("list", help="List available solutions.")
list_parser.set_defaults(which='list')

def execute_solution(n):
    """Executes solution for the problem n.

    Args:
        n: the number of the problem.
    """
    solution_path = os.path.join(SOLUTIONS_PATH, str(n))
    script_path = os.path.join(solution_path, "script.py")
    input_path = os.path.join(solution_path, "input.txt")

    result = run(["./execute.sh", script_path, input_path], stdout=PIPE, stderr=PIPE, text=True)
    print("Problem #{} => {}".format(n, result.stdout.strip("\n")))

if __name__ == "__main__":
    args = parser.parse_args()
    if args.which == "list" or args.which == "default":
        print("Currently solved problems:")
        print(solved_problems)
    elif args.which == "execute":
        problems = set(solved_problems)
        for n in args.solutions:
            if n in problems:
                execute_solution(n)