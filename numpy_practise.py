import numpy as np

class NumpyDemo:
    def __init__(self):
        """Initialize the NumpyDemo class."""
        pass

    def create_array(self, list_of_values):
        """
        Creates a numpy array from a list of values.
        
        Args:
        list_of_values (list): A list of values to convert into a numpy array.

        Returns:
        numpy.ndarray: The created numpy array.
        """
        array = np.array(list_of_values)
        return array

    def basic_operations(self, array):
        """
        Demonstrates basic arithmetic operations on a numpy array.
        
        Args:
        array (numpy.ndarray): Input numpy array.

        Returns:
        dict: Results of operations like addition, subtraction, multiplication, and division.
        """
        return {
            "array": array,
            "add_5": array + 5,
            "multiply_by_2": array * 2,
            "square": array ** 2,
            "mean": np.mean(array),
            "sum": np.sum(array)
        }

    def reshape_array(self, array, new_shape):
        """
        Reshapes a numpy array into a given shape.
        
        Args:
        array (numpy.ndarray): Input numpy array.
        new_shape (tuple): The new shape as a tuple.

        Returns:
        numpy.ndarray: Reshaped numpy array.
        """
        reshaped_array = array.reshape(new_shape)
        return reshaped_array

    def matrix_multiplication(self, matrix1, matrix2):
        """
        Demonstrates matrix multiplication using numpy.
        
        Args:
        matrix1 (numpy.ndarray): First matrix.
        matrix2 (numpy.ndarray): Second matrix.

        Returns:
        numpy.ndarray: The product of the two matrices.
        """
        product = np.dot(matrix1, matrix2)
        return product

    def generate_random_array(self, shape):
        """
        Generates a random numpy array with a given shape.
        
        Args:
        shape (tuple): The shape of the array (rows, columns).

        Returns:
        numpy.ndarray: Randomly generated numpy array.
        """
        random_array = np.random.random(shape)
        return random_array

    def calculate_statistics(self, array):
        """
        Demonstrates statistical operations on a numpy array.
        
        Args:
        array (numpy.ndarray): Input numpy array.

        Returns:
        dict: Results of statistical operations like mean, standard deviation, and variance.
        """
        return {
            "mean": np.mean(array),
            "std_dev": np.std(array),
            "variance": np.var(array),
            "min": np.min(array),
            "max": np.max(array)
        }

# Example usage of the class
if __name__ == "__main__":
    demo = NumpyDemo()

    # Create an array
    array = demo.create_array([1, 2, 3, 4, 5])
    print("Created Array:", array)

    # Perform basic operations
    operations = demo.basic_operations(array)
    print("\nBasic Operations on Array:", operations)

    # Reshape the array
    reshaped_array = demo.reshape_array(array, (5, 1))
    print("\nReshaped Array:", reshaped_array)

    # Matrix multiplication example
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    product = demo.matrix_multiplication(matrix1, matrix2)
    print("\nMatrix Multiplication Result:\n", product)

    # Generate a random array
    random_array = demo.generate_random_array((2, 3))
    print("\nRandom Array:\n", random_array)

    # Calculate statistics on the array
    stats = demo.calculate_statistics(array)
    print("\nStatistics on the Array:", stats)
