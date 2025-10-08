pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker_hub')
        DOCKER_HOST = "unix:///home/adarsha/.docker/desktop/docker-cli.sock"
    }

    stages {
        stage('Checkout') {
            steps { 
                checkout scm 
            }
        }

        stage('Install Dependencies') {
            steps {
                // Create venv if not exists and install dependencies
                sh '''
                python3 -m venv venv || true
                . venv/bin/activate
                pip install --upgrade pip --break-system-packages
                pip install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Activate venv and run tests
                sh '''
                . venv/bin/activate
                PYTHONPATH=. python -m pytest -v tests/
                '''
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
