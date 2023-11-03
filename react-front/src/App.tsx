import React, { useState, useEffect } from 'react';

function Login({ setAuthenticated, authenticated }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);

  const handleLogin = async () => {
    try {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        setError(null);
        setAuthenticated(true); // Set the user as authenticated
      } else {
        setError('Login Failed');
        setAuthenticated(false); // Set the user as not authenticated
      }
    } catch (error) {
      console.error(error);
      setError('Login Failed');
      setAuthenticated(false); // Set the user as not authenticated
    }
  };

  return (
    <div>
      <h2>Login</h2>
      {!authenticated && (
        <div>
          <div>
            <label>Username: </label>
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
          </div>
          <div>
            <label>Password: </label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
          </div>
          <button onClick={handleLogin}>Login</button>
          {error && <p>{error}</p>}
        </div>
      )}
    </div>
  );
}

function UserProfile({ authenticated }) {
  const [profileData, setProfileData] = useState(null);
  const [error, setError] = useState(null);

  const handleGetProfile = async () => {
    try {
      const response = await fetch('http://localhost:5000/profile', {
        method: 'GET',
        credentials: 'include',
      });

      if (response.ok) {
        const data = await response.json();
        setProfileData(data);
      } else {
        setError('Profile data fetch failed');
      }
    } catch (error) {
      console.error(error);
      setError('Profile data fetch failed');
    }
  }

  useEffect(() => {
    if (authenticated) {
      handleGetProfile();
    }
  }, [authenticated]);

  return (
    <div>
      <h2>User Profile</h2>
      {!authenticated && <p>Please log in to view your profile.</p>}
      {error && <p>{error}</p>}
      {authenticated && profileData && (
        <div>
          <p>Username: {profileData.username}</p>
          <p>Email: {profileData.email}</p>
          <img src={profileData.profile_picture} alt="Profile Picture" />
        </div>
      )}
    </div>
  );
}

function App() {
  const [authenticated, setAuthenticated] = useState(false);

  return (
    <div>
      <h1>Secure Token Storage Example</h1>
      <Login setAuthenticated={setAuthenticated} authenticated={authenticated} />
      <UserProfile authenticated={authenticated} />
    </div>
  );
}

export default App;
