from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(25, 25, 10, 8, 50, 50, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    maze._solve_r(0,0)

    win.wait_for_close()

if __name__ == '__main__':
    main()