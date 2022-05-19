import random


def generate_points(num_points):
    return {(random.randrange(num_points), random.randrange(num_points)) for i in range(num_points)}


def main():
    points = generate_points(5)
    print(points)


if __name__ == '__main__':
    main()
