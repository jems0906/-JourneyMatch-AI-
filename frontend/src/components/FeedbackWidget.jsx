import { Star } from "lucide-react";

export default function FeedbackWidget({ rating, onRate }) {
  return (
    <div className="feedback">
      <div>
        <strong>Does this direction feel right?</strong>
        <span>Your feedback improves the guide, not a profile.</span>
      </div>
      <div className="stars">
        {[1, 2, 3, 4, 5].map((value) => (
          <button key={value} type="button" className={value <= rating ? "selected" : ""} onClick={() => onRate(value)} aria-label={`${value} stars`}>
            <Star size={20} fill="currentColor" />
          </button>
        ))}
      </div>
    </div>
  );
}
