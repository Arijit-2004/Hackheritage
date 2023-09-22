// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.4.0/firebase-app.js";
import {
    getAuth,
    createUserWithEmailAndPassword,
  } from "https://www.gstatic.com/firebasejs/10.4.0/firebase-auth.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyD8zTQgud3ad1WQcKhGqIOo-ZQHCPHFG5k",
  authDomain: "authentic-b0cc0.firebaseapp.com",
  databaseURL: "https://authentic-b0cc0-default-rtdb.firebaseio.com",
  projectId: "authentic-b0cc0",
  storageBucket: "authentic-b0cc0.appspot.com",
  messagingSenderId: "596293461019",
  appId: "1:596293461019:web:a43b175ddeccd4ee9cc4be"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth()

// var fullName = document.getElementById("fullname");
// var contact = document.getElementById("contact");
var email = document.getElementById("email");
var password = document.getElementById("password");
// var copassword = document.getElementById("copassword")

window.signUp = function (e) {
    // if(password)
    
    //     if(fullName.value == "" || contact.value=="" || email.value =="" || password.value ==""){
    //         alert("All Field Are Required")
    //     }
    //     if(password.value == copassword.value){
         
    //     }
    //     else{
    //         alert("Password Confirmation is Wrong")
    //         return false
    //     }
    
        e.preventDefault();
        var obj = {
        //   firstName: fullName.value,
        //   contact: contact.value,
          email: email.value,
          password: password.value,
        };
      
        createUserWithEmailAndPassword(auth, obj.email, obj.password)
        .then(function(success){
            window.location.replace('/login.html')
          // console.log(success.user.uid)
          alert("signup successfully")
        })
        .catch(function(err){
          alert("Error in " + err)
        });
    //    console.log()
        console.log(obj);
};
