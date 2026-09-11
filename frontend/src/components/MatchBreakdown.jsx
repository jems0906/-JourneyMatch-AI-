export default function MatchBreakdown({ breakdown }) {
  return (
    <div className="match-breakdown">
      {Object.entries(breakdown).map(([label, value]) => (
        <div className="match-row" key={label}>
          <div><span>{label}</span><strong>{value}%</strong></div>
          <div className="bar"><i style={{ width: `${value}%` }} /></div>
        </div>
      ))}
    </div>
  );
}
