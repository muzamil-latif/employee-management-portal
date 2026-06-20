pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-portal:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker rm -f employee-app || true
                docker run -d \
                  --name employee-app \
                  -p 5000:5000 \
                  employee-portal:latest
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
            }
        }
    }
}