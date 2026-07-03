import { useState } from "react";

export default function Home() {
  const [results, setResults] = useState([]);

  const search = async () => {
    const res = await fetch("http://localhost:8000/search/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ location: "Kent", max_price: 400000 })
    });

    const data = await res.json();
    setResults(data);
  };

  return (
    <div style={{ padding: 30 }}>
      <h1>AEGIS Property Intelligence</h1>

      <button onClick={search}>Search Properties</button>

      {results.map(p => (
        <div key={p.id} style={{ marginTop: 10 }}>
          <h3>{p.title}</h3>
          <p>£{p.price}</p>
          <p>{p.location}</p>
        </div>
      ))}
    </div>
  );
}
