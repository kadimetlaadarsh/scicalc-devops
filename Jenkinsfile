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
                # Create a virtual environment for Ansible
                python3 -m venv venv_ansible || true
                . venv_ansible/bin/activate

                # Upgrade pip inside the venv
                pip install --upgrade pip --break-system-packages

                # Install Ansible and Docker SDK inside venv
                pip install ansible --break-system-packages
                ansible-galaxy collection install community.docker


                # Run the deployment playbook (note the path change)
                ansible-playbook -i ansible/inventory.ini ansible/deploy.yml \
                    -e "image=adarshareddy69/scicalc:latest" \
                    -e "container_name=sci_calculator" \
                    -e "command='python main.py --op sqrt --x 16'"

                # Deactivate venv
                deactivate
                '''
            }
        }


        
    }
}
