#!/usr/bin/env python3
"""Generates the four site pages from one shared shell, so the header,
navigation and contact rail stay identical across pages.

Run:  python3 build.py
Then commit the generated .html files. (You can also just edit the .html
files directly and delete this script — it exists to keep the shared
parts in sync while the site is young.)"""

from icons import ICONS

ORCID = "0000-0002-3756-6097"   # <-- replace with your real ORCID iD

NAV = [
    ("index.html", "About"),
    ("research.html", "Research"),
    ("publications.html", "Publications"),
    ("conservation.html", "ML for conservation"),
]

LINKS = [
    ("pin",      "Piemonte, Italy", None),
    ("mail",     "Email",     "mailto:enrico.picco@hotmail.it"),
    ("github",   "GitHub",    "https://github.com/e-picco"),
    ("linkedin", "LinkedIn",  "https://www.linkedin.com/in/enrico-picco/"),
    ("scholar",  "Scholar",   "https://scholar.google.com/citations?user=zZwpqk8AAAAJ&hl=en"),
    ("orcid",    "ORCID",     f"https://orcid.org/{ORCID}"),
]


def icon(name):
    return (f'<svg class="ic" viewBox="0 0 24 24" aria-hidden="true">'
            f'<path d="{ICONS[name]}"/></svg>')


def rail():
    rows = []
    for name, label, href in LINKS:
        inner = f'{icon(name)}<span>{label}</span>'
        rows.append(f'<a href="{href}">{inner}</a>' if href
                    else f'<div>{inner}</div>')
    return f"""    <aside class="rail">
      <img class="portrait" src="portrait.jpg" alt="Enrico Picco">
      <h2 class="rail-name">Enrico Picco, PhD</h2>
      <p class="role">Machine learning for ecology and biodiversity</p>
      <div class="meta">
{chr(10).join('        ' + r for r in rows)}
      </div>
    </aside>"""


def page(slug, title, description, main):
    nav = "\n".join(
        f'      <a href="{h}"{" aria-current=\"page\"" if h == slug else ""}>{t}</a>'
        for h, t in NAV)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="style.css">
</head>
<body>

<header class="masthead">
  <div class="masthead-inner">
    <a class="brand" href="index.html">Enrico Picco</a>
    <nav class="site-nav">
{nav}
    </nav>
  </div>
</header>

<div class="wrap">
{rail()}

    <main>
{main}
    </main>

  <footer>&copy; 2026 Enrico Picco</footer>
</div>
</body>
</html>
"""


PAGES = {}

PAGES["index.html"] = dict(
    title="Enrico Picco — Machine learning for ecology and biodiversity",
    description="Enrico Picco, PhD — machine learning engineer working on applied AI for ecology, biodiversity and environmental data.",
    main="""      <h1>About</h1>
      <p class="lede">I build machine learning systems for real-world signals, and I am moving that work toward ecology and biodiversity.</p>

      <p>I hold a PhD in machine learning from the Universit&eacute; libre de Bruxelles, where I spent four years building audio and video recognition systems end to end &mdash; model design, training, benchmarking &mdash; and taking them out of simulation onto physical hardware that had to process live sensor signals in real time. That work produced five peer-reviewed papers and took me to IBM Research Zurich and imec as a visiting researcher.</p>

      <p>Then I spent a year in Latin America, volunteering with conservation projects in remote parts of Honduras, Nicaragua, Peru and Bolivia: night surveys with pitfall and camera traps, nesting data for river turtles, anti-poaching patrols. It put me at the collection end of ecological data for the first time, and it is the reason I now work on conservation technology.</p>

      <p>What I am after is the overlap: rigorous machine learning applied to problems with an environmental purpose, with enough fieldwork in it that I understand where the data comes from.</p>

      <p class="note">Italian and Belgian citizen. I work in Italian, English, Spanish and French.</p>""")

PAGES["research.html"] = dict(
    title="Research — Enrico Picco",
    description="Doctoral and visiting research: machine learning for audio and video recognition running in real time on physical hardware.",
    main="""      <h1>Research</h1>
      <p class="lede">My doctoral work sat between machine learning, electronics and physics: neural networks that run as physical systems rather than as code on a GPU. Four themes, each with published results.</p>

      <section>
        <p class="eyebrow">Audio</p>
        <h3>Real-time speech recognition on a physical neural network</h3>
        <p>Spoken-digit classification running on an optoelectronic system in real time, with a deep architecture whose layers were connected analogically rather than digitally &mdash; a first for this class of hardware. I designed the models, built the processing chain, and benchmarked accuracy against the digital equivalent.</p>
        <p class="note">This is the thread that connects most directly to bioacoustics: variable-length audio, noisy channels, classification under tight latency budgets.</p>
      </section>

      <section>
        <p class="eyebrow">Computer vision</p>
        <h3>High-speed human action recognition in video</h3>
        <p>The first implementation of video action classification on a physical reservoir computer, covering the full pipeline: human detection, pose estimation, feature extraction and classification, at frame rates a conventional implementation could not reach.</p>
      </section>

      <section>
        <p class="eyebrow">Method</p>
        <h3>Optimising physical neural networks with a delayed input</h3>
        <p>Physical learning systems are awkward to tune because their internal parameters are not freely accessible. We showed that manipulating the input signal in time alone is enough to optimise performance, which removes most of the need for hardware redesign. Published in <em>Nature Communications Engineering</em>.</p>
      </section>

      <section>
        <p class="eyebrow">Hardware</p>
        <h3>Data acquisition and control systems</h3>
        <p>All of the above needed an acquisition layer that did not exist: FPGA designs interfacing analog optical signals with digital processing, plus the instrumentation and control systems around them. I extended the same work as a visiting researcher at IBM Research Zurich, driving a photonic neuromorphic accelerator, and at imec Ghent, applying neural models to non-linear channel equalisation in optical telecoms.</p>
        <p class="note">Practically: I am comfortable with sensors, embedded systems and messy real-world signal acquisition, not only with clean datasets.</p>
      </section>

      <section>
        <p class="eyebrow">Context</p>
        <h3>POST-DIGITAL</h3>
        <p>My PhD was part of POST-DIGITAL, a European doctoral network on next-generation computing linking academic and industrial partners across several countries. It is where I learned to work as the technical translator between people who do not share a vocabulary &mdash; and where I found I like that role.</p>
      </section>""")

PAGES["publications.html"] = dict(
    title="Publications — Enrico Picco",
    description="Peer-reviewed publications and conference presentations by Enrico Picco.",
    main="""      <h1>Publications</h1>
      <p class="lede">Five peer-reviewed journal articles and nine conference presentations. Full list on <a href="https://scholar.google.com/citations?user=zZwpqk8AAAAJ&amp;hl=en">Google Scholar</a>.</p>

      <section>
        <p class="eyebrow">Peer-reviewed journals</p>

        <div class="pub">
          <strong>Picco, E.</strong>, Jaurigue, L., L&uuml;dge, K. &amp; Massar, S. Efficient optimisation of physical reservoir computers using only a delayed input. <span class="venue">Nature Communications Engineering</span> 4(1), 3 (2025).
          <div class="links"><a href="https://doi.org/10.1038/s44172-025-00340-6">DOI</a></div>
        </div>

        <div class="pub">
          <strong>Picco, E.</strong>, Lupo, A. &amp; Massar, S. Deep photonic reservoir computer for speech recognition. <span class="venue">IEEE Transactions on Neural Networks and Learning Systems</span> 36(4), 7606&ndash;7614 (2024).
          <div class="links"><a href="https://doi.org/10.1109/TNNLS.2024.3400451">DOI</a></div>
        </div>

        <div class="pub">
          Abreu, S., Boikov, I., Goldmann, M., Jonuzi, T., Lupo, A., Masaad, S., Nguyen, L., <strong>Picco, E.</strong>, et al. A photonics perspective on computing with physical substrates. <span class="venue">Reviews in Physics</span> 100093 (2024).
          <div class="links"><a href="#">DOI</a><!-- add the real DOI --></div>
        </div>

        <div class="pub">
          Lupo, A., <strong>Picco, E.</strong>, Zajnulina, M. &amp; Massar, S. Deep photonic reservoir computer based on frequency multiplexing with fully analog connection between layers. <span class="venue">Optica</span> 10(11), 1478&ndash;1485 (2023).
          <div class="links"><a href="#">DOI</a><!-- add the real DOI --></div>
        </div>

        <div class="pub">
          <strong>Picco, E.</strong>, Antonik, P. &amp; Massar, S. High speed human action recognition using a photonic reservoir computer. <span class="venue">Neural Networks</span> 165, 662&ndash;675 (2023).
          <div class="links"><a href="https://doi.org/10.1016/j.neunet.2023.06.014">DOI</a></div>
        </div>
      </section>

      <section>
        <p class="eyebrow">Selected conference presentations</p>

        <div class="pub">
          <strong>Picco, E.</strong> &amp; Massar, S. Real-time photonic deep reservoir computing for speech recognition. <span class="venue">IJCNN 2023</span>, Gold Coast, Australia.
          <div class="links"><a href="https://doi.org/10.1109/IJCNN54540.2023.10191786">DOI</a></div>
        </div>

        <div class="pub">
          <strong>Picco, E.</strong>, Jaurigue, L., L&uuml;dge, K. &amp; Massar, S. Use of a delayed input for simple and effective optimisation of physical reservoir computers. <span class="venue">SPIE Optics + Photonics 2024</span>, San Diego, USA.
        </div>

        <div class="pub">
          <strong>Picco, E.</strong>, Antonik, P. &amp; Massar, S. Time-multiplexed photonic reservoir computer for recognition of human actions in videos. <span class="venue">CLEO Europe 2023</span>, Munich, Germany.
        </div>

        <p class="note">Also presented at NNPC (Hanover), ECML-PKDD (Turin), IEEE Benelux Photonics (Eindhoven), BePOM (Brussels) and JNOG (Nice).</p>
      </section>

      <section>
        <p class="eyebrow">Thesis</p>
        <div class="pub">
          Optoelectronic reservoir computing: human action recognition, deep architectures, optimisation with delayed inputs. PhD thesis, Universit&eacute; libre de Bruxelles (2024). European Doctorate label. Supervisor: Prof. Serge Massar.
        </div>
      </section>""")

PAGES["conservation.html"] = dict(
    title="ML for conservation &amp; biodiversity — Enrico Picco",
    description="Applied machine learning for conservation: bioacoustic monitoring, computer vision for wildlife, and field data collection in Latin America.",
    main="""      <h1>ML for conservation &amp; biodiversity</h1>
      <p class="lede">Where I am taking the technical work, and how I got here.</p>

      <section>
        <div class="entry">
          <div class="when">2026&ndash;<br>present</div>
          <div>
            <h3>Conservation Mind</h3>
            <p class="where">Technical contributor, applied AI &mdash; volunteer, remote</p>
            <p>Machine learning support for a distributed conservation-technology group. I am involved in scoping and technical discussion across active projects, which include bioacoustic monitoring, GIS-based monitoring of small-scale fisheries in the Philippines, and computer vision for individual identification of big cats.</p>
            <!-- As soon as a specific contribution is yours to describe, replace the
                 sentence above with it: what you evaluated, what you recommended,
                 what changed as a result. Named and specific beats broad every time. -->
          </div>
        </div>

        <div class="entry">
          <div class="when">2025&ndash;<br>2026</div>
          <div>
            <h3>Field data collection</h3>
            <p class="where">Tapiche Reserve (Peru) &middot; Aquicuana Reserve / Sustainable Bolivia &middot; field time in Honduras and Nicaragua</p>
            <p>During a year travelling in Latin America I volunteered with non-profit conservation projects in remote parts of the Amazon and Central America: nightly biodiversity surveys with pitfall-trap transects and camera-trap stations, nesting records for taricaya river turtles, anti-poaching patrols, and science-education activities for children in neighbouring communities.</p>
            <p>It is the part of my background I expected least and use most. Enough time on the collection side to understand why ecological field data arrives inconsistent: rotating observers, patchy spatial coverage, no connectivity, equipment that fails in humidity. Models that ignore this are accurate on paper and useless in the field.</p>
          </div>
        </div>
      </section>

      <section>
        <p class="eyebrow">Notes</p>
        <h3>Writing</h3>
        <p>Short technical pieces on machine learning for biodiversity monitoring &mdash; what the current tooling does well, where it breaks, and what the field-data side looks like from inside.</p>
        <ul>
          <li><em>Pretrained audio encoders for animal sound: what they actually learn.</em> [draft]</li>
          <li><em>Notes from the collection end: why ecological datasets are messier than they look.</em> [draft]</li>
        </ul>
        <p class="note">Replace the placeholders above with real links as you publish them, or delete this section until the first piece is live. Two written pieces do more for this page than a list of intentions.</p>
      </section>

      <section>
        <p class="eyebrow">Transferable</p>
        <h3>From the PhD</h3>
        <p>Four years of audio and video classification transfers more directly than the hardware framing suggests: variable-length audio under noise, benchmark design and honest evaluation, distinguishing a real result from an artefact, and getting models to run on constrained devices in real time rather than only in a notebook. See <a href="research.html">Research</a>.</p>
      </section>

      <section>
        <p class="eyebrow">Open to</p>
        <h3>What I am looking for</h3>
        <p>Applied machine learning roles with an environmental purpose &mdash; bioacoustics, camera-trap and remote-sensing pipelines, biodiversity monitoring platforms &mdash; with enough fieldwork in them that I stay close to where the data comes from. Based in Piemonte, and happy to travel.</p>
        <p class="note">Get in touch: <a href="mailto:enrico.picco@hotmail.it">enrico.picco@hotmail.it</a></p>
      </section>""")


for slug, cfg in PAGES.items():
    with open(slug, "w", encoding="utf-8") as f:
        f.write(page(slug, cfg["title"], cfg["description"], cfg["main"]))
    print("wrote", slug)
