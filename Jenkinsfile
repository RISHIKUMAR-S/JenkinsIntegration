pipeline {
    agent none
    stages {
        stage('checkout') { 
            agent any
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/python']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RISHIKUMAR-S/JenkinsIntegration.git']]])
            }
        }
        stage('Build') { 
            //agent { docker { image 'python:3.10.1-alpine' } }
            agent any
            steps {
                git branch: 'python', url: 'https://github.com/RISHIKUMAR-S/JenkinsIntegration.git'
                sh 'python list_dict.py'
            }
        }
        stage('Test') {
            steps {
                echo "Testing the app..."
            }
        }
    }
    post{
        success {
            echo "hooray , it succedded"
        }
    }
}
