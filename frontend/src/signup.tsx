import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

let apiServer = "http://localhost:5000";

if (import.meta.env.VITE_API_SERVER !== undefined) {
  apiServer = import.meta.env.VITE_API_SERVER;
}

function SignUp() {
    // useStates for form values, and success/error messages
    const [username, setName] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const [successMessage, setSuccessMessage] = useState<string>("");
    const [errorMessage, setErrorMessage] = useState<string>("");

    const navigate = useNavigate();

    // async function for handling form submit
    const handleSubmit = async(e: React.FormEvent) => {
    e.preventDefault();
    const formValues = { username, password };
    {
      axios
        .post(`${apiServer}/api/users`, formValues)
        .then(() => {
            // Set success message to display if form passes
          setSuccessMessage(
            "You have successfully signed up! Redirecting."
          );
          setTimeout(() => {
            navigate("/login"); // Redirect after 3 seconds
          }, 3000);
          // Reset name and password on fail
          setName("");
          setPassword("");
        })
        .catch((error) => {
          // Check if the status is 409 (Conflict) or some other error
          if (error.response) {
            if (error.response.status === 409) {
              setErrorMessage(error.response.data.message); // Sets error message to error message as written in route
            } else if (error.response.status === 400)
              setErrorMessage(error.response.data.message);
            else {
              setErrorMessage(
                "An unexpected error occurred. Please try again."
              );
            }
          }
        });
    }
  };
    return(
        <>
        <h2>Sign Up</h2>
        <form onSubmit={handleSubmit}>
            <div>
                {successMessage && (
            <div className="auth__success-message">{successMessage}<br /></div>
          )}
          {errorMessage && (
            <div className="auth__error-message">{errorMessage}</div>
          )}
            <label htmlFor="name" className="auth__label">
                <strong>Username</strong>
              </label>
              <input
                type="text"
                id="username"
                value={username}
                onChange={(e) => setName(e.target.value)}
                placeholder="Enter Username"
              />
              <label htmlFor="password" className="auth__label">
                <strong>Password</strong>
              </label>
              <input
                type="password"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Enter Password"
                className="auth__form-control"
              />
              <button type="submit">Sign Up</button>
            </div>
        </form>
        </>
    )
}

export default SignUp