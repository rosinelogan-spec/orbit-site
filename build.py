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


def ring(value, label, sub, color, fill):
    r = 22
    c = 2 * math.pi * r
    return (
        f'<div class="m-ring"><div class="m-dial"><svg viewBox="0 0 56 56"><circle cx="28" cy="28" r="{r}" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="6"/>'
        f'<circle cx="28" cy="28" r="{r}" fill="none" stroke="{color}" stroke-width="6" stroke-linecap="round" '
        f'stroke-dasharray="{c * fill:.1f} {c:.1f}" transform="rotate(-90 28 28)"/></svg>'
        f'<div class="m-val"><b>{value}</b><i style="color:{color}">{sub}</i></div></div><span>{label}</span></div>'
    )


def hero_phone():
    """An illustrated hand holding a phone that shows Orbit's Today screen."""
    rings_row = "".join([
        ring("82", "Readiness", "Ready", "#ae95ff", 0.82),
        ring("6.4k", "Steps", "of 8k", "#45e0c2", 0.8),
        ring("1,120", "Calories", "of 1,480", "#ff9f5a", 0.76),
        ring("48", "Water", "of 72 oz", "#7fd3ff", 0.66),
    ])
    tabs = "".join(
        f'<span class="{"on" if i == 0 else ""}"><em></em>{t}</span>'
        for i, t in enumerate(["Today", "Food", "Workout", "Sleep", "Profile"])
    )
    return f"""<div class="holder" aria-label="A hand holding an iPhone showing Orbit's Today screen" role="img">
      <svg class="hand-back" viewBox="0 0 360 760" aria-hidden="true">
        <defs>
          <linearGradient id="skin" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f1c3a0"/><stop offset="1" stop-color="#c88660"/></linearGradient>
          <linearGradient id="skinDark" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#b9774f"/><stop offset="1" stop-color="#d99a72"/></linearGradient>
          <linearGradient id="sleeve" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a2350"/><stop offset="1" stop-color="#15122b"/></linearGradient>
        </defs>
        <path d="M300 280 C340 280 352 330 350 420 C350 520 356 600 300 668 L290 760 L92 760 L98 690 C52 650 26 590 40 520 L120 400 Z" fill="url(#skin)"/>
        <g fill="url(#skinDark)">
          <rect x="318" y="290" width="40" height="42" rx="20"/>
          <rect x="320" y="334" width="40" height="44" rx="20"/>
          <rect x="320" y="380" width="38" height="42" rx="19"/>
          <rect x="318" y="424" width="36" height="38" rx="18"/>
        </g>
        <path d="M86 700 Q190 676 300 700 L304 760 L82 760 Z" fill="url(#sleeve)"/>
        <path d="M86 700 Q190 676 300 700" stroke="rgba(174,149,255,.5)" stroke-width="3" fill="none"/>
      </svg>
      <div class="phone"><div class="screen">
        <div class="m-status"><span>9:41</span><span class="m-island"></span><span class="m-icons"><i></i><i></i><i></i></span></div>
        <div class="m-date">Tuesday, November 17</div>
        <div class="m-title">Good morning, Alex</div>
        <div class="m-card m-rings">{rings_row}</div>
        <div class="m-card m-insight"><span class="m-label" style="color:#ae95ff">YOUR INSIGHT</span>
          <p>On days you work out, you sleep <b>34 min longer</b>.</p></div>
        <div class="m-tiles">
          <div class="m-card"><span class="m-label">CHECK-IN</span><b>How do you feel?</b></div>
          <div class="m-card"><span class="m-label">WEIGHT</span><b>148.6 lb</b></div>
        </div>
        <div class="m-card m-plan"><span class="m-label" style="color:#ff9f5a">TODAY’S WORKOUT</span>
          <b>Upper-body strength</b><span class="m-sub">~35 min · moderate · best at 5:30 PM</span></div>
        <img class="m-coach" src="coach-bubble.png" alt="">
        <div class="m-tabs">{tabs}</div>
      </div></div>
      <svg class="hand-front" viewBox="0 0 360 760" aria-hidden="true">
        <defs><linearGradient id="skin2" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#d48f66"/><stop offset="1" stop-color="#f3c8a6"/></linearGradient></defs>
        <g fill="url(#skin2)">
          <path d="M338 292 L322 292 C310 292 304 302 304 312 C304 322 310 332 322 332 L338 332 Z"/>
          <path d="M338 336 L320 336 C308 336 302 346 302 356 C302 367 308 377 320 377 L338 377 Z"/>
          <path d="M338 381 L321 381 C309 381 303 391 303 401 C303 411 309 421 321 421 L338 421 Z"/>
          <path d="M338 425 L324 425 C313 425 308 434 308 443 C308 452 313 461 324 461 L338 461 Z"/>
          <path transform="translate(-24 6)" d="M40 650 C26 600 34 556 58 520 C70 502 94 498 102 514 C110 530 98 548 88 566 C76 590 78 620 92 650 Z"/>
        </g>
        <g fill="rgba(255,238,226,.6)">
          <rect x="307" y="303" width="12" height="18" rx="6"/>
          <rect x="305" y="347" width="12" height="19" rx="6"/>
          <rect x="306" y="392" width="12" height="18" rx="6"/>
          <rect x="311" y="435" width="11" height="16" rx="5.5"/>
          <ellipse cx="60" cy="522" rx="10" ry="7" transform="rotate(-40 60 522)"/>
        </g>
        <g stroke="rgba(120,60,30,.25)" stroke-width="1.5" fill="none">
          <path d="M338 334 L322 334"/><path d="M338 379 L322 379"/><path d="M338 423 L323 423"/>
        </g>
      </svg>
    </div>"""


FEATURES = [
    ("var(--purple)", "Readiness, Sleep &amp; Stress", "Three scores every morning from your HRV, resting heart rate, sleep and recent training, with a plain-English read on what they mean for today."),
    ("var(--orange)", "A plan that fits your day", "Workout intensity matched to how recovered you are, a time that works around your calendar, and a bedtime that gets you the sleep you need."),
    ("var(--orange)", "Guided workouts", "Follow today’s workout set by set with rest timers. Don’t like an exercise? Swap it for one of 150+ from the library, matched to your equipment."),
    ("var(--pink)", "Food by photo or barcode", "Snap a meal and Orbit estimates the calories and macros, or scan a barcode. Group items into meals, save favorites and look back at any day."),
    ("var(--gold)", "Meal plans, recipes &amp; groceries", "Orbit plans up to a week of meals that hit your calories and protein, each with a recipe, and builds your grocery list sorted by aisle."),
    ("var(--teal)", "A coach that’s always there", "Tap the Orbit button on any screen to ask why you’re tired, what to eat tonight or whether to train. It can change your plan for you."),
    ("var(--blue)", "Insights only you have", "Orbit learns your patterns over weeks: what late meals do to your sleep, how workouts move your HRV, and your best and worst nights."),
    ("var(--teal)", "Groups &amp; challenges", "A weekly leaderboard with friends, plus short challenges for steps, sleep, recovery or workouts. You choose what’s shared."),
    ("var(--pink)", "Cycle-aware", "Track your cycle and see how each phase can affect mood, energy, cravings, training and sleep, right on your Today screen."),
]

MORE = ["Health Monitor", "Journal &amp; check-ins", "Water", "Fasting timer", "Weight trends", "Achievements", "Screen time", "Home Screen widgets", "Weekly recap"]


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
    <div class="section-head"><h2>Simple pricing, everything included</h2><p>Every plan unlocks all of Orbit: scores, food logging, meal plans, guided workouts, the coach, insights, groups and challenges. Annual plans start with 2 weeks free.</p></div>
    <div class="plans">{cards}</div>
    <p class="plans-note">Prices in USD. Subscriptions renew automatically until you cancel; one free trial per person. See our <a href="terms/">Terms of Use</a>. Free for beta testers.</p>
  </div></section>"""


def home():
    cards = "".join(f'<div class="card"><div class="dot" style="color:{c}"></div><h3>{t}</h3><p>{d}</p></div>' for c, t, d in FEATURES)
    return page("index.html", "Orbit: Health & Recovery", DESC, f"""
<main>
  <div class="hero"><div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="eyebrow">Now in beta on iPhone</span>
      <h1>Your body’s data,<br><span class="grad">turned into today’s plan.</span></h1>
      <p class="lede">Orbit reads your sleep, recovery and activity from Apple Health and your wearable, then tells you how hard to train, what to eat and when to wind down. And a coach is one tap away.</p>
      <div class="cta">
        <a class="btn btn-primary" href="{BETA_URL}">Join the beta</a>
        <a class="btn btn-ghost" href="#features">See what it does</a>
      </div>
      <p class="note">2 weeks free, then from $5/month · Free during the beta · iPhone first</p>
    </div>
    {hero_phone()}
  </div></div>

  <section id="features"><div class="wrap">
    <div class="section-head"><h2>Everything in one calm place</h2><p>Today, Food, Workout and Sleep, each with its own plan and history. No more checking five apps to decide whether today is a rest day.</p></div>
    <div class="grid">{cards}</div>
    <div class="more"><span>Also in Orbit</span>{"".join(f'<span class="chip">{m}</span>' for m in MORE)}</div>
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
      <li><strong>Insights are worked out on your phone,</strong> and your meal plan and grocery list stay there too.</li>
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
    return page("add/index.html", "Join my group on Orbit", "You've been invited to a group on Orbit.", f"""
<main class="doc" style="text-align:center">
  <h1 style="text-align:center">Join my group 👥</h1>
  <p id="lede">You’ve been invited to a group on Orbit: a weekly leaderboard and challenges for recovery, sleep, steps and workouts.</p>
  <p id="label" style="margin:28px 0 8px;color:var(--muted)">Group code</p>
  <p id="code" style="font-size:40px;font-weight:800;letter-spacing:8px;margin:0">······</p>
  <div class="cta" style="margin-top:28px">
    <a class="btn btn-primary" id="open" href="healthapp://groups">Open in Orbit</a>
    <a class="btn btn-ghost" href="{BETA_URL}">Don’t have Orbit? Join the beta</a>
  </div>
  <p id="hint" class="note" style="margin-top:20px">Already have Orbit? Tap Open in Orbit, or go to Profile › Groups and enter the code.</p>
</main>
<script>
  const q = new URLSearchParams(location.search);
  const clean = (v) => (v || '').toUpperCase().replace(/[^A-Z0-9]/g, '').slice(0, 6);
  const group = clean(q.get('group'));
  const code = group;
  if (group) {{
    document.querySelector('h1').textContent = 'Join my group 👥';
    document.getElementById('lede').textContent = 'You’ve been invited to a group on Orbit: a weekly leaderboard and challenges for recovery, sleep, steps and workouts.';
    document.getElementById('label').textContent = 'Group code';
    document.getElementById('hint').textContent = 'Already have Orbit? Tap Open in Orbit, or go to Profile › Groups and enter the code.';
  }}
  if (code) {{
    document.getElementById('code').textContent = code;
    // Old friend links (?code=) just open Groups: friends were replaced by groups.
    const link = group ? 'healthapp://groups?join=' + code : 'healthapp://groups';
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
