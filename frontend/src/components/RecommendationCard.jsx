import { Sparkles } from "lucide-react";
import MatchBar from "./MatchBar";

export default function RecommendationCard({ recommendation, index }) {
  return <article className={`recommendation-card card-${index}`}>
    <div className="card-top"><span className="rank">0{index + 1}</span><span>{recommendation.airport}</span></div>
    <h3>{recommendation.city}<small>{recommendation.country}</small></h3>
    <p>{recommendation.description}</p>
    <div className="highlights">{recommendation.highlights.map((highlight) => <span key={highlight}>{highlight}</span>)}</div>
    <div className="match-label"><span>Match score</span><strong>{recommendation.score}%</strong></div>
    <div className="matches"><MatchBar label="Budget fit" value={recommendation.breakdown.budget} /><MatchBar label="Climate" value={recommendation.breakdown.climate} /><MatchBar label="Interests" value={recommendation.breakdown.interests} /></div>
    <div className="why"><Sparkles size={16} /><span>{recommendation.explanation}</span></div>
  </article>;
}
