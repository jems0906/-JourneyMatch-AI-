export default function MatchBar({ label, value }) {
  return <div className="match-row"><div><span>{label}</span><strong>{value}%</strong></div><div className="bar"><i style={{ width: `${value}%` }} /></div></div>;
}
