import time
import random
from graphics import Cell


class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self._cells = []
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        if seed:
            self.__seed = random.seed(seed)
        else:
            self.__seed = random.seed()
        self._create_cells()
    

    def _create_cells(self):
        for col in range(self.__num_cols):
            n_cells = []
            for row in range(self.__num_rows):
                top_left_x = self.__x1 + (row * self.__cell_size_x)
                top_left_y = self.__y1 + (col * self.__cell_size_y)
                bottom_right_x = top_left_x + self.__cell_size_x
                bottom_right_y = top_left_y + self.__cell_size_y
                n_cell = Cell(top_left_x, top_left_y, bottom_right_x, bottom_right_y, self.__win)
                n_cells.append(n_cell)
            self._cells.append(n_cells)

        if self.__win:
            for i in range(self.__num_cols):
                for j in range(self.__num_rows):
                    self._draw_cell(self._cells[i][j])
    

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[self.__num_cols-1][self.__num_rows-1].has_right_wall = False

        if self.__win:
            self._draw_cell(self._cells[0][0])
            self._draw_cell(self._cells[self.__num_cols-1][self.__num_rows-1])


    def _break_walls_r(self, row, col):
        self._cells[col][row].visited = True
        while True:
            to_visit = []
            
            locations = [(row-1, col, "left"),(row+1, col, "right"),(row, col-1, "up"),(row, col+1, "down")]
            for l in locations:
                if l[0] >= 0 and l[0] < self.__num_rows and l[1] >= 0 and l[1] < self.__num_cols:
                    if not self._cells[l[1]][l[0]].visited:
                        to_visit.append(l)
            
            if not to_visit:
                return

            random_dir = random.randint(0, len(to_visit)-1)
            random_visited = self._cells[to_visit[random_dir][1]][to_visit[random_dir][0]]
            match (to_visit[random_dir][2]):
                case "left":
                    self._cells[col][row].has_left_wall = False
                    random_visited.has_right_wall = False
                case "right":
                    self._cells[col][row].has_right_wall = False
                    random_visited.has_left_wall = False
                case "up":
                    self._cells[col][row].has_top_wall = False
                    random_visited.has_bottom_wall = False
                case "down":
                    self._cells[col][row].has_bottom_wall = False
                    random_visited.has_top_wall = False

            if self.__win:
                self._draw_cell(self._cells[col][row])
                self._draw_cell(random_visited)
            self._break_walls_r(to_visit[random_dir][0], to_visit[random_dir][1])


    def _reset_cells_visited(self):
        for i in self._cells:
            for j in i:
                j.visited = False


    def _solve_r(self, row, col):
        self._animate()
        self._cells[col][row].visited = True
        if row == self.__num_rows-1 and col == self.__num_cols-1:
            return True
        
        to_visit = []
        locations = [(row-1, col, 'left'),(row+1, col, 'right'),(row, col-1, 'up'),(row, col+1, 'down')]
        for l in locations:
            if l[0] >= 0 and l[0] < self.__num_rows and l[1] >= 0 and l[1] < self.__num_cols:
                can_move_in_direction = False
                match l[2]:
                    case 'left':
                        can_move_in_direction = not self._cells[col][row].has_left_wall and not self._cells[l[1]][l[0]].has_right_wall
                    case 'right':
                        can_move_in_direction = not self._cells[col][row].has_right_wall and not self._cells[l[1]][l[0]].has_left_wall
                    case 'up':
                        can_move_in_direction = not self._cells[col][row].has_top_wall and not self._cells[l[1]][l[0]].has_bottom_wall
                    case 'down':
                        can_move_in_direction = not self._cells[col][row].has_bottom_wall and not self._cells[l[1]][l[0]].has_top_wall
                
                if not self._cells[l[1]][l[0]].visited and can_move_in_direction:
                    to_visit.append(l)

        for l in to_visit:
            cell = self._cells[l[1]][l[0]]
            if self.__win:
                self._cells[col][row].draw_move(cell)
            result = self._solve_r(l[0],l[1])
            if result:
                return True
            if self.__win:
                self._cells[col][row].draw_move(cell, True)
        return False


    def _draw_cell(self, cell_ref):
        cell_ref.draw("black")
        self._animate()


    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)
        