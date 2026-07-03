import { useEffect, useState } from "react";

export default function Home() {
  const [properties, setProperties] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/properties/")
      .then(res => res.json())
      .then(data => setProperties(data));
  }, []);

  return (
    <div style={{ padding: 30, fontFamily: "Arial" }}>
      <h1>🏠 AEGIS Property Intelligence Platform</h1>

      <p>AI-powered property decisions for buyers and investors</p>

      {properties.map(p => (
        <div key={p.id} style={{
          margin: 10,
          padding: 15,
          border: "1px solid #ddd",
          borderRadius: 8
        }}>
          <h3>{p.title}</h3>
          <p>💰 £{p.price}</p>
          <p>📍 {p.location}</p>
          <p>🛏 {p.bedrooms} bedrooms</p>
        </div>
      ))}
    </div>
  );
}
