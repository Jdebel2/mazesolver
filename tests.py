import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_shift_start_position(self):
        num_cols = 5
        num_rows = 4
        m1 = Maze(50, 50, num_rows, num_cols, 15, 15)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(
            m1._cells[0][0]._x1,
            50
        )
        self.assertEqual(
            m1._cells[0][1]._x1,
            65
        )
    
    def test_wall_breaks(self):
        num_cols = 5
        num_rows = 4
        m1 = Maze(50, 50, num_rows, num_cols, 15, 15)
        m1._break_entrance_and_exit()
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False
        )
        self.assertEqual(
            m1._cells[num_cols-1][num_rows-1].has_right_wall,
            False
        )
    
    def test_reset_wall_breaks(self):
        num_cols = 5
        num_rows = 4
        m1 = Maze(50, 50, num_rows, num_cols, 15, 15)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0,0)
        m1._reset_cells_visited()
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        has_all_walls = m1._cells[1][1].has_left_wall and m1._cells[1][1].has_right_wall and m1._cells[1][1].has_top_wall and m1._cells[1][1].has_bottom_wall
        self.assertEqual(
            has_all_walls,
            False
        )
        self.assertEqual(
            m1._cells[1][1].visited,
            False
        )
        

if __name__ == '__main__':
    unittest.main()