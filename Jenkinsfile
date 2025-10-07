pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'PYTHONPATH=. pytest -v tests/'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t adarshareddy69/scicalc:latest .'
            }
        }

        stage('Push Docker Hub') {
            steps {
                sh '''
                echo "$DOCKERHUB_CREDENTIALS_PSW" | docker login -u "$DOCKERHUB_CREDENTIALS_USR" --password-stdin
                docker push adarshareddy69/scicalc:latest
                '''
            }
        }
    }
}
