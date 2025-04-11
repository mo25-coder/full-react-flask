// import React, { useEffect, useState } from 'react';
// import axios from 'axios';

// const UserShows = () => {
//   const [userData, setUserData] = useState(null);
//   const [loading, setLoading] = useState(true);

//   useEffect(() => {
//     // Fetch data from Flask backend
//     axios.get('http://127.0.0.1:5000/user-data')
//       .then(response => {
//         setUserData(response.data);
//         setLoading(false);
//       })
//       .catch(error => {
//         console.error('Error fetching data:', error);
//         setLoading(false);
//       });
//   }, []);

//   if (loading) {
//     return <p>Loading...</p>;
//   }

//   if (!userData) {
//     return <p>No user data available.</p>;
//   }

//   return (
//     <div>
//       <h1>{userData.name}'s Shows</h1>
//       <p>Email/Phone: {userData.email_or_phone}</p>
//       <div>
//         {userData.shows.map((show) => (
//           <div key={show.show_id} style={{ border: '1px solid #ccc', margin: '10px', padding: '10px' }}>
//             <h3>{show.show_name} ({show.show_category})</h3>
//             <p>{show.show_description}</p>
//             <p>Rating: {show.show_rating}</p>
//             <p>Time: {show.show_time}</p>
//             <p>Age Limit: {show.show_age_limit}</p>
//             <p>Category: {show.category_name}</p>
//             <p>Liked: {show.is_liked ? 'Yes' : 'No'}</p>
//             <p>Disliked: {show.is_disliked ? 'Yes' : 'No'}</p>
//           </div>
//         ))}
//       </div>
//     </div>
//   );
// };

// export default UserShows;

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const UserShows = () => {
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch data from Flask backend
    axios.get('http://127.0.0.1:5000/user-data')
      .then(response => {
        setUserData(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (!userData) {
    return <p>No user data available.</p>;
  }

  return (
    <div>
      <h1>{userData.name}'s Shows</h1>
      <p>Email/Phone: {userData.email_or_phone}</p>
      <div>
        {userData.shows.map((show) => (
          <div key={show.show_id} style={{ border: '1px solid #ccc', margin: '10px', padding: '10px' }}>
            <h3>{show.show_name} ({show.show_category})</h3>
            <p>{show.show_description}</p>
            <p>Rating: {show.show_rating}</p>
            <p>Time: {show.show_time}</p>
            <p>Age Limit: {show.show_age_limit}</p>
            <p>Category: {show.category_name}</p>
            <p>Liked: {show.is_liked ? 'Yes' : 'No'}</p>
            <p>Disliked: {show.is_disliked ? 'Yes' : 'No'}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default UserShows;

