import { useEffect, useState } from "react";
import PropertyMap from "../components/PropertyMap";
import { fetchProperties } from "../services/property";

export default function Dashboard() {
  const [properties, setProperties] = useState([]);

  useEffect(() => {
    fetchProperties().then(setProperties);
  }, []);

  return (
    <div>
      <h1>AEGIS Property Intelligence Map</h1>
      <PropertyMap properties={properties} />
    </div>
  );
}
