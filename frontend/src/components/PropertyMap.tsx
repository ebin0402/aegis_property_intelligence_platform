import { useEffect, useRef } from "react";
import mapboxgl from "mapbox-gl";

mapboxgl.accessToken = process.env.NEXT_PUBLIC_MAPBOX_TOKEN as string;

export default function PropertyMap({ properties }: any) {
  const mapContainer = useRef<HTMLDivElement | null>(null);
  const map = useRef<mapboxgl.Map | null>(null);

  useEffect(() => {
    if (map.current) return;

    map.current = new mapboxgl.Map({
      container: mapContainer.current!,
      style: "mapbox://styles/mapbox/streets-v12",
      center: [-0.7, 51.3], // Kent UK approx
      zoom: 9,
    });

    properties?.forEach((p: any) => {
      new mapboxgl.Marker()
        .setLngLat([p.lng, p.lat])
        .setPopup(
          new mapboxgl.Popup().setHTML(`
            <div>
              <h3>${p.title}</h3>
              <p>£${p.price}</p>
              <p>Score: ${p.deal_score || "N/A"}</p>
            </div>
          `)
        )
        .addTo(map.current!);
    });
  }, [properties]);

  return <div ref={mapContainer} style={{ height: "600px", width: "100%" }} />;
}
