import random as rand

class MatrixCrawler:
    def __init__(self, matrix):
        self.x = 0
        self.y = 0
        self.left_bound = 0
        self.top_bound = 0
        self.right_bound = len(matrix[0]) - 1 
        self.bottom_bound = len(matrix) - 1
        self.move_horizontal = 1
        self.move_vertical = 0
        self.matrix = matrix

    def move(self):
        self.x += self.move_horizontal
        self.y += self.move_vertical
        if self.x > self.right_bound:
            self.x -= 1 
            self.top_bound += 1
            self.move_horizontal = 0
            self.move_vertical = 1
            self.y += self.move_vertical
        elif self.x < self.left_bound:
            self.x += 1
            self.bottom_bound -= 1
            self.move_horizontal = 0
            self.move_vertical = -1 
            self.y += self.move_vertical
        elif self.y > self.bottom_bound:
            self.y -= 1
            self.right_bound -= 1
            self.move_horizontal = -1
            self.move_vertical = 0
            self.x += self.move_horizontal 
        elif self.y < self.top_bound:
            self.y += 1
            self.left_bound += 1
            self.move_horizontal = 1
            self.move_vertical = 0
            self.x += self.move_horizontal
    def getPosition(self):
        return self.x, self.y

    def crawl(self):
        for row in self.matrix:
            for col in self.matrix[0]:
                print self.matrix[self.y][self.x]
                self.move()

def randomMatrix(rows, cols):
    matrix = []
    for row in range(rows):
        aRow = [] 
        for col in range(cols):
            aRow.append(rand.randint(0, 9))
        matrix.append(aRow)
    return matrix
 
matrix = randomMatrix(3, 3)                
matrix_crawler = MatrixCrawler(matrix)
print matrix
matrix_crawler.crawl()
