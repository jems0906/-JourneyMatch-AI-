export default function DestinationDetail({ recommendation }) {
  if (!recommendation) return null;
  return (
    <section className="destination-detail">
      <h2>{recommendation.city}<small>{recommendation.country}</small></h2>
      <p>{recommendation.description}</p>
      <div className="highlights">{recommendation.highlights.map((highlight) => <span key={highlight}>{highlight}</span>)}</div>
      <p><strong>Average cost:</strong> ${recommendation.avg_cost.toLocaleString()}</p>
      <p><strong>Accessibility:</strong> {recommendation.accessibility ? "Accessible" : "Not confirmed accessible"}</p>
    </section>
  );
}
