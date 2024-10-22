from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, {"bg": "white"}, height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
    
    def close(self):
        self.__running = False


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, x1, y1, x2, y2):
        self.start = Point(x1, y1)
        self.end = Point(x2, y2)
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )


class Cell():
    def __init__(self, x1, y1, x2, y2, window, visited=False):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = window
        self.visited = visited
    
    
    def __repr__(self):
        return f"Cell({self._x1},{self._y1},{self._x2},{self._y2})"
    

    def draw(self, fill_color):
        left_line = Line(self._x1, self._y1, self._x1, self._y2)
        if self.has_left_wall:
            self._win.draw_line(left_line, fill_color)
        else:
            self._win.draw_line(left_line, "white")

        right_line = Line(self._x2, self._y1, self._x2, self._y2)
        if self.has_right_wall:
            self._win.draw_line(right_line, fill_color)
        else:
            self._win.draw_line(right_line, "white")

        top_line = Line(self._x1, self._y1, self._x2, self._y1)
        if self.has_top_wall:
            self._win.draw_line(top_line, fill_color)
        else:
            self._win.draw_line(top_line, "white")
        
        bottom_line = Line(self._x1, self._y2, self._x2, self._y2)
        if self.has_bottom_wall:
            self._win.draw_line(bottom_line, fill_color)
        else:
            self._win.draw_line(bottom_line, "white")
    

    def draw_move(self, to_cell, undo=False):
        fill_color = ''
        if not undo:
            fill_color = "red"
        else:
            fill_color = "gray"
        
        self_center_x = (self._x1 + self._x2) // 2
        self_center_y = (self._y1 + self._y2) // 2
        other_center_x = (to_cell._x1 + to_cell._x2) // 2
        other_center_y = (to_cell._y1 + to_cell._y2) // 2
        self._win.draw_line(Line(self_center_x, self_center_y, other_center_x, other_center_y), fill_color)