import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Swap nav links
text = text.replace(
'''                <li><a href="#experience">Experience</a></li>
                <li><a href="#projects">Projects</a></li>''',
'''                <li><a href="#projects">Projects</a></li>
                <li><a href="#experience">Experience</a></li>'''
)

# 2. Add profile image
text = text.replace(
'''            <div class="about-grid">
                <div class="about-text glass-card">''',
'''            <div class="about-grid">
                <div class="profile-image-container fade-in-up">
                    <img src="Sachiel_Photo.png" alt="Sachiel Chuckrow Profile" class="profile-image">
                </div>
                <div class="about-text glass-card">'''
)

# 3. Add images to project cards and update buttons

# Project 1
p1_old = '''                <div class="project-card glass-card">
                    <div class="project-header">
                        <i class="far fa-folder-open folder-icon"></i>
                        <div class="project-links">
                            <a href="https://www.linkedin.com/feed/update/urn:li:activity:7405394275842273281/"
                                target="_blank"><i class="fas fa-external-link-alt"></i></a>
                        </div>
                    </div>
                    <h3 class="project-title">Identifying "Stranger Danger Behaviors"</h3>'''

p1_new = '''                <div class="project-card glass-card">
                    <div class="project-header">
                        <i class="far fa-folder-open folder-icon"></i>
                    </div>
                    <h3 class="project-title">Identifying "Stranger Danger Behaviors"</h3>'''

text = text.replace(p1_old, p1_new)
text = text.replace(
'''                    <ul class="project-tech">
                        <li>Python</li>
                        <li>HTML</li>
                        <li>Machine Learning</li>
                        <li>Computer Vision</li>
                    </ul>\n                </div>''',
'''                    <ul class="project-tech">
                        <li>Python</li>
                        <li>HTML</li>
                        <li>Machine Learning</li>
                        <li>Computer Vision</li>
                    </ul>
                    <a href="https://www.linkedin.com/feed/update/urn:li:activity:7405394275842273281/" target="_blank" class="project-btn">View Demo <i class="fas fa-external-link-alt"></i></a>
                </div>'''
)

# Project 2
p2_old = '''                <div class="project-card glass-card">
                    <div class="project-header">
                        <i class="far fa-folder-open folder-icon"></i>
                        <div class="project-links">
                            <a href="https://github.com/SachielC/Finance_Agent_RL/blob/Clean/Report.pdf"
                                target="_blank"><i class="fab fa-github"></i></a>
                        </div>
                    </div>
                    <h3 class="project-title">Offline RL for Quant Trading</h3>'''

p2_new = '''                <div class="project-card glass-card">
                    <img src="RL_Photo.png" alt="Offline RL for Quant Trading" class="project-image">
                    <div class="project-header">
                        <i class="far fa-folder-open folder-icon"></i>
                    </div>
                    <h3 class="project-title">Offline RL for Quant Trading</h3>'''

text = text.replace(p2_old, p2_new)
text = text.replace(
'''                    <ul class="project-tech">
                        <li>Reinforcement Learning</li>
                        <li>Jupyter Notebook</li>
                        <li>Python</li>
                        <li>Finance</li>
                        <li>PyTorch</li>
                    </ul>\n                </div>''',
'''                    <ul class="project-tech">
                        <li>Reinforcement Learning</li>
                        <li>Jupyter Notebook</li>
                        <li>Python</li>
                        <li>Finance</li>
                        <li>PyTorch</li>
                    </ul>
                    <a href="https://github.com/SachielC/Finance_Agent_RL/blob/Clean/Report.pdf" target="_blank" class="project-btn">View Paper <i class="fas fa-file-pdf"></i></a>
                </div>'''
)


# Project 3
p3_old = '''                <div class="project-card glass-card">
                    <div class="project-header">
                        <i class="far fa-folder-open folder-icon"></i>
                        <div class="project-links">
                            <a href="https://www.bu.edu/articles/2025/using-ai-to-identify-plundered-antiquities/"
                                target="_blank"><i class="fas fa-external-link-alt"></i></a>
                        </div>
                    </div>
                    <h3 class="project-title">Khmer Statues Identification</h3>'''

p3_new = '''                <div class="project-card glass-card">
                    <img src="KhmerStatue.png" alt="Khmer Statues Identification" class="project-image">
                    <div class="project-header">
                        <i class="far fa-folder-open folder-icon"></i>
                    </div>
                    <h3 class="project-title">Khmer Statues Identification</h3>'''

text = text.replace(p3_old, p3_new)
text = text.replace(
'''                    <ul class="project-tech">
                        <li>Computer Vision</li>
                        <li>Neural Networks</li>
                        <li>Artificial Data Generation</li>
                        <li>PyTorch</li>
                    </ul>\n                </div>''',
'''                    <ul class="project-tech">
                        <li>Computer Vision</li>
                        <li>Neural Networks</li>
                        <li>Artificial Data Generation</li>
                        <li>PyTorch</li>
                    </ul>
                    <a href="https://www.bu.edu/articles/2025/using-ai-to-identify-plundered-antiquities/" target="_blank" class="project-btn">Read Article <i class="fas fa-external-link-alt"></i></a>
                </div>'''
)


# Project 4
p4_old = '''                <div class="project-card glass-card">
                    <div class="project-header">
                        <i class="far fa-folder-open folder-icon"></i>
                        <div class="project-links">
                            <a href="https://github.com/SachielC/Covid-Data-ETL-310" target="_blank"><i
                                    class="fab fa-github"></i></a>
                        </div>
                    </div>
                    <h3 class="project-title">Covid Data ETL Pipeline</h3>'''

p4_new = '''                <div class="project-card glass-card">
                    <img src="Azure.png" alt="Covid Data ETL Pipeline" class="project-image">
                    <div class="project-header">
                        <i class="far fa-folder-open folder-icon"></i>
                    </div>
                    <h3 class="project-title">Covid Data ETL Pipeline</h3>'''

text = text.replace(p4_old, p4_new)
text = text.replace(
'''                    <ul class="project-tech">
                        <li>Azure</li>
                        <li>Big Data</li>
                        <li>Microsoft PowerBI</li>
                        <li>Pipeline design</li>
                    </ul>\n                </div>''',
'''                    <ul class="project-tech">
                        <li>Azure</li>
                        <li>Big Data</li>
                        <li>Microsoft PowerBI</li>
                        <li>Pipeline design</li>
                    </ul>
                    <a href="https://github.com/SachielC/Covid-Data-ETL-310" target="_blank" class="project-btn">View Code <i class="fab fa-github"></i></a>
                </div>'''
)

# Project 5
p5_old = '''                <div class="project-card glass-card">
                    <div class="project-header">
                        <i class="far fa-folder-open folder-icon"></i>
                        <div class="project-links">
                            <a href="https://github.com/SachielC/Rust-Graph-Analysis" target="_blank"><i
                                    class="fab fa-github"></i></a>
                        </div>
                    </div>
                    <h3 class="project-title">Rust Graph Analysis</h3>'''

p5_new = '''                <div class="project-card glass-card">
                    <div class="project-header">
                        <i class="far fa-folder-open folder-icon"></i>
                    </div>
                    <h3 class="project-title">Rust Graph Analysis</h3>'''

text = text.replace(p5_old, p5_new)
text = text.replace(
'''                    <ul class="project-tech">
                        <li>RUST</li>
                        <li>Graphical Analysis</li>
                    </ul>\n                </div>''',
'''                    <ul class="project-tech">
                        <li>RUST</li>
                        <li>Graphical Analysis</li>
                    </ul>
                    <a href="https://github.com/SachielC/Rust-Graph-Analysis" target="_blank" class="project-btn">View Code <i class="fab fa-github"></i></a>
                </div>'''
)


# Project 6
p6_old = '''                <div class="project-card glass-card">
                    <div class="project-header">
                        <i class="far fa-folder-open folder-icon"></i>
                        <div class="project-links">
                            <a href="https://github.com/SachielC/NFL-Longevity-Prediction" target="_blank"><i
                                    class="fab fa-github"></i></a>
                        </div>
                    </div>
                    <h3 class="project-title">NFL Longevity Prediction</h3>'''

p6_new = '''                <div class="project-card glass-card">
                    <div class="project-header">
                        <i class="far fa-folder-open folder-icon"></i>
                    </div>
                    <h3 class="project-title">NFL Longevity Prediction</h3>'''

text = text.replace(p6_old, p6_new)
text = text.replace(
'''                    <ul class="project-tech">
                        <li>Scikit-learn</li>
                        <li>Random Forest</li>
                        <li>Data Visualization</li>
                    </ul>\n                </div>''',
'''                    <ul class="project-tech">
                        <li>Scikit-learn</li>
                        <li>Random Forest</li>
                        <li>Data Visualization</li>
                    </ul>
                    <a href="https://github.com/SachielC/NFL-Longevity-Prediction" target="_blank" class="project-btn">View Code <i class="fab fa-github"></i></a>
                </div>'''
)

# Swap Experience and Projects
exp_match = re.search(r'(<!-- Experience Section -->.*?)(<!-- Projects Section -->.*?)(<!-- Extracurriculars Section -->)', text, flags=re.DOTALL)
if exp_match:
    exp_code = exp_match.group(1)
    proj_code = exp_match.group(2)
    next_code = exp_match.group(3)
    
    text = text.replace(exp_match.group(0), proj_code + exp_code + next_code)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("done")
