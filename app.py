from flask import Flask, request, render_template
from src.car import Car
from src.field import Field

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the home page with the input form.
    """
    return render_template('index.html')

@app.route('/simulate_part1', methods=['POST'])
def simulate_part1():
    """
    Handle the form submission for Part 1, simulate the car's movements,
    and return the final position and direction.
    """
    input_data = request.form['input']
    lines = input_data.strip().split('\n')
    
    if len(lines) != 3:
        return "Error: Please provide exactly 3 lines of input.", 400

    try:
        # Parse field dimensions
        width, height = map(int, lines[0].split())
    except ValueError:
        return "Error: Field dimensions must be integers.", 400
    
    try:
        # Parse initial position and direction
        x, y, direction = lines[1].split()
        x, y = int(x), int(y)
    except ValueError:
        return "Error: Initial position must be integers.", 400
    except Exception:
        return "Error: Invalid initial position or direction format.", 400

    if direction not in ['N', 'E', 'S', 'W']:
        return "Error: Initial direction must be one of 'N', 'E', 'S', or 'W'.", 400
    
    commands = lines[2].strip()
    if any(c not in 'RLF' for c in commands):
        return "Error: Commands must be a sequence of 'R', 'L', and 'F' only.", 400

    try:
        # Initialize field and car for Part 1
        field = Field(width, height)
        car = Car(x, y, direction)
        
        car.execute_commands(commands, field)

        output = car.get_position()
        return output

    except Exception as e:
        return f"Error: {str(e)}", 400

@app.route('/simulate_part2', methods=['POST'])
def simulate_part2():
    """
    Handle the form submission for Part 2, simulate the car's movements,
    check for collisions, and return the result.
    """
    input_data = request.form['input']
    lines = [line.strip() for line in input_data.strip().split('\n') if line.strip()]

    # Validate that the input has the correct format:
    # The number of lines must be 3 * number_of_cars + 1 (for the field dimensions line).
    # There must be at least 2 cars.
    if len(lines) < 7 or (len(lines) - 1) % 3 != 0:
        return "Error: Invalid input format. Please provide field size and details for each car.", 400

    number_of_cars = (len(lines) - 1) // 3

    # Ensure that there are at least two cars
    if number_of_cars < 2:
        return "Error: There must be at least two cars provided.", 400

    try:
        # Parse field dimensions
        width, height = map(int, lines[0].split())
    except ValueError:
        return "Error: Field dimensions must be integers.", 400

    cars_with_commands = []
    for i in range(1, len(lines), 3):
        if i + 2 >= len(lines):
            return "Error: Invalid input format. Each car must have an identifier, position, and command sequence.", 400
        
        try:
            car_id = lines[i]
            position_line = lines[i + 1].split()

            # Ensure the position line has exactly 3 parts: x, y, and direction
            if len(position_line) != 3:
                return f"Error: Invalid position format for car {car_id}.", 400

            x, y, direction = position_line
            x, y = int(x), int(y)
            commands = lines[i + 2].strip()

            if direction not in ['N', 'E', 'S', 'W']:
                return f"Error: Invalid direction for car {car_id}. Must be one of 'N', 'E', 'S', 'W'.", 400

            if any(c not in 'RLF' for c in commands):
                return f"Error: Invalid commands for car {car_id}. Must be 'R', 'L', 'F' only.", 400

            car = Car(x, y, direction, car_id)
            cars_with_commands.append((car, commands))
        except ValueError:
            return f"Error: Invalid position or command format for car {car_id}.", 400

    try:
        # Initialize the field and simulate Part 2
        field = Field(width, height)
        result = field.simulate_multiple_cars(cars_with_commands)
        return result

    except Exception as e:
        return f"Error: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)