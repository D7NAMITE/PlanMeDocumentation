import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup } from 'firebase/auth';

const firebaseConfig = {
  apiKey: "AIzaSyDRLf6GEoHKnQcHzf8Nh4bhO8e13r0iiVI",
  authDomain: "planme-6007f.firebaseapp.com",
  projectId: "planme-6007f",
  storageBucket: "planme-6007f.appspot.com",
  messagingSenderId: "409452142687",
  appId: "1:409452142687:web:e6eb0572b53dac1ce1fbea",
  measurementId: "G-P806F77297"
};

const app = initializeApp(firebaseConfig);

export const handleGoogleSignIn = async () => {
    const auth = getAuth();
    const provider = new GoogleAuthProvider();

    try {
      const result = await signInWithPopup(auth, provider);
      const user = result.user;
      console.log('Signed in user:', user);
    } catch (error) {
      console.error('Error signing in with Google:', error);
    }
  };

