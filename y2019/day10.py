from utils import data_import
import math

def extract_asteroids(data):
    asteroids = set()
    for line_no, line in enumerate(data):
        for col_no, cell in enumerate(line):
            if cell == '#':
                asteroids.add((col_no, line_no))

    return asteroids

def count_visible_asteroids(x0, y0, asteroids):
    valid_reports = set()
    for x, y in asteroids:
        if y != y0:
            valid_reports.add(((y-y0)/abs(y-y0), (x-x0)/(y-y0)))
        else:
            if x > x0:
                valid_reports.add('Inf')
            else:
                valid_reports.add('-Inf')

    return len(valid_reports) 


def part1(data):
    asteroids = extract_asteroids(data)

    return max(count_visible_asteroids(x, y, asteroids) for x, y in asteroids)
        

def part2(data):
    asteroids = extract_asteroids(data)

    best = None
    best_value = 0

    for x, y in asteroids:
        value = count_visible_asteroids(x,y, asteroids)
        if value > best_value:
            best = x, y
            best_value = value

    x0, y0 = best

    asteroids_with_angle = []
    for x, y in asteroids:
        if x0 == x:
            if y > y0:
                angle = -math.pi/2
            else:
                angle = math.pi/2
        else:
            angle = -math.atan((y-y0)/(x-x0))

        if x < x0:
            angle -= math.pi

        distance = (y0-y)**2 + (x0-x)**2

        if x != x0 or y != y0:
            asteroids_with_angle.append((math.pi/2 - angle, distance, x, y))

    asteroids_with_angle.sort()

    all_angles = set(a[0] for a in asteroids_with_angle)

    angle = min(all_angles)

    count = 0

    while asteroids_with_angle:
        removed_angle = angle
        removed = [asteroid for asteroid in asteroids_with_angle if asteroid[0] == angle][0]
        count += 1
        if count == 200:
            return removed[2]*100 + removed[3]
        asteroids_with_angle.remove(removed)
        previous_angle = angle
        all_angles = set(a[0] for a in asteroids_with_angle)
        if not all_angles:
            return 'No 200th'
        try:
            angle = min(angle for angle in all_angles if angle > previous_angle)
        except ValueError:
            angle = min(all_angles)


if __name__ == '__main__':

    data = data_import('y2019/data/day10', cast=str)

    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
