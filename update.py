import re

FILE_PATH = "c:\\Users\\rthsa\\OneDrive\\Desktop\\CYBER BREAKER 2\\socialengineeringquiz.html"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# CSS Replacement
new_css = """        :root {
            --primary-bg: #000428;
            --bg-deep: #0f0c29;
            --text-silver: #e0e0ff;
            --accent-cyan: #00c6ff;
            --accent-purple: #9d50bb;
            --accent-green: #00ff9d;
            --accent-red: #ff4757;
            --accent-orange: #ffa502;
            --text-main: #ffffff;
            --text-secondary: #e0e0ff;
            --glass: rgba(255, 255, 255, 0.05);
            --border: rgba(0, 198, 255, 0.2);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            user-select: none;
            font-family: 'Poppins', sans-serif;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: var(--bg-deep);
            color: var(--text-silver);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow-x: hidden;
            position: relative;
            padding-top: 100px;
            padding-bottom: 50px;
        }

        /* Aurora Borealis Green/Blue Animation */
        .aurora-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            background: var(--bg-deep);
            overflow: hidden;
        }

        .aurora {
            position: absolute;
            width: 200%;
            height: 200%;
            top: -50%;
            left: -50%;
            background:
                radial-gradient(circle at 20% 30%, rgba(0, 255, 170, 0.2) 0%, transparent 40%),
                radial-gradient(circle at 80% 20%, rgba(0, 198, 255, 0.2) 0%, transparent 40%),
                radial-gradient(circle at 50% 80%, rgba(0, 212, 255, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 30% 70%, rgba(0, 150, 255, 0.15) 0%, transparent 30%);
            filter: blur(80px);
            animation: auroraMove 30s linear infinite;
        }

        @keyframes auroraMove {
            0% { transform: rotate(0deg) scale(1); }
            50% { transform: rotate(180deg) scale(1.2); }
            100% { transform: rotate(360deg) scale(1); }
        }

        /* Navbar */
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 5%;
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            background: rgba(0, 0, 0, 0.4);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            left: 0;
        }

        .logo-container {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .logo-img {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            border: 2px solid var(--accent-cyan);
            box-shadow: 0 0 10px var(--accent-cyan);
        }

        .logo-text {
            font-family: 'Orbitron', sans-serif;
            font-size: clamp(14px, 3vw, 20px);
            font-weight: 900;
            color: var(--accent-cyan);
            letter-spacing: 2px;
            text-shadow: 0 0 10px rgba(0, 243, 255, 0.5);
        }

        .mobile-menu-btn {
            display: none;
            color: var(--text-main);
            font-size: 24px;
            cursor: pointer;
            z-index: 1001;
        }

        .nav-links {
            display: flex;
            gap: 30px;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--text-main);
            font-weight: 500;
            position: relative;
            transition: 0.3s;
        }

        .nav-links a:hover {
            color: var(--accent-cyan);
        }

        /* Container & Cards (Frosty) */
        .container {
            width: 90%;
            max-width: 800px;
            background: rgba(255, 255, 255, 0.05); /* Frosty */
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
            border-radius: 20px;
            padding: 40px;
            position: relative;
            z-index: 10;
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        /* Frosty Glass Shine Effect */
        .container::before {
            content: '';
            position: absolute;
            top: 0;
            left: -150%;
            width: 50%;
            height: 100%;
            background: linear-gradient(to right, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0) 100%);
            transform: skewX(-25deg);
            transition: 0.6s;
            z-index: 1;
            pointer-events: none;
        }

        .container:hover::before {
            left: 150%;
        }

        .container:hover {
            transform: translateY(-5px) scale(1.01);
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(0, 198, 255, 0.6);
            box-shadow: 0 15px 40px rgba(0, 255, 170, 0.1), 0 0 20px rgba(0, 198, 255, 0.1);
        }

        #intro-screen * {
            position: relative;
            z-index: 2;
        }
        
        #quiz-screen * {
            position: relative;
            z-index: 2;
        }
        
        #result-screen * {
            position: relative;
            z-index: 2;
        }

        /* Intro Screen */
        #intro-screen { text-align: center; }

        .icon-row {
            display: flex;
            justify-content: center;
            gap: 25px;
            margin-bottom: 30px;
            font-size: 2.5rem;
            color: var(--accent-cyan);
        }

        .icon-row i {
            filter: drop-shadow(0 0 10px rgba(0, 198, 255, 0.5));
            transition: 0.3s;
        }

        .icon-row i:hover {
            transform: scale(1.2);
            color: var(--accent-green);
        }

        .title {
            font-family: 'Orbitron', sans-serif;
            font-size: clamp(1.5rem, 5vw, 2rem);
            color: var(--accent-cyan);
            margin-bottom: 25px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .intro-text {
            background: rgba(0, 0, 0, 0.3);
            padding: 25px;
            border-radius: 15px;
            line-height: 1.7;
            margin-bottom: 30px;
            text-align: left;
            border-left: 5px solid var(--accent-cyan);
            color: var(--text-silver);
        }

        .disclaimer {
            font-size: 0.85rem;
            color: var(--accent-red);
            font-weight: bold;
            margin-bottom: 30px;
            text-transform: uppercase;
        }

        /* Quiz HUD */
        #quiz-screen { display: none; }

        .hud {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
            font-family: 'Orbitron', sans-serif;
            font-size: clamp(0.7rem, 2.5vw, 0.9rem);
        }

        .timer-container {
            width: 100%;
            height: 8px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 4px;
            margin-bottom: 25px;
            overflow: hidden;
        }

        .timer-bar {
            height: 100%;
            width: 100%;
            background: var(--accent-green);
            transition: width 0.1s linear, background-color 0.3s ease;
            box-shadow: 0 0 10px var(--accent-green);
        }

        .progress-bar {
            width: 100%;
            height: 4px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 2px;
            margin-bottom: 30px;
        }

        .progress-fill {
            height: 100%;
            width: 0%;
            background: var(--accent-cyan);
            transition: width 0.4s ease;
        }

        /* Question Box */
        .question-text {
            font-size: clamp(1rem, 3vw, 1.3rem);
            margin-bottom: 30px;
            line-height: 1.6;
        }

        .options-grid {
            display: grid;
            gap: 15px;
        }

        .option {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border);
            padding: clamp(12px, 3vw, 18px) 25px;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s;
            font-size: clamp(0.9rem, 2.5vw, 1.05rem);
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .option:hover {
            background: rgba(0, 198, 255, 0.1);
            transform: translateX(10px);
            border-color: var(--accent-cyan);
        }

        .option.correct {
            background: rgba(0, 255, 157, 0.15) !important;
            border-color: var(--accent-green) !important;
            color: var(--accent-green);
        }

        .option.wrong {
            background: rgba(255, 71, 87, 0.15) !important;
            border-color: var(--accent-red) !important;
            color: var(--accent-red);
        }

        .option.disabled {
            pointer-events: none;
            opacity: 0.6;
        }

        /* Result Section */
        #result-screen {
            display: none;
            text-align: center;
        }

        .score-box {
            font-family: 'Orbitron', sans-serif;
            font-size: clamp(2rem, 8vw, 4rem);
            color: var(--accent-cyan);
            margin: 20px 0;
            text-shadow: 0 0 15px rgba(0, 198, 255, 0.5);
        }

        .explanation-scroll {
            max-height: 350px;
            overflow-y: auto;
            margin: 30px 0;
            padding-right: 10px;
            text-align: left;
        }

        .exp-item {
            background: rgba(0,0,0,0.3);
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 15px;
            border-left: 4px solid var(--accent-cyan);
        }

        .exp-item.incorrect {
            border-left-color: var(--accent-red);
        }

        .tips-section {
            background: rgba(0, 255, 157, 0.05);
            border: 1px dashed var(--accent-green);
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 30px;
            text-align: left;
        }

        /* Buttons */
        .btn {
            background: transparent;
            border: 1px solid var(--accent-cyan);
            color: var(--accent-cyan);
            padding: 12px 30px;
            font-family: 'Orbitron', sans-serif;
            text-transform: uppercase;
            cursor: pointer;
            border-radius: 5px;
            transition: 0.3s;
            letter-spacing: 1px;
            font-weight: bold;
            display: inline-block;
            text-decoration: none;
            margin: 5px;
        }

        .btn:hover {
            background: var(--accent-cyan);
            color: #000;
            box-shadow: 0 0 20px var(--accent-cyan);
        }

        /* Scrollbar */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-thumb {
            background: var(--accent-cyan);
            border-radius: 10px;
        }

        /* Responsive */
        @media screen and (max-width: 768px) {
            .mobile-menu-btn { display: block; }
            .nav-links {
                display: none;
                flex-direction: column;
                position: absolute;
                top: 70px;
                left: 0;
                width: 100%;
                background: rgba(0, 0, 0, 0.9);
                backdrop-filter: blur(10px);
                border-bottom: 1px solid var(--accent-cyan);
                padding: 20px 0;
                text-align: center;
                gap: 20px;
            }
            .nav-links.active { display: flex; }
            .container { padding: 25px; }
            .btn {
                padding: 10px 20px;
                font-size: 0.8rem;
            }
        }"""

content = re.sub(r'<style>.*?</style>', '<style>\n' + new_css + '\n    </style>', content, flags=re.DOTALL)

# HTML Body Replacement
old_body_start = r'<body>(.*?)<div class="container">'

new_body_start = """<body>

    <!-- Aurora Background -->
    <div class="aurora-container">
        <div class="aurora"></div>
    </div>

    <!-- Responsive Navbar -->
    <nav>
        <div class="logo-container">
            <img src="logo.jpeg" alt="Logo" class="logo-img" onerror="this.src='https://via.placeholder.com/40'">
            <div class="logo-text">CYBER BREAKER</div>
        </div>
        <div class="mobile-menu-btn" onclick="document.querySelector('.nav-links').classList.toggle('active')">☰</div>
        <div class="nav-links">
            <a href="home.html">Home</a>
            <a href="lessons.html">Learn</a>
            <a href="phishingquiz.html">Quiz</a>
        </div>
    </nav>

    <div class="container">"""

content = re.sub(old_body_start, new_body_start, content, flags=re.DOTALL)

# Update font links and title wrapper
font_link_replace = r'<link\s+href="https://fonts.googleapis.com/css2\?family=Orbitron[^"]*"\s+rel="stylesheet">'
new_font_link = '<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Poppins:wght@300;400;500;600;700;900&display=swap" rel="stylesheet">'
content = re.sub(font_link_replace, new_font_link, content)

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)
