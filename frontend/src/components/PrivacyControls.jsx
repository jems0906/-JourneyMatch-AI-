import { ShieldCheck, Trash2 } from "lucide-react";

export default function PrivacyControls({ onClearSession }) {
  return (
    <div className="privacy-line">
      <ShieldCheck size={15} /> Your text is used for this session only <span>·</span>{" "}
      <button type="button" onClick={onClearSession}><Trash2 size={14} /> Clear session</button>
    </div>
  );
}
