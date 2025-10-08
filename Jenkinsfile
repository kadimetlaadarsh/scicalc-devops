pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker_hub')
        DOCKER_HOST = "unix:///var/run/docker.sock"  // default Docker socket
        IMAGE_NAME = "adarshareddy69/scicalc:latest"
        CONTAINER_NAME = "scicalc"
    }

    stages {
        stage('Checkout') {
            steps { 
                checkout scm 
            }
        }

        stage('Install Dependencies') {
            steps {
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
                sh '''
                . venv/bin/activate
                PYTHONPATH=. python -m pytest -v tests/
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Push Docker Hub') {
            steps {
                sh '''
                echo "$DOCKERHUB_CREDENTIALS_PSW" | docker login -u "$DOCKERHUB_CREDENTIALS_USR" --password-stdin
                docker push ${IMAGE_NAME}
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                # Ensure ansible is installed on Jenkins agent
                pip install --user ansible==7.9.0 community.docker

                # Run deployment playbook
                ansible-playbook -i inventory.ini deploy.yml \
                    -e "image=${IMAGE_NAME}" \
                    -e "container_name=${CONTAINER_NAME}" \
                    -e "command='python main.py --op sqrt --x 16'"
                '''
            }
        }
    }
}
