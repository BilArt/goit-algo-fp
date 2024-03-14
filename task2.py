import turtle

def draw_pifagor_tree(t, branch_length, level):
    if level == 0:
        return
    t.forward(branch_length * level)
    t.right(45)
    draw_pifagor_tree(t, branch_length, level-1)
    t.left(90)
    draw_pifagor_tree(t, branch_length, level-1)
    t.right(45)
    t.backward(branch_length * level)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    
    # Створення об'єкта черепашки
    t = turtle.Turtle()
    t.color("green")
    t.speed(0) 

    # Початкові параметри фрактала
    branch_length = 20
    level = int(input("Введіть рівень рекурсії: "))

    # Позиціюємо черепашку у відповідне місце
    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    # Малюємо фрактал
    draw_pifagor_tree(t, branch_length, level)

    # Закриваємо вікно при кліку
    window.exitonclick()

if __name__ == "__main__":
    main()
