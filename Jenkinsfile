
pipeline {
    agent any

    stages {
        stage('Check Environment') {
            steps {
                bat 'where python'
                bat 'python --version'
                bat 'where docker'
                bat 'docker --version'
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/saanvisawant2006-max/Lab10-End-to-End-Pipeline.git'
            }
        }

        stage('Install Dependencies and Test') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m pytest -v'
            }
        }

        stage('Security Scan') {
            steps {
                bat 'python -m pip install bandit'
                bat 'python -m bandit -r app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t lab10-app:latest .'
            }
        }
    }

    post {
        success {
            echo 'Lab 10 pipeline completed successfully.'
        }
        failure {
            echo 'Lab 10 pipeline failed. Check the console output.'
        }
    }
}


