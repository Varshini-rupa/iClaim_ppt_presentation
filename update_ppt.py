import os
import re

filepath = r'c:\Users\HP\OneDrive\Desktop\project\iClaim_ppt_presentation\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Architecture Slide (Slide 4)
# We will use regex to find the s4 section and replace it
s4_pattern = re.compile(r'<!-- ══ SLIDE 4: ARCHITECTURE ══════════════════════════════════ -->.*?<!-- ══ SLIDE 5: AI ENGINE ═════════════════════════════════════ -->', re.DOTALL)

s4_new = """<!-- ══ SLIDE 4: ARCHITECTURE ══════════════════════════════════ -->
        <section class="slide" id="s4">
            <div class="eyebrow an-1">Slide 4 — Enterprise Architecture</div>
            <div class="slide-title an-2">END-TO-END <span>SYSTEM LIFECYCLE</span></div>
            <div style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
                <div class="slide-sub an-3" style="margin-bottom: 0;">9-Layer Architecture Mapped to the Claim Journey</div>
                <button class="an-3" id="btn-reshape-s4" style="padding: 6px 14px; font-size: 11px; font-weight: 700; border-radius: var(--radius-sm); background: var(--blue); color: #ffffff; border: none; cursor: pointer; display: flex; align-items: center; gap: 6px; box-shadow: 0 2px 6px rgba(26,41,128,0.15); transition: var(--trans);" onclick="toggleReshapeArchitecture()">
                    <span>↕️ Reshape Layout</span>
                </button>
            </div>
            <div class="divider an-3"></div>
            
            <div class="arch-split-container an-4"
                style="display: flex; gap: 24px; align-items: start; margin-top: 20px;">
                <div class="arch-image-side"
                    style="flex: 1.4; max-width: 60%; height: 440px; background: #ffffff; border-radius: var(--radius); border: 1px solid var(--border); padding: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); display: flex; align-items: center; justify-content: center;">
                    <img src="./project_architecture.png" alt="9-Layer Architecture"
                        style="width: 100%; height: 100%; object-fit: contain; display: block; border-radius: var(--radius-sm); cursor: zoom-in;"
                        onclick="openImageModal(this.src)" />
                </div>
                <div class="arch-layers-side"
                    style="flex: 1; display: flex; flex-direction: column; gap: 12px; max-width: 40%;">
                    <div class="arch-layer" style="border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; display: flex;">
                        <div class="arch-label l-pres" style="min-width: 120px; padding: 12px 10px; font-size: 12px; font-weight: 700; background: rgba(21, 101, 216, 0.15); display: flex; align-items: center;">🖥️ Presentation</div>
                        <div class="arch-content" style="flex: 1; padding: 10px 12px; display: flex; gap: 8px; flex-wrap: wrap; background: var(--glass);">
                            <span class="tag tag-blue" style="font-size: 10px; padding: 4px 8px;">Customer</span>
                            <span class="tag tag-blue" style="font-size: 10px; padding: 4px 8px;">Hospital</span>
                            <span class="tag tag-blue" style="font-size: 10px; padding: 4px 8px;">Reviewer</span>
                        </div>
                    </div>
                    <div class="arch-layer" style="border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; display: flex;">
                        <div class="arch-label l-biz" style="min-width: 120px; padding: 12px 10px; font-size: 12px; font-weight: 700; background: rgba(18, 200, 160, 0.15); display: flex; align-items: center;">⚙️ Business API</div>
                        <div class="arch-content" style="flex: 1; padding: 10px 12px; display: flex; gap: 8px; flex-wrap: wrap; background: var(--glass);">
                            <span class="tag tag-teal" style="font-size: 10px; padding: 4px 8px;">FastAPI</span>
                            <span class="tag tag-teal" style="font-size: 10px; padding: 4px 8px;">Claims Router</span>
                        </div>
                    </div>
                    <div class="arch-layer" style="border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; display: flex;">
                        <div class="arch-label l-ai" style="min-width: 120px; padding: 12px 10px; font-size: 12px; font-weight: 700; background: rgba(245, 158, 11, 0.15); display: flex; align-items: center;">🧠 AI Layer</div>
                        <div class="arch-content" style="flex: 1; padding: 10px 12px; display: flex; gap: 8px; flex-wrap: wrap; background: var(--glass);">
                            <span class="tag tag-amber" style="font-size: 10px; padding: 4px 8px;">OCR</span>
                            <span class="tag tag-amber" style="font-size: 10px; padding: 4px 8px;">spaCy RAG</span>
                            <span class="tag tag-amber" style="font-size: 10px; padding: 4px 8px;">ML Ensemble</span>
                        </div>
                    </div>
                    <div class="arch-layer" style="border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; display: flex;">
                        <div class="arch-label l-data" style="min-width: 120px; padding: 12px 10px; font-size: 12px; font-weight: 700; background: rgba(220, 38, 38, 0.12); display: flex; align-items: center;">🗄️ Data</div>
                        <div class="arch-content" style="flex: 1; padding: 10px 12px; display: flex; gap: 8px; flex-wrap: wrap; background: var(--glass);">
                            <span class="tag tag-red" style="font-size: 10px; padding: 4px 8px;">SQLite</span>
                            <span class="tag tag-red" style="font-size: 10px; padding: 4px 8px;">VectorStore</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ══ SLIDE 5: AI ENGINE ═════════════════════════════════════ -->"""
if s4_pattern.search(content):
    content = s4_pattern.sub(s4_new, content)
else:
    print("Could not find Slide 4")

# 2. Update Slides 8, add 9, 10
s8_pattern = re.compile(r'<!-- ══ SLIDE 8: ROADMAP ══════════════════════════════════════ -->.*?</div>\s*</section>\s*<!-- ══ HIDDEN DEMO ═════════════════════════════════════════ -->.*?</section>', re.DOTALL)

s8_new = """<!-- ══ SLIDE 8: DEMO ══════════════════════════════════════════ -->
        <section class="slide" id="s8">
            <div class="eyebrow an-1">Slide 8 — Product Demo</div>
            <div class="slide-title an-2">iCLAIM <span>IN ACTION</span></div>
            <div class="slide-sub an-3">Live Walkthrough of the Pre-Assessment Engine</div>
            <div class="divider an-3"></div>
            <div class="video-wrap an-4">
                <video controls poster="">
                    <source src="./project_demo.mp4" type="video/mp4">
                    <div
                        style="background:#111;padding:60px;text-align:center;color:#888;font-family:monospace;font-size:14px">
                        Video not found. Please place your MP4 at <code style="color:#12C8A0">./project_demo.mp4</code>
                    </div>
                </video>
            </div>
            <div class="demo-note an-5" style="text-align: center;">Press Space to Play/Pause, Left/Right to seek 5s</div>
        </section>

        <!-- ══ SLIDE 9: ROADMAP ══════════════════════════════════════ -->
        <section class="slide" id="s9">
            <div class="eyebrow an-1">Slide 9 — Strategic Future</div>
            <div class="slide-title an-2">FUTURE ROADMAP: <span>SCALING TO ENTERPRISE</span></div>
            <div class="slide-sub an-3">Evolving the MVP into a Comprehensive AI Claim Ecosystem</div>
            <div class="divider an-3"></div>
            
            <div class="roadmap-grid an-4" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 12px;">
                <div class="road-card">
                    <div class="road-icon">🏥</div>
                    <div class="road-title">Core System Integration</div>
                    <div class="road-desc">Deep integration with Hospital Information Systems (HIS/EHR) and Insurance Policy Management APIs for zero-touch document ingestion.</div>
                </div>
                <div class="road-card">
                    <div class="road-icon">🛡️</div>
                    <div class="road-title">Advanced Fraud Analytics</div>
                    <div class="road-desc">Network-based fraud detection across hospitals and agents. Enhanced OCR models to detect image tampering and forged medical bills.</div>
                </div>
                <div class="road-card">
                    <div class="road-icon">🤖</div>
                    <div class="road-title">Agentic AI Copilot</div>
                    <div class="road-desc">Autonomous AI agents that can proactively query missing data from hospitals, explain policy decisions to users, and recommend actions.</div>
                </div>
                <div class="road-card">
                    <div class="road-icon">☁️</div>
                    <div class="road-title">Cloud Native Deployment</div>
                    <div class="road-desc">Migration to AWS/Azure for horizontal scalability, high availability, and robust disaster recovery for enterprise workloads.</div>
                </div>
                <div class="road-card">
                    <div class="road-icon">📱</div>
                    <div class="road-title">Mobile Ecosystem</div>
                    <div class="road-desc">Dedicated iOS/Android applications with real-time push notifications, offline mode, and on-device secure document scanning.</div>
                </div>
                <div class="road-card">
                    <div class="road-icon">🌐</div>
                    <div class="road-title">Expanded Multilingual</div>
                    <div class="road-desc">Scaling beyond Telugu and English to support 15+ regional languages with localized dialect awareness and real-time voice translation.</div>
                </div>
            </div>
            <div class="s1-footer an-5" style="margin-top: 24px; padding-top: 16px;">
                    <div class="footer-left">
                        <span class="footer-label">PRESENTED BY</span>
                        <span class="footer-value">TEAM 15</span>
                    </div>
                    <div class="footer-divider"></div>
                    <div class="footer-right">
                        <span class="footer-label">POWERED BY</span>
                        <div class="calibo-brand">
                            <svg class="calibo-logo-icon" width="18" height="18" viewBox="0 0 24 24" fill="none">
                                <circle cx="12" cy="12" r="9" stroke="#1a2980" stroke-width="2.5" fill="none" />
                                <path d="M8.5 12L11 14.5L15.5 9.5" stroke="#0c7270" stroke-width="2.5"
                                    stroke-linecap="round" stroke-linejoin="round" />
                            </svg>
                            <span class="calibo-text">calibo</span>
                        </div>
                    </div>
            </div>
        </section>

        <!-- ══ SLIDE 10: THANK YOU ════════════════════════════════════ -->
        <section class="slide" id="s10" style="justify-content: center; align-items: center; text-align: center; position: relative;">
            <div class="ty-glow"></div>
            <div class="thankyou-logo an-1">THANK YOU</div>
            <div class="thankyou-qa an-2">Questions & Answers</div>
            <div class="thankyou-cta an-3">"We believe the future of health insurance isn't just about paying claims faster—it's about building trust through transparency, security, and human-centric AI."</div>
            <div class="ty-meta an-4">TEAM 15 • CALIBO AI ACADEMY • CAPSTONE PROJECT</div>
        </section>"""
if s8_pattern.search(content):
    content = s8_pattern.sub(s8_new, content)
else:
    print("Could not find Slide 8 and Hidden Demo")

# 3. Update TOTAL and NOTES
# Let's completely rewrite the script portion since the diff showed it might be missing or messed up.
script_pattern = re.compile(r'<script>\s*(?:const\s+TOTAL\s*=\s*\d+;.*?\];)?', re.DOTALL)
script_new = """<script>
        const TOTAL = 10;
        const NOTES = [
            "Welcome to the iCLAIM presentation. Today we will show how our Capstone Project solves a critical bottleneck in health insurance using Intelligent Document Processing and AI.",
            "Tell the story of Ramesh naturally. Highlight that the 15-day average delay in Andhra Pradesh is a real, measurable problem caused by manual operational bottlenecks.",
            "Walk through the DBIM Phase 1 research steps. Emphasize that the MVP focuses strictly on high-value business outcomes: automated validation and reviewer empowerment.",
            "This is the enterprise architecture mapped to the claim lifecycle. The diagram outlines the core components of our solution.",
            "The intelligence engine is built on three pillars. Explain how OCR, Semantic RAG (without heavy databases), and a machine learning ensemble work together.",
            "Show how the different roles interact with the system. Stress that the Reviewer Hub keeps the human-in-the-loop, backed by robust testing and QA.",
            "This slide contrasts the manual baseline with our AI-assisted approach. Emphasize the shift to rapid processing and the proactive nature of our fraud detection.",
            "Here is a live demonstration of our MVP in action.",
            "Conclude with the future vision. Our foundation is built for enterprise scale — these roadmap items are the logical next steps.",
            "Thank the audience for their time and open the floor to questions."
        ];"""
content = script_pattern.sub(script_new, content)

# 4. Fix Keydown
keydown_pattern = re.compile(r'if \(current === 11\)')
content = keydown_pattern.sub('if (current === 7)', content)

# 5. Fix Toggle Function
toggle_pattern = re.compile(r'function toggleReshapeS7\(\) \{.*?\}', re.DOTALL)
toggle_new = """function toggleReshapeArchitecture() {
            const container = document.querySelector('#s4 .arch-split-container');
            const imageSide = document.querySelector('#s4 .arch-image-side');
            const layersSide = document.querySelector('#s4 .arch-layers-side');
            const buttonSpan = document.querySelector('#btn-reshape-s4 span');
            
            if (container.classList.contains('reshaped')) {
                container.classList.remove('reshaped');
                imageSide.style.maxWidth = '60%';
                imageSide.style.flex = '1.4';
                imageSide.style.height = '440px';
                layersSide.style.display = 'flex';
                buttonSpan.textContent = '↕️ Reshape Layout';
            } else {
                container.classList.add('reshaped');
                imageSide.style.maxWidth = '100%';
                imageSide.style.flex = '1';
                imageSide.style.height = '520px';
                layersSide.style.display = 'none';
                buttonSpan.textContent = '↕️ Restore Split';
            }
        }"""
content = toggle_pattern.sub(toggle_new, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated HTML successfully")
