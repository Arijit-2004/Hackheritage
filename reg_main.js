// setting up firebase with our website
const firebaseApp = firebase.initializeApp({
  apiKey: "AIzaSyD8zTQgud3ad1WQcKhGqIOo-ZQHCPHFG5k",
  authDomain: "authentic-b0cc0.firebaseapp.com",
  databaseURL: "https://authentic-b0cc0-default-rtdb.firebaseio.com",
  projectId: "authentic-b0cc0",
  storageBucket: "authentic-b0cc0.appspot.com",
  messagingSenderId: "596293461019",
  appId: "1:596293461019:web:a43b175ddeccd4ee9cc4be"
});
const db = firebaseApp.firestore();
const auth = firebaseApp.auth();

// Sign up function
const signUp = () => {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  console.log(email, password)
  // firebase code
  firebase.auth().createUserWithEmailAndPassword(email, password)
      .then((result) => {
          // Signed in 
          document.write("You are Signed Up")
          console.log(result)
          // ...
      })
      .catch((error) => {
          console.log(error.code);
          console.log(error.message)
          // ..
      });
}

// Sign In function
const signIn = () => {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  // firebase code
  firebase.auth().signInWithEmailAndPassword(email, password)
      .then((result) => {
          // Signed in 
          window.location.replace('/Main.html')
        //   document.write("You are Signed In")
          console.log(result)
      })
      .catch((error) => {
          console.log(error.code);
          console.log(error.message)
      });
}
