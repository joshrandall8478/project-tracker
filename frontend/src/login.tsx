import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

let apiServer = "http://localhost:5000";

if (import.meta.env.VITE_API_SERVER !== undefined) {
  apiServer = import.meta.env.VITE_API_SERVER;
}

function Login() {
     const [username, setName] = useState<string>("");
    const [password, setPassword] = useState<string>("");
    const [successMessage, setSuccessMessage] = useState<string>("");
    const [errorMessage, setErrorMessage] = useState<string>("");

    const navigate = useNavigate();

    const handleSubmit = async(e: React.FormEvent) => {
    e.preventDefault();
    const formValues = { username, password };
    {
      axios
        .post(`${apiServer}/api/login`, formValues)
        .then((response) => {
            const token = response.data.token; // Get JWT from response
            if (token) {
            localStorage.setItem("jwt_token", token); // Store JWT token in localStorage
            setSuccessMessage("Login successful! Redirecting..."); // Display success message
            setTimeout(() => {
              navigate("/"); // Redirect to VideoPlayer after success message
            }, 1500); // Redirect after 1.5 seconds
          } else {
            setErrorMessage("Invalid username/email or password");
          }
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
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
            <div>
                {successMessage && (
            <div className="auth__success-message">{successMessage}<br /></div>
          )}
          {errorMessage && (
            <div className="auth__error-message">{errorMessage}</div>
          )}
            <label htmlFor="username">
              <strong>Username</strong>
            </label>
            <input
              type="username"
              id="username"
              value={username} // Can be username OR email
              onChange={(e) => setName(e.target.value)}
              placeholder="Enter Username"
            />
            <br></br>
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
              /><br></br>
              <button type="submit">Login</button>
              </div>
        </form>
        </>
    )
}

export default Login