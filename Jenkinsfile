pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out Airline Crew Scheduling project'
                checkout scm
            }
        }

        stage('Install') {
            steps {
                echo 'Installing Python dependencies'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Duty-Limit Validator tests'
                bat 'python -m pytest test_duty_validator.py -v'
            }
        }

        stage('Package') {
            steps {
                echo 'Building Docker image'
                bat 'docker build -t duty-validator:0.1 .'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check console output.'
        }
    }
}
