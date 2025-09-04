# ACEest_Fitness
## Repo for DevOps Assignment - 2024TM93152 - Amruthaa V

#### Project structure - 

```
ACEest_Fitness/
│── ACEest_Fitness.py      # workout logic (from your file, refactored to separate logic from Tkinter)
│── app.py                 # Flask API entry point
│── requirements.txt
│── Dockerfile
│── README.md
│── tests/
│   └── test_app.py
│   └── test_fitness.py 
│── .github/
│   └── workflows/
│       └── ci.yml
```


Install Homebrew - 

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Add brew to PATH -
```

echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Install required tools - 

```
brew install python
brew install git
Download Docker Desktop
brew install --cask visual-studio-code
```

Validate installation - 

```
python3 --version
pip3 --version
git --version
docker --version
```

Use a virtual environment for the project - 

```
python3 -m venv venv
source venv/bin/activate
pip install flask pytest
```

Create requirements file - 

```
pip freeze > requirements.txt
```

To run the app, always run these commands in the project - 

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the app -

```
python app.py
```

Run tests - 

```
pytest
```

Create Dockerfile - 

```
mkdir Dockerfile
```

Run with Docker - 

```
docker build -t aceest-fitness .
docker run -p 5000:5000 aceest-fitness
```

Sample output when running the app with Docker - 

```
❯ docker build -t aceest-fitness .
[+] Building 5.4s (11/11) FINISHED                                                                                                                               docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                             0.0s
 => => transferring dockerfile: 199B                                                                                                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                                              4.2s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                    0.0s
 => [internal] load .dockerignore                                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                                  0.0s
 => [1/5] FROM docker.io/library/python:3.11-slim@sha256:1d6131b5d479888b43200645e03a78443c7157efbdb730e6b48129740727c312                                                        0.0s
 => => resolve docker.io/library/python:3.11-slim@sha256:1d6131b5d479888b43200645e03a78443c7157efbdb730e6b48129740727c312                                                        0.0s
 => [internal] load build context                                                                                                                                                0.3s
 => => transferring context: 26.96MB                                                                                                                                             0.3s
 => CACHED [2/5] WORKDIR /app                                                                                                                                                    0.0s
 => CACHED [3/5] COPY requirements.txt .                                                                                                                                         0.0s
 => CACHED [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                                              0.0s
 => [5/5] COPY . .                                                                                                                                                               0.1s
 => exporting to image                                                                                                                                                           0.7s
 => => exporting layers                                                                                                                                                          0.6s
 => => exporting manifest sha256:33b4adc281044686c07feab2f4111f0911595f9d6e03bea364bef37af7f8320a                                                                                0.0s
 => => exporting config sha256:57f739394b298bc8b6e9904923f5aae5e81e7580046f4de598e62f9463dc30a4                                                                                  0.0s
 => => exporting attestation manifest sha256:41d6b73c93d364881d9955748b30cc26cbb540bd116688bf8c8c747e049233ba                                                                    0.0s
 => => exporting manifest list sha256:73f1abb4d14c3bee77ec4a425f45c4d9f60b278cf69fb257f4339d8aafe6462a                                                                           0.0s
 => => naming to docker.io/library/aceest-fitness:latest                                                                                                                         0.0s
 => => unpacking to docker.io/library/aceest-fitness:latest                                                                                                                      0.1s

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview
❯ docker run -p 5000:5000 aceest-fitness
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
192.168.65.1 - - [04/Sep/2025 12:53:34] "GET / HTTP/1.1" 200 -
192.168.65.1 - - [04/Sep/2025 12:53:34] "GET /favicon.ico HTTP/1.1" 404 -
192.168.65.1 - - [04/Sep/2025 12:54:29] "POST /workout HTTP/1.1" 201 -
192.168.65.1 - - [04/Sep/2025 12:54:42] "GET /workouts HTTP/1.1" 200 -
192.168.65.1 - - [04/Sep/2025 12:54:53] "POST /workout HTTP/1.1" 201 -
192.168.65.1 - - [04/Sep/2025 12:55:01] "GET /workouts HTTP/1.1" 200 -

````
Sample CURL requests and responses - 

```
❯ curl -X POST http://localhost:5000/workout \
     -H "Content-Type: application/json" \
     -d '{"workout":"Running","duration":30}'
{"status":"success","workout":{"duration":30,"workout":"Running"}}

❯ curl http://localhost:5000/workouts
{"workouts":[{"duration":30,"workout":"Running"}]}

❯ curl -X POST http://localhost:5000/workout \
     -H "Content-Type: application/json" \
     -d '{"workout":"Running","duration":20}'
{"status":"success","workout":{"duration":20,"workout":"Running"}}

❯ curl http://localhost:5000/workouts
{"workouts":[{"duration":30,"workout":"Running"},{"duration":20,"workout":"Running"}]}
```

Set GitHub actions - 

```
mkdir -p .github/workflows
touch .github/workflows/ci.yml
```

Unit tests - 

Adding and running tests for app.py

```
❯ pytest
================================================================================ test session starts =================================================================================
platform darwin -- Python 3.13.7, pytest-8.4.1, pluggy-1.6.0
rootdir: /Users/amruthaa/workspace/DevOps_Assignment/ACEest_Fitness
plugins: cov-5.0.0
collected 3 items

tests/test_app.py ...                                                                                                                                                          [100%]

================================================================================= 3 passed in 0.22s ==================================================================================
```

Adding tests for ACEest_Fitness.py

```
❯ pytest
================================================================================ test session starts =================================================================================
platform darwin -- Python 3.13.7, pytest-8.4.1, pluggy-1.6.0
rootdir: /Users/amruthaa/workspace/DevOps_Assignment/ACEest_Fitness
plugins: cov-5.0.0
collected 6 items

tests/test_app.py ...                                                                                                                                                          [ 50%]
tests/test_fitness.py ...                                                                                                                                                      [100%]

================================================================================= 6 passed in 0.07s ==================================================================================
```

Test coverage badge - 

[![codecov](https://codecov.io/gh/2024tm93152-droid/ACEest_Fitness/branch/main/graph/badge.svg)](https://codecov.io/gh/2024tm93152-droid/ACEest_Fitness)


Important links - 

GitHub Repo - https://github.com/2024tm93152-droid/ACEest_Fitness.git

[![CI Pipeline](https://github.com/2024tm93152-droid/ACEest_Fitness/actions/workflows/ci.yml/badge.svg)](https://github.com/2024tm93152-droid/ACEest_Fitness/actions)

[![Docker Pulls](https://img.shields.io/docker/pulls/amruthaav03/aceest-fitness)](https://hub.docker.com/r/amruthaav03/aceest-fitness)

### CI/CD Overview  
This project is powered by a GitHub Actions pipeline that runs automatically every time code is pushed or a pull request is opened against the main branch. The pipeline acts as a safety net for development by setting up a clean Python environment, installing all required dependencies, and then running the full test suite. Test coverage is also measured to make sure that both the core logic and the Flask API are thoroughly validated.

After the tests pass, the workflow goes one step further and builds a Docker image of the application. This ensures that the project can run in a consistent, containerized environment across different systems, removing the “works on my machine” problem. By combining automated testing with containerization, the pipeline provides developers with fast feedback, reliable builds, and confidence that changes won’t break the application in production.