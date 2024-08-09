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

@app.route('/simulate', methods=['POST'])
def simulate():
    """
    Handle the form submission, simulate the car's movements,
    and return the final position and direction.
    """
    input_data = request.form['input']
    lines = input_data.strip().split('\n')
    
    # Ensure the input consists of exactly 3 lines
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

    # Validate direction
    if direction not in ['N', 'E', 'S', 'W']:
        return "Error: Initial direction must be one of 'N', 'E', 'S', or 'W'.", 400
    
    # Validate commands
    commands = lines[2]
    if any(c not in 'RLF' for c in commands):
        return "Error: Commands must be a sequence of 'R', 'L', and 'F' only.", 400

    try:
        # Initialize field and car
        field = Field(width, height)
        car = Car(x, y, direction)
        
        # Execute commands
        car.execute_commands(commands, field)

        # Return final position and direction as a string
        output = car.get_position()
        return output

    except Exception as e:
        return f"Error: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)
