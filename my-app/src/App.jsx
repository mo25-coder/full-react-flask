import React from 'react';
import UserShows from './UserShows';
import SignIn from './SignIn';

function App() {
  return (
    <div className="App">
      <h1>Welcome to the Show App</h1>
      {/* <UserShows /> */}
      <SignIn />
      {/* Uncomment the line below to display user shows */}
      {/* <UserShows /> */}
    </div>
  );
}

export default App;
