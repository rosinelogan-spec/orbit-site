"""Builds the site pages from shared parts. Run: python3 build.py"""
import math

DESC = "Orbit turns your sleep, recovery and activity into a clear plan for today."
BETA_URL = "mailto:support@orbitrecovery.app?subject=Orbit%20beta"  # swap for the TestFlight public link


def page(path, title, description, body, current=""):
    depth = path.count("/")
    root = "../" * depth
    cur = ' aria-current="page"'
    nav = lambda href, label, key: f'<a href="{root}{href}"{cur if current == key else ""}>{label}</a>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#06070a">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="https://orbitrecovery.app/icon.png">
<meta property="og:url" content="https://orbitrecovery.app/{path.replace('index.html', '')}">
<link rel="icon" href="{root}favicon.png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="stylesheet" href="{root}styles.css">
</head>
<body>
<header class="site-header"><div class="wrap">
  <a class="brand" href="{root or './'}"><img src="{root}icon.png" alt="">Orbit</a>
  <nav class="nav">{nav('#features', 'Features', '') + nav('#pricing', 'Pricing', '') if not depth else nav('', 'Home', '')}{nav('privacy/', 'Privacy', 'privacy')}{nav('support/', 'Support', 'support')}</nav>
</div></header>
{body}
<footer><div class="wrap">
  <span>© 2026 Orbit · Health &amp; Recovery</span>
  <nav>{nav('privacy/', 'Privacy', '')}{nav('terms/', 'Terms', '')}{nav('support/', 'Support', '')}<a href="mailto:support@orbitrecovery.app">Contact</a></nav>
</div></footer>
</body>
</html>
"""


def rings():
    specs = [(118, 0.78, "#b9ceff", "#4f7bff"), (88, 0.66, "#d9ccff", "#8c6bff"), (58, 0.86, "#a6f7e6", "#1fc7a6")]
    defs, tracks, arcs = [], [], []
    for i, (r, fill, a, b) in enumerate(specs):
        c = 2 * math.pi * r
        defs.append(f'<linearGradient id="r{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>')
        tracks.append(f'<circle cx="150" cy="150" r="{r}" fill="none" stroke="rgba(255,255,255,.07)" stroke-width="22"/>')
        arcs.append(f'<circle class="arc" cx="150" cy="150" r="{r}" fill="none" stroke="url(#r{i})" stroke-width="22" stroke-linecap="round" stroke-dasharray="{c:.1f} {c:.1f}" style="--len:{c:.1f};--end:{c * (1 - fill):.1f}" transform="rotate(-90 150 150)"/>')
    return f'<svg class="rings" viewBox="0 0 300 300" role="img" aria-label="Readiness, Sleep and Stress rings"><defs>{"".join(defs)}</defs>{"".join(tracks)}{"".join(arcs)}</svg>'


FEATURES = [
    ("var(--blue)", "Readiness, Sleep &amp; Stress", "Three scores each morning built from your HRV, resting heart rate, sleep and recent training, with a plain-English read on what they mean."),
    ("var(--orange)", "A plan that fits your day", "Workout intensity matched to how recovered you are, a suggested time that works around your calendar, and reminders before it starts."),
    ("var(--pink)", "Food by photo or barcode", "Snap a meal and Orbit estimates the calories and macros, or scan a barcode. Group items into meals and look back at any day."),
    ("var(--purple)", "Sleep that tells the whole story", "Deep, REM and light sleep from your wearable, bedtime consistency, and a score that rewards good habits, not just hours."),
    ("var(--teal)", "A coach that knows your data", "Ask why you're tired, what to eat tonight or whether to train. Answers use your real numbers, not generic advice."),
    ("var(--gold)", "Progress you can feel", "Weight trends, cycle-aware insights, screen time, and achievements with tiers from Bronze to Master."),
]


PLANS = [
    ("", "In the app", "Monthly", "$9.99", "/month", "Billed monthly through the App Store", ["Most flexible: no yearly commitment", "Cancel anytime in Settings"]),
    ("", "In the app", "Annual", "$69.99", "/year", "$5.83/month, billed yearly", ["2 weeks free, then $69.99/year", "Save 42% vs monthly"]),
    ("best", "Best price", "Annual on our website", "$59.99", "/year", "$5/month, billed yearly", ["2 weeks free, then $59.99/year", "Save $10 vs the App Store", "Tap “Continue on website” in the app (US)"]),
]


def pricing():
    cards = "".join(
        f'<div class="plan {cls}"><span class="tag">{tag}</span><h3>{name}</h3>'
        f'<div class="price">{price}<small>{unit}</small></div><div class="per">{per}</div>'
        f'<ul>{"".join(f"<li>{b}</li>" for b in bullets)}</ul></div>'
        for cls, tag, name, price, unit, per, bullets in PLANS
    )
    return f"""
  <section id="pricing"><div class="wrap">
    <div class="section-head"><h2>Simple pricing, everything included</h2><p>Every plan unlocks all of Orbit: scores, food logging, the coach, journal insights and friends. Annual plans start with 2 weeks free.</p></div>
    <div class="plans">{cards}</div>
    <p class="plans-note">Prices in USD. Subscriptions renew automatically until you cancel; one free trial per person. See our <a href="terms/">Terms of Use</a>. Free for beta testers.</p>
  </div></section>"""


def home():
    cards = "".join(f'<div class="card"><div class="dot" style="color:{c}"></div><h3>{t}</h3><p>{d}</p></div>' for c, t, d in FEATURES)
    return page("index.html", "Orbit: Health & Recovery", DESC, f"""
<main>
  <div class="hero"><div class="wrap">
    {rings()}
    <span class="eyebrow">Now in beta on iPhone</span>
    <h1>Your body’s data,<br><span class="grad">turned into today’s plan.</span></h1>
    <p class="lede">Orbit reads your sleep, recovery and activity from Apple Health and your wearable, then tells you how hard to train, what to eat and when to wind down.</p>
    <div class="cta">
      <a class="btn btn-primary" href="{BETA_URL}">Join the beta</a>
      <a class="btn btn-ghost" href="#features">See what it does</a>
    </div>
    <p class="note">2 weeks free, then from $5/month · Free during the beta · iPhone first</p>
  </div></div>

  <section id="features"><div class="wrap">
    <div class="section-head"><h2>Everything in one calm place</h2><p>No more checking five apps to decide whether today is a rest day.</p></div>
    <div class="grid">{cards}</div>
  </div></section>

  <section><div class="wrap">
    <div class="section-head"><h2>Works with what you already wear</h2><p>Connect directly for the details your phone’s health app doesn’t get, like sleep stages and recovery scores.</p></div>
    <div class="devices">
      <span class="chip">Apple Health</span><span class="chip">WHOOP</span><span class="chip">Oura</span><span class="chip">Fitbit</span>
      <span class="chip">Polar <small>soon</small></span><span class="chip">Garmin <small>via Apple Health</small></span><span class="chip">Health Connect <small>Android</small></span>
    </div>
  </div></section>

{pricing()}

  <section class="privacy-band"><div class="wrap"><div class="card">
    <div><h2>Private by design</h2><p style="color:var(--muted);margin:14px 0 0">Your health data is yours. Orbit only uses it to build your plan.</p></div>
    <ul class="checks">
      <li><strong>Never sold</strong> or shared with advertisers.</li>
      <li><strong>Calendar stays on your phone.</strong> Event details are never uploaded.</li>
      <li><strong>Wearable logins stay on our server,</strong> never in the app, and disconnecting deletes the copied data.</li>
      <li><strong>Delete everything</strong> from the app, any time.</li>
    </ul>
  </div></div></section>
</main>""", "home")


def privacy():
    body = open("privacy/_body.html").read()
    return page("privacy/index.html", "Privacy Policy · Orbit", "How Orbit collects, uses and protects your data.", f'<main class="doc">{body}</main>', "privacy")


FAQ = [
    ("How do I connect my wearable?", "Open Orbit, go to Profile › Connected devices and tap your device. WHOOP, Oura and Fitbit connect directly. For Garmin and other watches, turn on Apple Health sharing in that watch’s app and Orbit reads it from there."),
    ("My steps or sleep look wrong.", "Orbit counts steps from one source per day so nothing is counted twice. If you have several devices, pick your main wearable in Profile › Connected devices. Also note Orbit’s day runs 4 AM to 4 AM, so late nights count toward the day before."),
    ("I forgot my password.", "On the sign-in screen, enter your email and tap “Forgot password?”. Open the email on your iPhone and tap Reset password to choose a new one."),
    ("I didn’t get my confirmation email.", "Check your spam folder for an email from noreply@orbitrecovery.app. Trying to sign in sends a fresh link if your email isn’t confirmed yet."),
    ("How much does Orbit cost?", "Orbit is $9.99 a month or $69.99 a year in the app, or $59.99 a year on our website (from the app, tap “Continue on website” on the plans screen). Annual plans start with 2 weeks free (one free trial per person)."),
    ("How do I cancel my subscription?", "If you subscribed in the app: on your iPhone, open Settings › your name › Subscriptions › Orbit › Cancel Subscription. If you subscribed on our website: in Orbit, go to Profile › Subscription › Open billing page and tap Cancel. You keep access until the end of the period you’ve paid for. Cancel at least 24 hours before a free trial ends to avoid being charged."),
    ("Can I get a refund?", "App Store purchases are refunded by Apple: request one at reportaproblem.apple.com. For website purchases, email us within 7 days of a charge you didn’t mean to make and we’ll refund it."),
    ("How do I delete my account and data?", "In Orbit, go to Profile › Delete account. This permanently deletes your account and everything stored with it. Data in Apple Health isn’t affected."),
    ("Is Orbit medical advice?", "No. Orbit gives general wellness suggestions. Talk to a healthcare professional before big changes to your diet or exercise."),
]


def support():
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
    return page("support/index.html", "Support · Orbit", "Help with Orbit: connecting devices, your account and your data.", f"""
<main class="doc">
  <h1>Support</h1>
  <p>Answers to common questions. Can’t find what you need? Email us and we’ll get back to you, usually within a day.</p>
  <div class="faq">{items}</div>
  <div class="contact-card">
    <p><strong>Contact us</strong><br>Questions, bugs or feature ideas are all welcome.</p>
    <a class="btn btn-primary" href="mailto:support@orbitrecovery.app">support@orbitrecovery.app</a>
  </div>
</main>""", "support")


def terms():
    body = open("terms/_body.html").read()
    return page("terms/index.html", "Terms of Use · Orbit", "The terms for using Orbit, including subscriptions and free trials.", f'<main class="doc">{body}</main>', "terms")


def welcome():
    # Where Stripe sends people after website checkout (and after the billing page).
    return page("welcome/index.html", "Welcome to Orbit", "Your Orbit subscription is ready.", """
<main class="doc" style="text-align:center">
  <h1 id="title" style="text-align:center">You’re all set 🎉</h1>
  <p id="text">Your Orbit subscription is ready. Head back to the app to get started.</p>
  <div class="cta" style="margin-top:28px;justify-content:center">
    <a class="btn btn-primary" href="healthapp://">Open Orbit</a>
  </div>
  <p class="note" style="margin-top:20px">If Orbit still shows the plans screen, tap “Already paid on the website? Tap to refresh”.</p>
</main>
<script>
  const q = new URLSearchParams(location.search);
  if (q.has('canceled')) {
    document.getElementById('title').textContent = 'No charge made';
    document.getElementById('text').textContent = 'Checkout was cancelled. You can go back to Orbit and choose a plan whenever you’re ready.';
  } else if (q.has('manage')) {
    document.getElementById('title').textContent = 'Billing updated';
    document.getElementById('text').textContent = 'Your changes are saved. Head back to Orbit.';
  }
</script>""", "")


def add_friend():
    return page("add/index.html", "Join me on Orbit", "A friend invited you to compete on Orbit.", f"""
<main class="doc" style="text-align:center">
  <h1 style="text-align:center">You’re invited 🏆</h1>
  <p>A friend wants to compete with you on Orbit: weekly goals and sleep leaderboards.</p>
  <p style="margin:28px 0 8px;color:var(--muted)">Friend code</p>
  <p id="code" style="font-size:40px;font-weight:800;letter-spacing:8px;margin:0">······</p>
  <div class="cta" style="margin-top:28px">
    <a class="btn btn-primary" id="open" href="healthapp://friends">Open in Orbit</a>
    <a class="btn btn-ghost" href="{BETA_URL}">Don’t have Orbit? Join the beta</a>
  </div>
  <p class="note" style="margin-top:20px">Already have Orbit? Tap Open in Orbit, or go to Friends and enter the code.</p>
</main>
<script>
  const code = (new URLSearchParams(location.search).get('code') || '').toUpperCase().replace(/[^A-Z0-9]/g, '').slice(0, 6);
  if (code) {{
    document.getElementById('code').textContent = code;
    const link = 'healthapp://friends?code=' + code;
    document.getElementById('open').href = link;
    // Try the app straight away; if it isn't installed the page just stays here.
    setTimeout(() => {{ location.href = link; }}, 300);
  }}
</script>""", "")


for path, html in [
    ("index.html", home()),
    ("privacy/index.html", privacy()),
    ("support/index.html", support()),
    ("add/index.html", add_friend()),
    ("terms/index.html", terms()),
    ("welcome/index.html", welcome()),
]:
    open(path, "w").write(html)
print("built")
