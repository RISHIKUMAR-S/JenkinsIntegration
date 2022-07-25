def Build_App(){
    echo 'Building the app'
}

def Test_App(){
    echo "Testing the app version ${param.VERSION}"
}

def Deploy_App(){
    echo "deploying the app version ${param.VERSION}"
}
return this