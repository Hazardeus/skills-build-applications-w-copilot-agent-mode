import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch('/api/leaderboard/')
      .then(response => response.json())
      .then(data => setLeaderboard(data))
      .catch(error => console.error('Error fetching leaderboard:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Leaderboard</h1>
      <div className="row">
        {leaderboard.map(entry => (
          <div className="col-md-4 mb-4" key={entry._id}>
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{entry.user.username}</h5>
                <p className="card-text">Score: {entry.score}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Leaderboard;
