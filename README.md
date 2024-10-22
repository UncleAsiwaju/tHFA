<!-- This README template is inspired by othneildrew's Best-README-Template repo avaible at : https://github.com/othneildrew/Best-README-Template/tree/master
-->
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/downloads/release/python-3110/)  [![Conda](https://img.shields.io/badge/Venv-miniconda3-green)](https://docs.conda.io/en/latest/miniconda.html)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://www.iqvia.com/">
    <img src="https://upload.wikimedia.org/wikipedia/en/thumb/5/5a/IQVIA.svg/1280px-IQVIA.svg.png" alt="IQVIA_logo" width="500">
  </a>
</div>

# IQVIA tHFA Analysis Tool

<!-- ABOUT THE PROJECT -->
## About The Project

Here's a blank template to get started. To started, give a short description of the project.

### Built With

- 
- 
- 

<!-- GETTING STARTED -->
## Getting Started

_This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps._

### Prerequisites

_List of prerequisites._

- [miniconda](https://docs.conda.io/projects/miniconda/en/latest/) or [anaconda](https://www.anaconda.com/download) installed
- 

### Installation

1. Clone project repo
    ```sh
    $ git clone https://github.com/adrienpra/Template_Python.git
    ```

2. Create virtual environnement named these_BG274510 from .yml 
    ```sh
    $ conda env create -f environment.yml
    ```

3. Install pyhton dependencies and build project wheel
    ```sh
    $ conda activate these_BG274510
    $ pip install -e .
    ```
4. Install specific group dependencies
    ```sh
    $ pip install .[doc]
    ```

### Docs
1. Generate docs
    ```sh
    $ ./docs/make html
    ```

2. Docs' available at `.\docs\_build\html\index.html`

### Tests
1. Run tests
    ```sh
    $ cd ./tests/
    $ pytest --cov
    $ coverage html
    ```
2. Tests' coverage available at `.\tests\htmlcov\index.html`

## Additional informations

<!-- USAGE EXAMPLES -->
### Usage

_Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources._

For more examples, please refer to the documentation.

<!-- ROADMAP -->
### Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

<!-- LICENSE -->
### License

This project is released under the [MIT License](LICENSE).

<!-- CONTACT -->
### Contact

Your Name - seun.osonuga.work@gmail.com

Project Link: [https://www.python.org/](https://www.python.org/)

<!-- ACKNOWLEDGMENTS -->
### Acknowledgments

 - Valentine Adaiwo - IQVIA
 - Nnaemeka Iduma - IQVIA
 - Prankuri xxxxxx - The Global Fund
 - Japneet Xxxxxx - The Global Fund
 - Rohit Xxxxxx - The Global Fund
