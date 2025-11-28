pipeline {
    agent any

    environment {
        IMAGE_NAME = "YOURDOCKERHUBUSERNAME/cyberdef25-inference"
        IMAGE_TAG = "latest"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                    """
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                script {
                    sh """
                    docker push ${IMAGE_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }

        stage('Run Docker Compose') {
            steps {
                script {
                    sh """
                    docker-compose down || true
                    docker-compose up --build -d
                    """
                }
            }
        }
    }

    post {
        always {
            sh "docker logout || true"
        }
    }
}
