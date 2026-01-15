import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

let apiServer = "http://localhost:5000";

if (import.meta.env.VITE_API_SERVER !== undefined) {
  apiServer = import.meta.env.VITE_API_SERVER;
}

function Index() {
    const [loggedIn, setLoggedIn] = useState(false);
    const [username, setUsername] = useState("");
    const token = localStorage.getItem("jwt_token");
    // Check login state, and modify useStates if needed
    async function checkLoginState() {
      if (token) {
        try{
          const response = await axios.get(`${apiServer}/api/current_user`, {
            headers: {
            'Authorization': `Bearer ${token}`
          }
          });
          setUsername(response.data.username);
          setLoggedIn(true)
        }
        catch (error) {
          console.error("Failure to get username.", error)
        }
      }
    }
    checkLoginState();

    const handleLogout = () => {
    // Clear the authentication token from localStorage
    localStorage.removeItem("jwt_token");
    // Navigate to index (force refresh the page)
    window.location.href = "/";
  };
    
    return (
    <>
      <div>
        
          {!loggedIn && (<div>
          <a href="/login">Sign In</a><br></br>
          <a href="/signup">Sign Up</a>
          </div>
          )}
          {loggedIn && (<div>
            <h2>Welcome, {username}</h2>
            <button onClick={handleLogout}>Logout</button>
          </div>
          )
          }
        
      </div>
    </>
)
}

export default Index