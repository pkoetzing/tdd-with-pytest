# TDD in Python with pytest

This is a Python package used for the "TDD with pytest" workshop.

## TDD benefits

- Writing tests require that you know the inputs and output to make the feature work - TDD forces us to think about the `application interface` before we start coding.
- Increased `confidence in codebase`. By having automated tests for all features, developers feel more confident when developing new features. It becomes trivial to test the entire system to see if new changes broke what existed before.
- TDD does not eliminate all bugs, but the likelihood of encountering them is lower. When trying to `fix a bug`, you can write a test for it to ensure it's fixed when done coding.
- Tests can be used as further `documentation`. As we write the inputs and outputs of a feature, a developer can look at the test and see how the code's interface is meant to be used.

## Red - Green - Refactor

- First write the tests. Then run pytest to see them fail.
- Second write the code. Run pytest to see them succeed.
- Enhance the code by making it readable and efficient (if needed) w/o violating the tests

## Aim to test `Corner Cases`

`Wikipedia`: A `corner case` (or pathological case) involves a problem or situation that occurs only outside of normal operating parameters—specifically one that manifests itself when multiple environmental variables or conditions are simultaneously at extreme levels, even though each parameter is within the specified range for that parameter.

## Write a module `calculator` that performs some basic calculations

- `Addition` of multiple arguments.
- `Subtraction` of 2 arguments.
- `Multiplication` of multiple arguments. Multiplication by zero must raise a `ValueError` exception.
- `Division` of 2 arguments. Division by zero shall not raise an exeption but return `+/-inf`.
- `Averaging` of an iterator with two optional upper and lower thresholds to remove outliers.
