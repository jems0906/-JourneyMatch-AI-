export default function QualityDashboard({ quality }) {
  return (
    <section className="quality">
      <div><div className="eyebrow"><span /> LIVE QUALITY SIGNALS</div><h3>How the guide is learning</h3></div>
      <div className="quality-metrics">
        <div><strong>{quality?.average_satisfaction || "--"}</strong><span>avg satisfaction</span></div>
        <div><strong>{quality?.click_rate ? `${Math.round(quality.click_rate * 100)}%` : "--"}</strong><span>click rate</span></div>
        <div><strong>{quality?.save_rate ? `${Math.round(quality.save_rate * 100)}%` : "--"}</strong><span>save rate</span></div>
        <div><strong>{quality?.feedback_count || 0}</strong><span>responses</span></div>
      </div>
    </section>
  );
}
