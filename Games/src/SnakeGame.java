import java.util.LinkedList;
import java.util.Objects;
import java.util.Random;
import java.util.Scanner;

public class SnakeGame {

    public static void main(String[] args) {
        new SnakeGame().startGame();
    }

    private static final int WIDTH = 20;
    private static final int HEIGHT = 10;
    private LinkedList<Point> snake;
    private Point food;
    private char[][] board;
    private Direction direction;
    private boolean isGameOver;
    private Random random;

    public SnakeGame() {
        snake = new LinkedList<>();
        board = new char[HEIGHT][WIDTH];
        random = new Random();
    }

    public void startGame() {
        initialize();
        while (!isGameOver) {
            printBoard();
            handleInput();
            move();
            checkCollision();
            spawnFood();
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("Game Over!");
    }

    private void initialize() {
        direction = Direction.RIGHT;
        snake.add(new Point(0, 0));
        isGameOver = false;
        spawnFood();
    }

    private void printBoard() {
        for (int i = 0; i < HEIGHT; i++) {
            for (int j = 0; j < WIDTH; j++) {
                char cell = board[i][j];
                if (cell == 'X') {
                    System.out.print("X");
                } else if (snake.contains(new Point(j, i))) {
                    System.out.print("O");
                } else if (food.getX() == j && food.getY() == i) {
                    System.out.print("F");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }

    private void handleInput() {
        Scanner scanner = new Scanner(System.in);
        char input = scanner.next().charAt(0);
        switch (input) {
            case 'w':
                direction = Direction.UP;
                break;
            case 's':
                direction = Direction.DOWN;
                break;
            case 'a':
                direction = Direction.LEFT;
                break;
            case 'd':
                direction = Direction.RIGHT;
                break;
        }
    }

    private void move() {
        Point head = snake.getFirst();
        Point newHead = new Point(head.getX(), head.getY());

        switch (direction) {
            case UP:
                newHead.setY(newHead.getY() - 1);
                break;
            case DOWN:
                newHead.setY(newHead.getY() + 1);
                break;
            case LEFT:
                newHead.setX(newHead.getX() - 1);
                break;
            case RIGHT:
                newHead.setX(newHead.getX() + 1);
                break;
        }

        snake.addFirst(newHead);
        snake.removeLast();
    }

    private void checkCollision() {
        Point head = snake.getFirst();
        if (head.getX() < 0 || head.getX() >= WIDTH || head.getY() < 0 || head.getY() >= HEIGHT) {
            isGameOver = true;
            return;
        }
        if (snake.contains(head) && !head.equals(snake.getLast())) {
            isGameOver = true;
            return;
        }
        if (head.equals(food)) {
            snake.addLast(food);
            spawnFood();
        }
    }

    private void spawnFood() {
        int x, y;
        do {
            x = random.nextInt(WIDTH);
            y = random.nextInt(HEIGHT);
        } while (snake.contains(new Point(x, y)));
        food = new Point(x, y);
    }

    private enum Direction {
        UP, DOWN, LEFT, RIGHT
    }

    private class Point {
        private int x;
        private int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) {
                return true;
            }
            if (obj == null || getClass() != obj.getClass()) {
                return false;
            }
            Point point = (Point) obj;
            return x == point.x && y == point.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }

        public void setY(int y) {
            this.y = y;
        }

        public void setX(int x) {
            this.x = x;
        }
    }
}
