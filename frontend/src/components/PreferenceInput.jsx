import { ArrowUpRight } from "lucide-react";

export default function PreferenceInput({ prompt, onChange, onSubmit, loading }) {
  return (
    <form onSubmit={onSubmit} className="prompt-box">
      <textarea aria-label="Describe your trip" value={prompt} onChange={(event) => onChange(event.target.value)} placeholder="I'm dreaming of..." />
      <div className="prompt-footer">
        <span>{prompt.length} / 2,000</span>
        <button type="submit" disabled={loading}>{loading ? "Finding..." : <>Find my matches <ArrowUpRight size={17} /></>}</button>
      </div>
    </form>
  );
}
