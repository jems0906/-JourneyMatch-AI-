import React from "react";
import { Compass, ShieldCheck } from "lucide-react";
import { createSession, deleteSession, getQualityDashboard, getRecommendations, submitFeedback } from "./api/client";
import RecommendationCard from "./components/RecommendationCard";
import PreferenceInput from "./components/PreferenceInput";
import PrivacyControls from "./components/PrivacyControls";
import FeedbackWidget from "./components/FeedbackWidget";
import DashboardPage from "./pages/DashboardPage";

export default function App() {
  const [sessionId, setSessionId] = React.useState("");
  const [prompt, setPrompt] = React.useState("I want a warm beach vacation in December, budget around $2000, flying from Atlanta, love food and culture, need wheelchair accessibility");
  const [preferences, setPreferences] = React.useState(null);
  const [recommendations, setRecommendations] = React.useState([]);
  const [loading, setLoading] = React.useState(false);
  const [rating, setRating] = React.useState(0);
  const [message, setMessage] = React.useState("");
  const [quality, setQuality] = React.useState(null);

  React.useEffect(() => { createSession().then((data) => setSessionId(data.session_id)); }, []);
  React.useEffect(() => { getQualityDashboard().then(setQuality).catch(() => {}); }, [recommendations, rating]);

  async function submit(event) {
    event.preventDefault();
    if (!sessionId || prompt.length < 8) return;
    setLoading(true); setMessage("");
    try {
      const data = await getRecommendations(sessionId, prompt);
      setPreferences(data.preferences);
      setRecommendations(data.recommendations);
    } catch {
      setMessage("The guide is taking a pause. Check that the backend is running.");
    } finally {
      setLoading(false);
    }
  }

  async function clearSession() {
    await deleteSession(sessionId);
    setPreferences(null);
    setRecommendations([]);
    setPrompt("");
    setMessage("Session cleared. Nothing from this trip was saved.");
    const data = await createSession();
    setSessionId(data.session_id);
  }

  async function sendRating(value) {
    setRating(value);
    await submitFeedback(sessionId, value);
  }

  return (
    <main>
      <nav>
        <a className="brand" href="/"><span className="brand-mark"><Compass size={22} /></span><span>JourneyMatch <em>AI</em></span></a>
        <div className="nav-note"><ShieldCheck size={16} /> Private by design</div>
      </nav>
      <section className="hero">
        <div className="eyebrow"><span /> PERSONALIZED TRAVEL, WITHOUT THE PROFILE</div>
        <h1>Tell us where<br /><i>your curiosity</i> leads.</h1>
        <p className="hero-copy">Describe the feeling, the season, the budget. We'll turn a few words into a trip that fits.</p>
        <PreferenceInput prompt={prompt} onChange={setPrompt} onSubmit={submit} loading={loading} />
        <PrivacyControls onClearSession={clearSession} />
      </section>
      {message && <p className="message">{message}</p>}
      {preferences && (
        <section className="results">
          <div className="results-heading">
            <div><div className="eyebrow"><span /> YOUR SHORTLIST</div><h2>Three places, <i>one good beginning.</i></h2></div>
            <div className="preference-chips">
              {preferences.climate && <span>{preferences.climate} climate</span>}
              {preferences.budget && <span>${preferences.budget.toLocaleString()} budget</span>}
              {preferences.interests?.slice(0, 3).map((interest) => <span key={interest}>{interest}</span>)}
            </div>
          </div>
          <div className="recommendations">
            {recommendations.map((recommendation, index) => <RecommendationCard key={recommendation.city} recommendation={recommendation} index={index} />)}
          </div>
          <FeedbackWidget rating={rating} onRate={sendRating} />
          <DashboardPage quality={quality} />
        </section>
      )}
      <footer><span>JourneyMatch AI · A privacy-first travel prototype</span><span>Recommendations are directional, not bookings.</span></footer>
    </main>
  );
}
