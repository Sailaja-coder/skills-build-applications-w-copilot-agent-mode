import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const apiUrl = "http://localhost:8000/api/teams/";

  useEffect(() => {
    console.log('Fetching teams from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Fetched teams:', results);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <h2 className="mb-3">Teams</h2>
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th>#</th>
            <th>Name</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {teams.map((team, idx) => (
            <tr key={idx}>
              <td>{idx + 1}</td>
              <td>{team.name}</td>
              <td>{team.description}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Teams;
