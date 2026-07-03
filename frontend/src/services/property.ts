export async function fetchProperties() {
  const res = await fetch("http://localhost:8000/api/v1/properties");
  return res.json();
}
