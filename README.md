# pygrain
An application development framework built on the
Pygame library with integration for Tkinter windows.

You can install pygrain using
> pip install pygrain

There are several built-in UI components:

- Button
- Text
- Image
- Toggle switch
- Slider
- Scrollbar
- Textbox
- Point

# Packaging and Publishing Instructions

## Prerequisites

- Python
- `setuptools`
- `wheel`
- `build`
- `twine`

## Building the Package

1. Clone the repository.
2. Navigate to the project directory.
3. Run the following command:

   ```
   python -m build
   ```

   This will create source and wheel distribution files in a `dist` directory.

## Publishing to PyPI

1. Register an account on PyPI if you haven't already.
2. Build the package using the instructions above.
3. Run the following command:

   ```
   twine upload dist/*
   ```

   You will be prompted to enter your PyPI username and password.


## Contribution Guidelines

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and test them thoroughly.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact Information

For any questions or issues, please contact the project maintainers.
