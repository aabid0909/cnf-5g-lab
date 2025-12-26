pipeline {
    agent any

    stages {
        stage('Check Environment') {
            steps {
                sh '''
                    python3 --version
                    robot --version
                '''
            }
        }

        stage('Start AMF & SMF') {
            steps {
                sh '''
                    nohup python3 api/amf_api.py &
                    nohup python3 api/smf_api.py &
                    sleep 3
                '''
            }
        }

        stage('Run Robot CNF Tests') {
            steps {
                sh 'robot robot/'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*.html,*.xml', fingerprint: true
        }
        success {
            echo "✅ CNF API Tests PASSED"
        }
        failure {
            echo "❌ CNF API Tests FAILED"
        }
    }
}
