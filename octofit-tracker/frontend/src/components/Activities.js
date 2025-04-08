import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('/api/activities/')
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Activities</h1>
      <div className="row">
        {activities.map(activity => (
          <div className="col-md-4 mb-4" key={activity._id}>
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{activity.activity_type}</h5>
                <p className="card-text">Duration: {activity.duration} minutes</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Activities;