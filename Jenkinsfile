pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out Airline Crew Scheduling from the verified GitHub remote'
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/feature/weekly-limit']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/manojshet2005/Airline-Crew-Scheduling..git'
                    ]]
                ])
            }
        }

        stage('Install') {
            steps {
                echo 'Creating an isolated Python environment and installing dependencies'
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Compiling validator and tests'
                bat '.venv\\Scripts\\python.exe -m compileall -q duty_validator.py test_duty_validator.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running all available project tests'
                bat '.venv\\Scripts\\python.exe -m pytest -q'
            }
        }

        stage('Quality Check') {
            steps {
                echo 'Checking installed dependency consistency'
                bat '.venv\\Scripts\\python.exe -m pip check'
            }
        }

        stage('Package Source Archive') {
            steps {
                echo 'Packaging the tested source files; this stage does not claim a Docker image build'
                bat '.venv\\Scripts\\python.exe -m zipfile -c duty-validator.zip duty_validator.py test_duty_validator.py requirements.txt Dockerfile'
                archiveArtifacts artifacts: 'duty-validator.zip', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Checkout, isolated dependency installation, tests, and source archive completed successfully. No Docker image was built.'
        }
        failure {
            echo 'Pipeline failed. Check console output.'
        }
    }
}
