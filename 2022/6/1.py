from itertools import product
import os

class CNF:
    def __init__(self):
        self.clauses = []
        self.number_to_var_name = {}
        self.var_name_to_number = {}
    
    def add_clause(self, clause):
        for literal in clause:
            var_name = literal.strip('-')
            if var_name not in self.var_name_to_number:
                var_number = len(self.var_name_to_number) + 1
                self.var_name_to_number[var_name] = var_number
                self.number_to_var_name[var_number] = var_name
        self.clauses.append(clause)

    def dimacs(self):
        result = f'p cnf {len(self.number_to_var_name)} {len(self.clauses)}\n'
        for clause in self.clauses:
            for literal in clause:
                var_name = literal.strip('-')
                if literal[0] == '-':
                    result += '-'
                result += f'{self.var_name_to_number[var_name]} '
            result += '0\n'
        return result

def minisat_solve(problem_name, problem_dimacs, number_to_var):
    with open(f'{problem_name}.cnf', 'w') as handle:
        handle.write(problem_dimacs)
    os.system(f'minisat {problem_name}.cnf {problem_name}_result.cnf')

    with open(f'{problem_name}_result.cnf', 'r') as result_file:
        lines = result_file.readlines()

    if lines[0].startswith('SAT'):
        print('SAT')
        var_values = {}
        for var in lines[1].split(' ')[:-1]:
            var_number = int(var.strip('-'))
            var_name = number_to_var[var_number]
            var_values[var_name] = 0 if var.startswith('-') else 1
        true_vars = list(filter(lambda v: v[1] == 1, var_values.items()))
        true_vars.sort()
        for var in true_vars:
            print(var)
    else:
        print('UNSAT')

def n_dama(n):
    cnf = CNF()
    for j in range(n):
        clause = [f'p{j}{i}' for i in range(n)]
        cnf.add_clause(clause)

    # Uslov da mora bar 1 u svakoj vrsti
    for k in range(n):
        for i in range(n-1):
            for j in range(i+1,n):
                cnf.add_clause([f'-p{k}{i}', f'-p{k}{j}'])


    # Uslov da mora bar 1 u svakoj koloni
    for k in range(n):
        for i in range(n-1):
            for j in range(i+1,n):
                cnf.add_clause([f'-p{k}{i}', f'-p{k}{j}'])



    # Uslov da se ne napadaju na dijagonalama
    for i,j,k,l in product(range(n), repeat = 4):
        if k > i and abs(k-i) == abs(l-j):
            cnf.add_clause([f'-p{i}{j}', f'-p{k}{l}'])
    
    minisat_solve(f'{n}_queens', cnf.dimacs(), cnf.number_to_var_name)

if __name__ == '__main__':
    n_dama(4)