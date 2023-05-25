pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Set up the environment and install dependencies
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                // Execute the Python application
                sh 'python your_application.py'
            }
        }
    }
}
