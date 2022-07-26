pipeline {
    agent any
    parameters {
        choice(name: 'VERSION', choices: ['1.1','1.2'], description: 'Version of the build')
        booleanParam(name: 'executeTest', defaultValue: true, description: 'choice to test the build or not')
        string(name: 'user', defaultValue: 'John', description: 'A user that triggers the pipeline')
    } 
    stages {
        stage('Build') { 
            steps {
                echo 'Building the app'
            }
        }
        stage('Test') { 
            when {
                expression {
                    echo "condition checking"
                    return params.executeTest
                }
            }
            steps {
                echo "Testing the app version ${params.VERSION}"
            }
        }
        stage('Deploy') { 
            steps {
                echo "deploying the app version ${params.VERSION}"
            }
        }
    }
    post{
        success {
            echo 'it succedded'
        }
    }
}
