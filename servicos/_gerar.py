#!/usr/bin/env python3
import os, urllib.parse

WA = "5527998805559"

def wa(msg): return f"https://wa.me/{WA}?text={urllib.parse.quote(msg)}"

def page(slug, name, icon_svg, tagline, headline, sub, problem_title, problem, solution_title, solution, includes, steps, faq, wa_msg):
    wlink = wa(wa_msg)
    inc_items = "".join(f"""
          <li class="inc-item">
            <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
            {item}
          </li>""" for item in includes)
    step_cards = "".join(f"""
        <div class="step-card reveal" data-step="0{i+1}">
          <h3>{s['t']}</h3>
          <p>{s['d']}</p>
        </div>""" for i,s in enumerate(steps))
    faq_items = "".join(f"""
        <div class="faq-item">
          <button class="faq-q" onclick="toggleFaq(this)">
            {q}
            <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>
          </button>
          <div class="faq-a"><p>{a}</p></div>
        </div>""" for q,a in faq)

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} — Audace</title>
  <meta name="description" content="{sub}">
  <link rel="stylesheet" href="../style.css">
  <style>
    .svc-hero {{
      min-height: 78vh;
      display: flex;
      align-items: center;
      padding: 140px 48px 80px;
      background: var(--black);
      position: relative;
      overflow: hidden;
    }}
    .svc-hero::before {{
      content: '';
      position: absolute;
      top: -100px; right: -100px;
      width: 600px; height: 600px;
      background: radial-gradient(circle, rgba(140,140,140,0.07) 0%, transparent 65%);
      pointer-events: none;
    }}
    .svc-hero-inner {{
      max-width: 1200px;
      margin: 0 auto;
      width: 100%;
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 60px;
      align-items: center;
    }}
    .svc-hero-icon {{
      width: 100px; height: 100px;
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 32px;
      color: var(--silver-light);
    }}
    .svc-hero-icon svg {{ width: 48px; height: 48px; }}
    .svc-tagline {{
      font-family: var(--font-head);
      font-size: 10px;
      font-weight: 700;
      letter-spacing: .3em;
      text-transform: uppercase;
      color: var(--silver-dark);
      margin-bottom: 18px;
    }}
    .svc-hero h1 {{
      font-family: var(--font-head);
      font-weight: 900;
      font-size: clamp(38px, 5.5vw, 72px);
      line-height: 1.0;
      letter-spacing: -.03em;
      color: var(--white-pure);
      margin-bottom: 20px;
    }}
    .svc-hero p {{
      font-size: 17px;
      line-height: 1.72;
      color: var(--silver-dark);
      max-width: 560px;
      margin-bottom: 40px;
    }}
    .svc-hero-badge {{
      background: rgba(255,255,255,0.03);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: var(--radius-lg);
      padding: 36px 40px;
      min-width: 280px;
      text-align: center;
      flex-shrink: 0;
    }}
    .badge-val {{
      font-family: var(--font-head);
      font-weight: 900;
      font-size: 52px;
      letter-spacing: -.03em;
      background: var(--grad-silver);
      background-size: 200% auto;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: shine 5s linear infinite;
    }}
    .badge-lbl {{
      font-family: var(--font-head);
      font-size: 11px;
      font-weight: 600;
      letter-spacing: .16em;
      text-transform: uppercase;
      color: var(--silver-dark);
      margin-top: 6px;
    }}
    .problem-solution {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2px;
      background: var(--gray-border);
      border-radius: var(--radius-lg);
      overflow: hidden;
      border: 1px solid var(--gray-border);
      margin-top: 56px;
    }}
    .ps-card {{
      background: var(--gray-deep);
      padding: 56px 52px;
    }}
    .ps-label {{
      font-family: var(--font-head);
      font-size: 10px;
      font-weight: 700;
      letter-spacing: .28em;
      text-transform: uppercase;
      color: var(--silver-dark);
      margin-bottom: 20px;
    }}
    .ps-card h3 {{
      font-family: var(--font-head);
      font-size: 26px;
      font-weight: 800;
      letter-spacing: -.015em;
      color: var(--white-pure);
      margin-bottom: 16px;
    }}
    .ps-card p {{
      font-size: 15px;
      line-height: 1.75;
      color: var(--silver-dark);
    }}
    .includes-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px 32px;
      margin-top: 40px;
    }}
    .inc-item {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 14px;
      color: var(--silver-light);
      padding: 12px 0;
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }}
    .inc-item svg {{ color: var(--silver); flex-shrink:0; }}
    .steps-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      margin-top: 56px;
    }}
    .step-card {{
      background: rgba(255,255,255,0.025);
      border: 1px solid rgba(255,255,255,0.07);
      border-radius: var(--radius-lg);
      padding: 40px 32px;
      position: relative;
    }}
    .step-card::before {{
      content: attr(data-step);
      font-family: var(--font-head);
      font-size: 10px;
      font-weight: 700;
      letter-spacing: .25em;
      color: var(--silver-dark);
      display: block;
      margin-bottom: 20px;
    }}
    .step-card h3 {{
      font-family: var(--font-head);
      font-size: 17px;
      font-weight: 800;
      color: var(--white-pure);
      margin-bottom: 10px;
    }}
    .step-card p {{ font-size: 14px; line-height: 1.68; color: var(--silver-dark); }}
    .faq-item {{
      border-bottom: 1px solid var(--gray-border);
    }}
    .faq-q {{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 22px 0;
      background: none;
      border: none;
      cursor: pointer;
      font-family: var(--font-head);
      font-size: 16px;
      font-weight: 600;
      color: var(--white-pure);
      text-align: left;
      gap: 16px;
    }}
    .faq-q svg {{ flex-shrink:0; transition: transform .3s; }}
    .faq-q.open svg {{ transform: rotate(180deg); }}
    .faq-a {{
      max-height: 0;
      overflow: hidden;
      transition: max-height .4s var(--ease-out);
    }}
    .faq-a.open {{ max-height: 300px; }}
    .faq-a p {{
      font-size: 15px;
      line-height: 1.72;
      color: var(--silver-dark);
      padding-bottom: 22px;
    }}
    .cta-svc {{
      background: var(--gray-deep);
      border-top: 1px solid var(--gray-border);
      padding: 120px 48px;
      text-align: center;
      position: relative;
      overflow: hidden;
    }}
    .cta-svc::before {{
      content: '';
      position: absolute;
      top: 50%; left: 50%;
      transform: translate(-50%,-50%);
      width: 700px; height: 500px;
      background: radial-gradient(ellipse, rgba(140,140,140,0.06) 0%, transparent 65%);
      pointer-events: none;
    }}
    .cta-svc h2 {{
      font-family: var(--font-head);
      font-weight: 900;
      font-size: clamp(36px, 5vw, 68px);
      line-height: 1.05;
      letter-spacing: -.03em;
      color: var(--white-pure);
      margin-bottom: 16px;
      position: relative;
    }}
    .cta-svc p {{
      font-size: 17px;
      line-height: 1.68;
      color: var(--silver-dark);
      max-width: 440px;
      margin: 0 auto 48px;
      position: relative;
    }}
    .back-link {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-head);
      font-size: 11px;
      font-weight: 600;
      letter-spacing: .12em;
      text-transform: uppercase;
      color: var(--silver-dark);
      margin-bottom: 40px;
      transition: color .25s;
    }}
    .back-link:hover {{ color: var(--white-pure); }}
    @media (max-width:900px) {{
      .svc-hero-inner {{ grid-template-columns: 1fr; }}
      .svc-hero-badge {{ display: none; }}
      .problem-solution {{ grid-template-columns: 1fr; }}
      .steps-grid {{ grid-template-columns: repeat(2,1fr); }}
      .includes-grid {{ grid-template-columns: 1fr; }}
    }}
    @media (max-width:600px) {{
      .svc-hero {{ padding: 120px 24px 60px; }}
      .steps-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <div id="cursor"></div>
  <div id="cursor-ring"></div>
  <div id="scroll-progress"></div>

  <nav id="nav">
    <a href="../index.html" class="nav-logo">
      <svg class="logo-mark" viewBox="0 0 100 96" xmlns="http://www.w3.org/2000/svg">
        <defs><linearGradient id="gnav" x1="10%" y1="0%" x2="90%" y2="100%"><stop offset="0%" stop-color="#ffffff"/><stop offset="50%" stop-color="#d0d0d0"/><stop offset="100%" stop-color="#909090"/></linearGradient></defs>
        <polygon points="49,4 62,4 27,92 14,92" fill="url(#gnav)"/>
        <polygon points="62,4 71,4 57,43 48,43" fill="url(#gnav)"/>
        <polygon points="59,53 68,53 84,92 71,92" fill="url(#gnav)"/>
      </svg>
      <span class="logo-text">AUDACE</span>
    </a>
    <ul class="nav-links">
      <li><a href="../index.html#servicos">Serviços</a></li>
      <li><a href="../index.html#diferenciais">Diferenciais</a></li>
      <li><a href="../index.html#processo">Processo</a></li>
      <li><a href="../index.html#depoimentos">Clientes</a></li>
    </ul>
    <a href="{wlink}" class="btn-nav" target="_blank" rel="noopener">Fale Conosco</a>
  </nav>

  <!-- HERO -->
  <section class="svc-hero">
    <div class="svc-hero-inner">
      <div>
        <a href="../index.html#servicos" class="back-link">
          <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 12H5M12 5l-7 7 7 7"/></svg>
          Todos os serviços
        </a>
        <div class="svc-hero-icon">
          {icon_svg}
        </div>
        <div class="svc-tagline">{tagline}</div>
        <h1 class="reveal">{headline}</h1>
        <p class="reveal">{sub}</p>
        <div class="reveal" style="display:flex;gap:14px;flex-wrap:wrap;">
          <a href="{wlink}" class="btn-whatsapp" target="_blank" rel="noopener">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            Quero saber mais
          </a>
          <a href="../index.html#servicos" class="btn-ghost">Ver outros serviços</a>
        </div>
      </div>
      <div class="svc-hero-badge reveal-right">
        <div class="badge-val">+250</div>
        <div class="badge-lbl">Clientes Atendidos</div>
        <div style="margin-top:24px;padding-top:24px;border-top:1px solid var(--gray-border);">
          <div class="badge-val" style="font-size:36px;">R$7M+</div>
          <div class="badge-lbl">Em Vendas Geradas</div>
        </div>
      </div>
    </div>
  </section>

  <!-- PROBLEM + SOLUTION -->
  <section class="section" style="background:var(--gray-deep);">
    <div style="max-width:1200px;margin:0 auto;">
      <div class="problem-solution">
        <div class="ps-card reveal-left">
          <div class="ps-label">O Problema</div>
          <h3>{problem_title}</h3>
          <p>{problem}</p>
        </div>
        <div class="ps-card reveal-right" style="background:var(--gray-mid);">
          <div class="ps-label">A Solução</div>
          <h3>{solution_title}</h3>
          <p>{solution}</p>
        </div>
      </div>
    </div>
  </section>

  <!-- INCLUDES -->
  <section class="section">
    <div style="max-width:1200px;margin:0 auto;">
      <p class="section-label reveal">O que está incluso</p>
      <h2 class="section-title reveal">Tudo que você precisa para <span class="gradient-text">crescer.</span></h2>
      <ul class="includes-grid">{inc_items}
      </ul>
    </div>
  </section>

  <!-- STEPS -->
  <section class="section dot-grid" style="background:var(--gray-deep);">
    <div style="max-width:1200px;margin:0 auto;">
      <p class="section-label reveal">Como funciona</p>
      <h2 class="section-title reveal">Processo claro, <span class="gradient-text">resultado previsível.</span></h2>
      <div class="steps-grid">{step_cards}
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section">
    <div style="max-width:800px;margin:0 auto;">
      <p class="section-label reveal">Dúvidas frequentes</p>
      <h2 class="section-title reveal" style="margin-bottom:48px;">Perguntas <span class="gradient-text">e respostas.</span></h2>
      {faq_items}
    </div>
  </section>

  <!-- CTA -->
  <section class="cta-svc">
    <div style="position:relative;z-index:2;max-width:700px;margin:0 auto;">
      <p class="section-label reveal" style="justify-content:center;">Pronto para começar</p>
      <h2 class="reveal">{name} que<br><span class="gradient-text">gera resultado real.</span></h2>
      <p class="reveal">Fale agora com um especialista. Sem compromisso — apenas uma conversa honesta sobre o que o marketing pode fazer pelo seu negócio.</p>
      <div class="reveal" style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">
        <a href="{wlink}" class="btn-whatsapp" target="_blank" rel="noopener">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
          Falar pelo WhatsApp
        </a>
        <a href="../index.html" class="btn-ghost">Voltar ao início</a>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer>
    <div style="max-width:1200px;margin:0 auto;">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="nav-logo" style="margin-bottom:16px;">
            <svg class="logo-mark" viewBox="0 0 100 96" xmlns="http://www.w3.org/2000/svg">
              <defs><linearGradient id="gft2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#c8c8c8"/><stop offset="100%" stop-color="#787878"/></linearGradient></defs>
              <polygon points="49,4 62,4 27,92 14,92" fill="url(#gft2)"/>
              <polygon points="62,4 71,4 57,43 48,43" fill="url(#gft2)"/>
              <polygon points="59,53 68,53 84,92 71,92" fill="url(#gft2)"/>
            </svg>
            <span class="logo-text" style="font-size:17px;">AUDACE</span>
          </div>
          <p>Audácia com estratégia.<br>Marketing com propósito.</p>
        </div>
        <div class="footer-col">
          <h4>Serviços</h4>
          <a href="trafego-pago.html">Tráfego Pago</a>
          <a href="social-media.html">Redes Sociais</a>
          <a href="branding.html">Branding</a>
          <a href="producao-conteudo.html">Produção</a>
        </div>
        <div class="footer-col">
          <h4>Mais serviços</h4>
          <a href="email-marketing.html">E-mail Marketing</a>
          <a href="seo.html">SEO</a>
          <a href="consultoria.html">Consultoria</a>
          <a href="automacao-crm.html">Automação & CRM</a>
        </div>
        <div class="footer-col">
          <h4>Contato</h4>
          <a href="https://wa.me/{WA}" target="_blank">WhatsApp</a>
          <a href="mailto:contato@audace.com.br">E-mail</a>
          <a href="https://instagram.com/audace" target="_blank">Instagram</a>
          <a href="https://linkedin.com/company/audace" target="_blank">LinkedIn</a>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2025 Audace. Todos os direitos reservados.</p>
        <p>Feito com audácia — ES, Brasil 🇧🇷</p>
      </div>
    </div>
  </footer>

  <script>
  (()=>{{
    const cur=document.getElementById('cursor'),ring=document.getElementById('cursor-ring');
    let mx=0,my=0,rx=0,ry=0;
    document.addEventListener('mousemove',e=>{{mx=e.clientX;my=e.clientY;cur.style.left=mx+'px';cur.style.top=my+'px';}});
    (function lp(){{rx+=(mx-rx)*.13;ry+=(my-ry)*.13;ring.style.left=rx+'px';ring.style.top=ry+'px';requestAnimationFrame(lp);}})();
    document.querySelectorAll('a,button').forEach(el=>{{
      el.addEventListener('mouseenter',()=>{{cur.style.transform='translate(-50%,-50%) scale(2.5)';ring.style.opacity='0';}});
      el.addEventListener('mouseleave',()=>{{cur.style.transform='translate(-50%,-50%) scale(1)';ring.style.opacity='1';}});
    }});
    const nav=document.getElementById('nav'),prog=document.getElementById('scroll-progress');
    window.addEventListener('scroll',()=>{{nav.classList.toggle('scrolled',scrollY>40);prog.style.width=(scrollY/(document.body.scrollHeight-innerHeight)*100)+'%';}},{{passive:true}});
    const obs=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('visible');obs.unobserve(e.target);}}}})  ,{{threshold:.1}});
    document.querySelectorAll('.reveal,.reveal-up,.reveal-left,.reveal-right').forEach(el=>obs.observe(el));
  }})();
  function toggleFaq(btn){{
    const a=btn.nextElementSibling;
    btn.classList.toggle('open');
    a.classList.toggle('open');
  }}
  </script>
</body>
</html>"""

# ── ICONS ──
ICONS = {
  'trafego-pago': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2" fill="currentColor" stroke="none"/><line x1="12" y1="2" x2="12" y2="4"/><line x1="12" y1="20" x2="12" y2="22"/><line x1="2" y1="12" x2="4" y2="12"/><line x1="20" y1="12" x2="22" y2="12"/></svg>',
  'social-media': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg>',
  'branding': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l2.4 7.4H22l-6.2 4.5 2.4 7.4L12 17l-6.2 4.3 2.4-7.4L2 9.4h7.6z"/></svg>',
  'producao-conteudo': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg>',
  'email-marketing': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>',
  'seo': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/><path d="M8 11h6M11 8v6"/></svg>',
  'consultoria': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>',
  'automacao-crm': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M15 2v2M15 20v2M9 2v2M9 20v2M2 15h2M20 15h2M2 9h2M20 9h2"/></svg>',
}

# ── SERVICE DEFINITIONS ──
services = [
  dict(
    slug='trafego-pago', name='Tráfego Pago',
    tagline='Cada centavo investido, rastreado',
    headline='Pare de queimar verba.<br>Comece a investir em clientes.',
    sub='Campanhas com precisão cirúrgica em Google, Meta, TikTok e YouTube. Segmentadas para quem realmente compra — não para quem só clica.',
    problem_title='Você está pagando por cliques que não convertem.',
    problem='A maioria das empresas gasta mais de 40% do orçamento em anúncios mal configurados, segmentações rasas e criativos fracos. O dinheiro sai, mas o cliente não entra. Você sente que está jogando no escuro.',
    solution_title='A Audace entrega campanhas que transformam cliques em receita.',
    solution='Auditamos suas campanhas atuais, eliminamos o desperdício e escalamos o que converte. Criativos que param o scroll, segmentações avançadas e otimização semanal — com relatórios transparentes que mostram exatamente onde cada real está trabalhando.',
    includes=['Auditoria completa da conta','Pesquisa de palavras-chave e audiências','Criação de criativos (copy + arte)','Configuração de pixel e conversões','Testes A/B contínuos','Campanhas em Google, Meta, TikTok ou YouTube','Otimização semanal','Relatório mensal com ROI detalhado'],
    steps=[
      dict(t='Diagnóstico',d='Auditamos suas campanhas atuais e identificamos exatamente onde o orçamento está sendo desperdiçado.'),
      dict(t='Estratégia',d='Definimos canais, audiências, orçamento e metas. Um plano de ataque com direção clara.'),
      dict(t='Execução',d='Criamos criativos, configuramos pixels e lançamos campanhas otimizadas desde o primeiro dia.'),
      dict(t='Escala',d='Monitoramos, testamos e escalamos o que funciona. Você vê o resultado em números reais.'),
    ],
    faq=[
      ('Quanto preciso investir em anúncios para começar?','Trabalhamos com investimentos a partir de R$1.500/mês em mídia. O mais importante é que cada real seja investido com estratégia — não jogado às cegas.'),
      ('Em quanto tempo vejo resultados?','As primeiras semanas são de aprendizado e otimização. Resultados consistentes geralmente aparecem entre 30 e 60 dias, dependendo do ticket médio e do setor.'),
      ('Vocês trabalham com quais plataformas?','Google Ads, Meta Ads (Facebook e Instagram), TikTok Ads, YouTube Ads e LinkedIn Ads. Recomendamos as plataformas certas para o seu negócio.'),
      ('O que diferencia a gestão da Audace?','Não gerenciamos campanhas no piloto automático. Cada conta tem atenção personalizada, com otimizações semanais e relatórios mensais que vão além do básico.'),
    ],
    wa_msg='Olá! Vim pelo site da Audace e tenho interesse em saber mais sobre Tráfego Pago para minha empresa. Poderia me dar mais informações?',
  ),
  dict(
    slug='social-media', name='Gestão de Redes Sociais',
    tagline='Presença que conecta, conteúdo que converte',
    headline='Sua marca não pode ser<br>mais um perfil no feed.',
    sub='Nas redes sociais, quem não gera conexão, gera irrelevância. Criamos estratégias de conteúdo que posicionam sua marca como autoridade e transformam seguidores em clientes.',
    problem_title='Você posta, mas ninguém engaja — e seu concorrente está crescendo.',
    problem='Publicar sem estratégia é como gritar num quarto vazio. Sem consistência, posicionamento claro e conhecimento do algoritmo, sua marca fica invisível — enquanto concorrentes menores conquistam o espaço que deveria ser seu.',
    solution_title='A Audace transforma sua presença digital em máquina de oportunidades.',
    solution='Criamos estratégias de conteúdo baseadas no seu público, no algoritmo de cada plataforma e nos seus objetivos de negócio. Do planejamento à publicação, do engajamento ao relatório — cuidamos de tudo para que você foque em vender.',
    includes=['Planejamento estratégico mensal','Calendário editorial personalizado','Criação de conteúdo (copy + design)','Produção de reels e vídeos curtos','Gestão de comentários e DMs','Hashtags e SEO de perfil','Análise de concorrência','Relatório mensal de performance'],
    steps=[
      dict(t='Briefing',d='Mapeamos seu negócio, público-alvo, tom de voz e objetivos. Sem essa base, não há estratégia.'),
      dict(t='Planejamento',d='Criamos o calendário editorial do mês com temas, formatos e frequência ideal para cada plataforma.'),
      dict(t='Produção',d='Desenvolvemos os conteúdos — copy, arte, vídeo — com qualidade e consistência visual.'),
      dict(t='Monitoramento',d='Acompanhamos o desempenho, respondemos comentários e ajustamos o que não está performando.'),
    ],
    faq=[
      ('Em quais plataformas vocês trabalham?','Instagram, TikTok, LinkedIn, Facebook e YouTube. Recomendamos focar nas plataformas onde seu público realmente está.'),
      ('Quantas publicações por semana?','Depende da estratégia e do plano escolhido. Trabalhamos com frequências que equilibram qualidade e consistência.'),
      ('Vocês criam os vídeos também?','Sim. Nossa equipe produz reels, vídeos curtos e conteúdo em vídeo dentro da estratégia de conteúdo.'),
      ('Preciso aprovar os conteúdos antes de publicar?','Sim. Todo o conteúdo passa pela sua aprovação. Você tem controle total sobre o que vai ao ar.'),
    ],
    wa_msg='Olá! Vim pelo site da Audace e tenho interesse em Gestão de Redes Sociais para minha empresa. Poderia me dar mais informações?',
  ),
  dict(
    slug='branding', name='Branding & Identidade Visual',
    tagline='Marcas que são reconhecidas antes de falar',
    headline='Uma marca sem identidade<br>é uma promessa sem rosto.',
    sub='Antes de vender, você precisa ser reconhecido, lembrado e desejado. Construímos identidades visuais que comunicam o que você é — antes mesmo de qualquer palavra ser dita.',
    problem_title='Sua marca parece genérica — e o cliente não sente motivo para escolher você.',
    problem='Num mercado lotado, a diferença entre ser lembrado e ser ignorado está na identidade. Sem um posicionamento claro, uma identidade visual coerente e uma promessa de marca forte, você compete apenas por preço. Isso é uma armadilha.',
    solution_title='A Audace cria marcas que dominam a percepção antes da primeira venda.',
    solution='Desenvolvemos a estratégia de marca completa: posicionamento, naming, identidade visual (logo, paleta, tipografia, padrões) e brandbook. Uma marca que atrai, retém e converte — porque comunica valor antes do preço.',
    includes=['Estratégia de posicionamento','Naming e tagline','Criação de logotipo e símbolo','Paleta de cores e tipografia','Manual de identidade visual (brandbook)','Aplicações em materiais (cartão, apresentação, social)','Identidade para redes sociais','Arquivos em todos os formatos'],
    steps=[
      dict(t='Imersão',d='Entendemos profundamente seu negócio, seu público e seus diferenciais. Branding sem estratégia é só estética.'),
      dict(t='Conceito',d='Desenvolvemos o posicionamento, a promessa de marca e a direção criativa antes de qualquer execução visual.'),
      dict(t='Criação',d='Desenhamos a identidade visual completa com refinamentos até o resultado perfeito.'),
      dict(t='Entrega',d='Brandbook completo, arquivos em todos os formatos e orientações de uso para manter a consistência.'),
    ],
    faq=[
      ('Qual o prazo para criar uma identidade visual?','O processo completo dura entre 3 e 6 semanas, dependendo da complexidade e das revisões.'),
      ('Posso pedir revisões no logo?','Sim. Trabalhamos com rodadas de revisão para garantir que o resultado final seja exatamente o que você precisa.'),
      ('O que está incluso no brandbook?','Logo e variações, paleta de cores, tipografia, ícones, padrões, exemplos de aplicação e regras de uso.'),
      ('Vocês fazem rebranding de marcas existentes?','Sim. Trabalhamos tanto com criação do zero quanto com atualização e modernização de marcas existentes.'),
    ],
    wa_msg='Olá! Vim pelo site da Audace e tenho interesse em Branding & Identidade Visual para minha empresa. Poderia me dar mais informações?',
  ),
  dict(
    slug='producao-conteudo', name='Produção de Conteúdo',
    tagline='Conteúdo que para o scroll e converte',
    headline='Conteúdo que vende<br>enquanto você trabalha.',
    sub='Vídeos, fotos e reels de alto impacto que capturam atenção em segundos e traduzem sua mensagem em linguagem visual irresistível — do planejamento ao produto final.',
    problem_title='Seu conteúdo está invisível porque parece amador ou genérico.',
    problem='Em um feed onde todos brigam pela mesma atenção, conteúdo mediano é pior do que nada. Imagens escuras, vídeos sem corte, copy fraca — cada peça assim reforça uma percepção negativa da sua marca. E o cliente simplesmente passa adiante.',
    solution_title='A Audace produz conteúdo que representa o real valor da sua marca.',
    solution='Nossa equipe de produção cria peças visuais estratégicas — com direção de arte, roteiro, edição e copy — que param o scroll, comunicam valor e geram ação. Conteúdo que você tem orgulho de publicar.',
    includes=['Planejamento editorial e roteiros','Produção fotográfica profissional','Produção e edição de vídeos','Reels e shorts para redes sociais','Motion graphics e animações','Tratamento e edição fotográfica','Copy estratégica para cada peça','Entrega em todos os formatos e resoluções'],
    steps=[
      dict(t='Briefing',d='Entendemos seus objetivos, sua marca e o que você precisa comunicar em cada peça.'),
      dict(t='Roteiro e direção',d='Criamos roteiros, storyboards e direção de arte antes de qualquer produção.'),
      dict(t='Produção',d='Fotografamos, filmamos e editamos com equipe especializada e equipamentos profissionais.'),
      dict(t='Entrega',d='Conteúdos prontos para publicação em todos os formatos — para feed, stories, reels e anúncios.'),
    ],
    faq=[
      ('Vocês vão até o meu negócio para produzir?','Sim. Realizamos produções no local quando necessário, além de produções em estúdio conforme o projeto.'),
      ('Qual o volume de conteúdo entregue por mês?','Varia conforme o plano. Trabalhamos desde pacotes pontuais até entregas mensais recorrentes.'),
      ('Posso usar o conteúdo em anúncios também?','Sim. Produzimos conteúdos otimizados tanto para conteúdo orgânico quanto para uso em campanhas pagas.'),
      ('Os vídeos têm legenda e edição completa?','Sim. Entregamos os vídeos completamente editados, com legenda, trilha e adaptação para cada plataforma.'),
    ],
    wa_msg='Olá! Vim pelo site da Audace e tenho interesse em Produção de Conteúdo para minha empresa. Poderia me dar mais informações?',
  ),
  dict(
    slug='email-marketing', name='E-mail Marketing',
    tagline='O canal com maior ROI do marketing digital',
    headline='4.200% de ROI.<br>O canal que sua concorrência ignora.',
    sub='E-mail marketing bem feito é a arma secreta de marcas que faturam no automático. Sequências que nutrem leads, reativam clientes inativos e vendem enquanto você dorme.',
    problem_title='Você tem uma lista de contatos — mas ela está esquecida e esfriando.',
    problem='Uma lista de e-mails sem estratégia é dinheiro parado. Disparos aleatórios sem segmentação, sem automação e sem cópia persuasiva resultam em descadastros e spam. Você perde o ativo mais valioso do marketing digital.',
    solution_title='A Audace transforma sua lista em máquina de receita recorrente.',
    solution='Criamos sequências automatizadas que guiam o lead desde o primeiro contato até a compra — e além. E-mails de boas-vindas, nutrição, abandono de carrinho, reativação e pós-venda. Cópia que converte e design que entrega na caixa de entrada.',
    includes=['Estratégia e arquitetura de funil de e-mail','Criação de fluxos de automação','Copywriting de alta conversão','Design de templates responsivos','Segmentação e personalização avançada','Integração com CRM e plataformas (RD Station, Mailchimp, Klaviyo)','Testes A/B de assunto e conteúdo','Relatórios de abertura, clique e conversão'],
    steps=[
      dict(t='Auditoria',d='Analisamos sua lista atual, suas plataformas e seus fluxos existentes para identificar oportunidades.'),
      dict(t='Estratégia',d='Desenhamos a arquitetura do funil de e-mail — cada sequência com objetivo, gatilho e timing definidos.'),
      dict(t='Criação',d='Escrevemos os e-mails, criamos o design e configuramos as automações na sua plataforma.'),
      dict(t='Otimização',d='Testamos assuntos, horários e conteúdos continuamente para maximizar abertura e conversão.'),
    ],
    faq=[
      ('Qual plataforma de e-mail vocês utilizam?','Trabalhamos com as principais: RD Station, Mailchimp, ActiveCampaign, Klaviyo e HubSpot. Também ajudamos na migração se necessário.'),
      ('Minha lista está "fria". Ainda vale a pena?','Sim. Criamos campanhas de reativação específicas para listas que não recebem e-mails há muito tempo.'),
      ('Quantos e-mails são enviados por mês?','Depende da estratégia e do funil desenhado. O foco é qualidade e timing — não volume.'),
      ('Como evitam que os e-mails caiam no spam?','Configuramos corretamente o SPF, DKIM e DMARC do seu domínio, além de seguirmos as melhores práticas de entregabilidade.'),
    ],
    wa_msg='Olá! Vim pelo site da Audace e tenho interesse em E-mail Marketing para minha empresa. Poderia me dar mais informações?',
  ),
  dict(
    slug='seo', name='SEO & Presença Orgânica',
    tagline='Seja encontrado quando mais importa',
    headline='Apareça no Google<br>quando seu cliente procura você.',
    sub='Enquanto você dorme, o Google trabalha por você. Otimizamos seu site e conteúdo para conquistar as primeiras posições nas buscas que mais convertem — sem depender de anúncios.',
    problem_title='Você está invisível para quem já quer comprar o que você vende.',
    problem='Se seu site não aparece nas primeiras posições do Google, você está perdendo clientes todos os dias para concorrentes que investiram em SEO. Pior: o tráfego orgânico que você poderia ter é gratuito e qualificado — e você está deixando na mesa.',
    solution_title='A Audace posiciona sua marca no topo das buscas que importam.',
    solution='Auditamos e otimizamos todos os aspectos do seu site — técnico, on-page e off-page. Criamos uma estratégia de conteúdo baseada em palavras-chave de alta intenção de compra. Construímos autoridade de domínio para resultados duradouros.',
    includes=['Auditoria técnica completa do site','Pesquisa de palavras-chave estratégicas','Otimização on-page (títulos, meta, headings, imagens)','Estratégia de conteúdo SEO','Criação de conteúdo otimizado','Link building e construção de autoridade','Otimização de velocidade e Core Web Vitals','Relatório mensal de posicionamento e tráfego'],
    steps=[
      dict(t='Auditoria',d='Diagnosticamos todos os problemas técnicos e de conteúdo que estão impedindo seu site de rankear.'),
      dict(t='Estratégia',d='Definimos as palavras-chave prioritárias e o plano de conteúdo baseado na intenção de busca do seu cliente.'),
      dict(t='Otimização',d='Implementamos as melhorias técnicas, otimizamos as páginas existentes e criamos novo conteúdo.'),
      dict(t='Autoridade',d='Construímos backlinks de qualidade e consolidamos a autoridade do domínio para rankings duradouros.'),
    ],
    faq=[
      ('Em quanto tempo aparecem os resultados de SEO?','SEO é um investimento de médio prazo. Resultados significativos geralmente aparecem entre 3 e 6 meses. Mas o tráfego cresce continuamente sem custo adicional.'),
      ('SEO é melhor que tráfego pago?','São complementares. O tráfego pago dá resultados imediatos; o SEO cria um ativo que gera tráfego gratuito por anos. O ideal é usar os dois.'),
      ('Vocês também otimizam para Google Meu Negócio?','Sim. SEO local e Google Meu Negócio fazem parte da estratégia para negócios com presença física.'),
      ('Como funciona a criação de conteúdo para SEO?','Identificamos os tópicos e palavras-chave de maior oportunidade e produzimos artigos, páginas e conteúdos otimizados para posicionar sua marca como autoridade.'),
    ],
    wa_msg='Olá! Vim pelo site da Audace e tenho interesse em SEO & Presença Orgânica para minha empresa. Poderia me dar mais informações?',
  ),
  dict(
    slug='consultoria', name='Consultoria Estratégica',
    tagline='Clareza para escalar com inteligência',
    headline='Chega de ações soltas<br>sem direção.',
    sub='Você não precisa de mais táticas — precisa de estratégia. Nossa consultoria mapeia sua situação atual, define prioridades e entrega um plano de marketing executável baseado em dados.',
    problem_title='Você investe em marketing, mas não sabe o que está funcionando.',
    problem='Sem uma estratégia clara, você acaba espalhando recursos em várias frentes ao mesmo tempo — e não consegue escalar nenhuma delas. Cada mês é uma tentativa diferente, sem aprendizado acumulado, sem direção.',
    solution_title='A Audace entrega clareza estratégica para você escalar com inteligência.',
    solution='Realizamos um diagnóstico completo da sua operação de marketing: canais, funil, posicionamento, concorrência e métricas. A partir daí, entregamos um plano estratégico com prioridades claras, canais validados e ações ordenadas por impacto.',
    includes=['Diagnóstico completo da operação de marketing','Análise de concorrência e posicionamento','Mapeamento do funil de vendas atual','Definição de personas e ICP','Plano estratégico com prioridades de 90 dias','Seleção e recomendação de canais','Definição de KPIs e metas realistas','Sessões de alinhamento e acompanhamento'],
    steps=[
      dict(t='Diagnóstico',d='Analisamos tudo: canais ativos, campanhas, posicionamento, concorrência e métricas atuais.'),
      dict(t='Imersão',d='Realizamos entrevistas com seu time e clientes para entender gargalos e oportunidades que os dados não mostram.'),
      dict(t='Plano estratégico',d='Entregamos um documento com diagnóstico, prioridades, canais recomendados, metas e próximos passos.'),
      dict(t='Acompanhamento',d='Sessões de check-in para garantir que o plano está sendo executado e ajustado conforme o cenário evolui.'),
    ],
    faq=[
      ('Consultoria é para que tamanho de empresa?','Desde MEIs e pequenas empresas até negócios de médio porte que querem estruturar ou escalar seu marketing.'),
      ('Vocês acompanham a execução depois?','Sim. Podemos seguir como parceiros de execução após a consultoria, implementando as estratégias definidas.'),
      ('Quanto tempo dura a consultoria?','O processo de diagnóstico e entrega do plano dura de 2 a 4 semanas. O acompanhamento pode ser contínuo.'),
      ('A consultoria é presencial ou online?','Online. Realizamos as sessões por videoconferência com toda a documentação compartilhada digitalmente.'),
    ],
    wa_msg='Olá! Vim pelo site da Audace e tenho interesse em Consultoria Estratégica de Marketing. Poderia me dar mais informações?',
  ),
  dict(
    slug='automacao-crm', name='Automação & CRM',
    tagline='Seu funil no piloto automático',
    headline='Escale sem contratar.<br>Atenda sem parar.',
    sub='Automatize sua operação de marketing e vendas com inteligência. Implantamos CRMs, fluxos de automação e integrações que colocam seu funil no piloto automático.',
    problem_title='Você perde leads por falta de follow-up. Todo dia.',
    problem='Sem automação, cada lead depende de uma ação manual — e ações manuais falham. Leads sem follow-up rápido resfriam, oportunidades somem e o time de vendas se sobrecarrega com tarefas repetitivas que poderiam ser automatizadas.',
    solution_title='A Audace coloca sua operação de marketing no piloto automático.',
    solution='Implantamos e configuramos seu CRM, criamos fluxos de automação que nutrem e qualificam leads automaticamente, e integramos todas as suas ferramentas. Do primeiro contato até o pós-venda — sem depender de memória ou planilha.',
    includes=['Implantação e configuração de CRM','Mapeamento e automação do funil de vendas','Criação de fluxos de nutrição automáticos','Integração de ferramentas (WhatsApp, e-mail, ads)','Qualificação automática de leads','Automação de follow-up e pós-venda','Dashboards de acompanhamento','Treinamento da equipe'],
    steps=[
      dict(t='Mapeamento',d='Entendemos seu funil atual, suas ferramentas e onde estão os gargalos de operação.'),
      dict(t='Implantação',d='Configuramos o CRM, criamos os pipelines e integramos com suas plataformas de marketing.'),
      dict(t='Automação',d='Desenvolvemos os fluxos automáticos de nutrição, follow-up e qualificação de leads.'),
      dict(t='Treinamento',d='Capacitamos seu time para operar o sistema e acompanhamos a adoção nas primeiras semanas.'),
    ],
    faq=[
      ('Quais CRMs vocês trabalham?','HubSpot, RD Station, Pipedrive, ActiveCampaign, Zoho CRM e outros. Recomendamos o melhor para o seu perfil.'),
      ('Minha empresa já tem um CRM. Vocês trabalham com o que temos?','Sim. Otimizamos e automatizamos CRMs existentes que não estão sendo usados ao máximo.'),
      ('A automação substitui minha equipe de vendas?','Não. Ela elimina tarefas repetitivas e garante que nenhum lead seja esquecido — liberando sua equipe para focar em fechar negócios.'),
      ('Vocês integram WhatsApp ao CRM?','Sim. Configuramos a integração com WhatsApp Business API para que as conversas sejam centralizadas e automatizadas.'),
    ],
    wa_msg='Olá! Vim pelo site da Audace e tenho interesse em Automação & CRM para minha empresa. Poderia me dar mais informações?',
  ),
]

out_dir = os.path.dirname(os.path.abspath(__file__))
for s in services:
    html = page(
        slug=s['slug'], name=s['name'],
        icon_svg=ICONS[s['slug']],
        tagline=s['tagline'], headline=s['headline'], sub=s['sub'],
        problem_title=s['problem_title'], problem=s['problem'],
        solution_title=s['solution_title'], solution=s['solution'],
        includes=s['includes'], steps=s['steps'], faq=s['faq'],
        wa_msg=s['wa_msg'],
    )
    path = os.path.join(out_dir, f"{s['slug']}.html")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✓ {s['slug']}.html")

print("\nTodas as páginas geradas!")
