pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code already checked out by Jenkins'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-portal:latest .'
            }
        }

        stage('Verify Image') {
            steps {
                sh 'docker images | grep employee-portal'
            }
        }

    }
}