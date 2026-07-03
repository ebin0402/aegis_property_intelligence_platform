import { useEffect, useState } from "react";

export default function Home() {
  const [properties, setProperties] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/properties/")
      .then(res => res.json())
      .then(data => setProperties(data));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>AEGIS Property Intelligence</h1>

      {properties.map(p => (
        <div key={p.id} style={{ margin: 10, padding: 10, border: "1px solid #ccc" }}>
          <h3>{p.title}</h3>
          <p>£{p.price}</p>
          <p>{p.location}</p>
        </div>
      ))}
    </div>
  );
}
