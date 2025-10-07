pipeline {
  agent any
  environment {
    DOCKERHUB_CREDS = 'dockerhub-creds'
    DOCKER_IMAGE = "yourdockerhubusername/scicalc-py:${env.BUILD_NUMBER}"
  }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Test') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'pytest -v'
      }
    }
    stage('Docker Build') {
      steps {
        sh "docker build -t ${DOCKER_IMAGE} ."
      }
    }
    stage('Docker Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDS}", usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
          sh "echo $DH_PASS | docker login -u $DH_USER --password-stdin"
          sh "docker push ${DOCKER_IMAGE}"
        }
      }
    }
    stage('Deploy via Ansible') {
      steps {
        sh "ansible-playbook ansible/deploy.yml -i ansible/inventory/hosts --extra-vars 'image=${DOCKER_IMAGE}'"
      }
    }
  }
  post {
    always {
      sh 'docker logout || true'
    }
  }
}
