# **Auto Driving Car Simulator**

## **Project Overview**

The Auto Driving Car Simulator is a web-based application designed to simulate the movement of one or more autonomous cars within a defined rectangular field. The cars can execute a sequence of commands to move forward, rotate left, or rotate right, while maintaining their direction and position on the grid. The simulator is divided into two parts:

1. **Part 1:** Simulates the movement of a single car.
2. **Part 2:** Simulates the movement of multiple cars and detects collisions if they attempt to occupy the same position on the grid.

This application is built using Python's Flask framework and includes both backend logic and a user-friendly frontend interface.

## **Design and Assumptions**

### **1. Application Design**

- **Backend:**
  - The backend is built using Python.
  - The core logic of the car movements and collision detection is encapsulated in two primary classes: `Car` and `Field`, located in the `src` directory.
  - The `Car` class handles the individual car's state and movement logic.
  - The `Field` class manages the grid and handles multiple cars, ensuring they remain within bounds and detecting collisions.

- **Frontend:**
  - The frontend is built using HTML, CSS, and JavaScript, with Bootstrap integrated for responsive design and styling.
  - The user interacts with the simulator through an intuitive web interface, where they can input commands and view results immediately.

- **Flask Application:**
  - The Flask application (`app.py`) serves as the web server, handling routing and processing user inputs. The application exposes two main endpoints:
    - `/simulate_part1`: Handles single-car simulations.
    - `/simulate_part2`: Handles multiple-car simulations.

### **2. Assumptions**

- **Input Format:**
  - For both Part 1 and Part 2, the input must follow a strict format as per the Sample Inputs given.
  - For Part 1, the input consists of three lines: field dimensions, initial car position and direction, and a sequence of commands.
  - For Part 2, the input includes the field dimensions and the details of multiple cars (identifier, position, direction, and commands).

- **Collision Detection:**
  - The simulation stops as soon as a collision is detected, and the positions and step number of the collision are reported.
  - 2 or more cars 'collide' only if they end on the same coordinates after their respective steps (i.e. After all actions on Step X are completed). Else, the cars will be considered to have driven past each other (e.g. Car A at (1, 2) going East and Car B at (2, 2) going West do not collide but have driven past each other since they end on different coordinates).


### **3. Environment Requirements**

- **Operating System:**
  - The application can be run on Windows, Linux, or macOS, as long as the required dependencies are installed.

- **Dependencies:**
  - Python 3.7 or higher
  - Flask 3.0.3
  - Bootstrap (via CDN)

## **Setup and Running the Application**

### **1. Installation Instructions**

#### **Step 1: Clone the Repository**

First, clone the repository containing the application code:

```bash
git clone https://github.com/adamtwh/potential-octo-journey
cd potential-octo-journey
```

#### **Step 2: Set Up a Virtual Environment**

It’s recommended to use a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

#### **Step 3: Install Dependencies**

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

#### **Step 4: Run the Flask Application**

To start the Flask development server, run:

```bash
export FLASK_APP=app.py  # On Windows, use `set FLASK_APP=app.py`
export FLASK_ENV=development  # Optional: for enabling debug mode
flask run
```

The application will start and can be accessed at `http://127.0.0.1:5000` in your web browser.

### **2. Detailed Usage Instructions**

1. **Access the Application:**
   - Navigate to `http://127.0.0.1:5000` in your browser to access the Auto Driving Car Simulator interface.

2. **Part 1: Single Car Simulation**
   - Input the field dimensions, initial position, and direction of the car, and the sequence of commands in the designated form.
   - You can use the "Insert Sample Input" button to quickly test the simulator.
   - Click "Simulate Part 1" to view the final position and direction of the car after executing the commands.

3. **Part 2: Multiple Cars Simulation**
   - Input the field dimensions, followed by the details for each car (identifier, position, direction, commands).
   - You can use the "Insert Sample Input" button for a quick test case.
   - Click "Simulate Part 2" to see if any collisions occur during the simulation. The result will indicate the cars involved in the collision, the position, and the step number.

### **3. Testing the Application**

The application includes unit tests and integration tests to ensure all functionalities work as expected. To run the tests:

```bash
python -m unittest discover tests
```

This will execute all the test cases located in the `tests` directory.

## **Conclusion**

The Auto Driving Car Simulator is designed with simplicity and user-friendliness in mind, providing an interactive platform for simulating the movements of autonomous cars. The modular design ensures that the application is maintainable and extendable, while the clean and responsive UI makes it accessible to a wide range of users. Please follow the instructions provided to set up and run the application on your preferred environment.

For any further queries or issues, please reach out to me (adamtwh@gmail.com).