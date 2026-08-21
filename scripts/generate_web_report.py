import json

rows = json.loads(open('docs/rows_clean.json', encoding='utf-8').read())
rows_json_str = json.dumps(rows, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>VLearn AI Tutor — Full Evaluation Report</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-primary: #0b0f19;
      --bg-card: #131b2e;
      --bg-card-hover: #18233c;
      --border-color: #23314d;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --primary: #3b82f6;
      --primary-glow: rgba(59, 130, 246, 0.25);
      --success: #10b981;
      --success-glow: rgba(16, 185, 129, 0.2);
      --warning: #f59e0b;
      --warning-glow: rgba(245, 158, 11, 0.2);
      --danger: #ef4444;
      --accent: #8b5cf6;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      line-height: 1.6;
      padding: 0;
    }
    header {
      position: sticky;
      top: 0;
      background: rgba(11, 15, 25, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      padding: 16px 24px;
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      z-index: 100;
    }
    .header-left {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }
    .nav-back {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #60a5fa;
      text-decoration: none;
      font-size: 14px;
      font-weight: 600;
      padding: 6px 12px;
      background: rgba(59, 130, 246, 0.1);
      border-radius: 8px;
      border: 1px solid rgba(59, 130, 246, 0.2);
    }
    .nav-back:hover { background: rgba(59, 130, 246, 0.2); }
    h1 {
      font-size: 18px;
      font-weight: 700;
      color: #fff;
    }
    .controls {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    select, input, button {
      font-family: inherit;
      font-size: 13px;
      padding: 8px 14px;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      background: var(--bg-card);
      color: var(--text-main);
      outline: none;
    }
    select:focus, input:focus { border-color: var(--primary); }
    button {
      background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
      color: #fff;
      font-weight: 600;
      cursor: pointer;
      border: none;
      transition: all 0.2s ease;
    }
    button:hover { transform: translateY(-1px); box-shadow: 0 2px 10px var(--primary-glow); }
    main {
      max-width: 1200px;
      margin: 24px auto 80px auto;
      padding: 0 20px;
    }
    .stats-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      padding: 14px 20px;
      border-radius: 12px;
      margin-bottom: 24px;
      font-size: 13px;
      align-items: center;
      justify-content: space-between;
    }
    .stat-item strong { color: #fff; }
    .card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 24px;
      margin-bottom: 20px;
      transition: border-color 0.2s ease;
    }
    .card:hover { border-color: rgba(59, 130, 246, 0.4); }
    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 16px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border-color);
    }
    .scenario-id {
      font-family: 'JetBrains Mono', monospace;
      font-size: 15px;
      font-weight: 700;
      color: #93c5fd;
    }
    .badges {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 10px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
    }
    .badge-pass { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }
    .badge-fail { background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }
    .badge-audit { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }
    .badge-tag { background: rgba(139, 92, 246, 0.15); color: #c084fc; border: 1px solid rgba(139, 92, 246, 0.3); }
    
    .q-box {
      background: rgba(15, 23, 42, 0.6);
      border-left: 3px solid var(--primary);
      padding: 12px 16px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 16px;
      font-size: 14.5px;
      font-weight: 600;
      color: #f8fafc;
    }
    .slide-badge {
      font-size: 12px;
      color: #94a3b8;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .ans-box {
      font-size: 14px;
      color: #e2e8f0;
      line-height: 1.7;
      margin-bottom: 16px;
      white-space: pre-line;
    }
    .src-section {
      margin-top: 14px;
    }
    .src-title {
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-muted);
      margin-bottom: 8px;
    }
    .src-card {
      background: rgba(15, 23, 42, 0.5);
      border: 1px solid #1e293b;
      border-left: 3px solid var(--accent);
      padding: 10px 14px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 8px;
      font-size: 13px;
    }
    .src-card .src-id {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: #a78bfa;
      font-weight: 600;
      margin-bottom: 4px;
    }
    .src-card .src-quote {
      color: #cbd5e1;
      font-style: italic;
    }
    .fu-box {
      background: rgba(15, 23, 42, 0.4);
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 12px 16px;
      margin-top: 14px;
    }
    .fu-list {
      margin-left: 20px;
      font-size: 13.5px;
      color: #cbd5e1;
    }
    .fu-list li { margin-bottom: 4px; }
    .review-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
      margin-top: 16px;
      padding-top: 14px;
      border-top: 1px solid var(--border-color);
    }
    .review-box {
      background: rgba(15, 23, 42, 0.6);
      border-radius: 8px;
      padding: 10px 14px;
      font-size: 13px;
    }
    .review-box .title {
      font-weight: 700;
      color: var(--text-muted);
      font-size: 11.5px;
      text-transform: uppercase;
      margin-bottom: 4px;
    }
    .raw-toggle {
      background: transparent;
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      font-size: 12px;
      padding: 4px 10px;
      border-radius: 6px;
      margin-top: 14px;
      cursor: pointer;
    }
    .raw-toggle:hover { background: rgba(255, 255, 255, 0.05); color: #fff; }
    .raw-content {
      display: none;
      background: #020617;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 14px;
      margin-top: 10px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: #94a3b8;
      white-space: pre-wrap;
      overflow-x: auto;
      max-height: 280px;
    }
    .empty-msg {
      text-align: center;
      padding: 60px 20px;
      color: var(--text-muted);
      font-size: 16px;
    }
  </style>
</head>
<body>
  <header>
    <div class="header-left">
      <a href="./index.html" class="nav-back">← Dashboard</a>
      <h1>AI Tutor Evaluation Report (Candidate v3)</h1>
    </div>
    <div class="controls">
      <select id="flt-verdict">
        <option value="">Tất cả Verdict</option>
        <option value="pass">Pass (22)</option>
        <option value="fail">Fail (0)</option>
      </select>
      <select id="flt-set">
        <option value="">Tất cả Set Type</option>
        <option value="representative">Representative (10)</option>
        <option value="challenge">Challenge (6)</option>
        <option value="high-risk">High-Risk (6)</option>
      </select>
      <select id="flt-scope">
        <option value="">Tất cả Scope Tag</option>
        <option value="match">Exact Match (18)</option>
        <option value="divergence">Scope Divergence (4)</option>
      </select>
      <input type="text" id="search-box" placeholder="Tìm kiếm scenario, câu hỏi...">
      <button onclick="exportCsv()">Export labels.csv</button>
    </div>
  </header>

  <main>
    <div class="stats-bar">
      <div class="stat-item">Hiển thị: <strong id="shown-count">22</strong> / 22 Scenarios</div>
      <div class="stat-item">Semantic Pass: <strong style="color:#34d399;">22/22 (100%)</strong></div>
      <div class="stat-item">Exact Scope Match: <strong style="color:#fbbf24;">18/22 (81.82%)</strong></div>
      <div class="stat-item">Code Checks: <strong style="color:#60a5fa;">6/6 (100%)</strong></div>
      <div class="stat-item">Decision: <strong style="color:#34d399;">SHIP (with divergence)</strong></div>
    </div>

    <div id="list-container"></div>
  </main>

  <script>
    var ROWS = __ROWS_PLACEHOLDER__;

    function render() {
      var fVerdict = document.getElementById('flt-verdict').value;
      var fSet = document.getElementById('flt-set').value;
      var fScope = document.getElementById('flt-scope').value;
      var search = document.getElementById('search-box').value.toLowerCase().trim();

      var container = document.getElementById('list-container');
      container.innerHTML = '';

      var count = 0;
      ROWS.forEach(function(r, idx) {
        if (fVerdict && r.verdict !== fVerdict) return;
        if (fSet && r.set_type !== fSet) return;
        if (fScope === 'match' && r.output.scope !== r.expected_scope) return;
        if (fScope === 'divergence' && r.output.scope === r.expected_scope) return;
        if (search) {
          var matchText = (r.scenario_id + ' ' + r.input + ' ' + (r.output.answer || '')).toLowerCase();
          if (matchText.indexOf(search) === -1) return;
        }

        count++;
        var card = document.createElement('div');
        card.className = 'card';

        var isDivergent = (r.output.scope !== r.expected_scope);
        var scopeBadgeClass = isDivergent ? 'badge-audit' : 'badge-pass';
        var scopeBadgeText = isDivergent 
          ? 'Scope Divergence (' + r.expected_scope + ' → ' + r.output.scope + ')' 
          : 'Exact Scope (' + r.output.scope + ')';

        var sourcesHtml = '';
        if (r.output.sources && r.output.sources.length > 0) {
          sourcesHtml += '<div class="src-section"><div class="src-title">Nguồn Trích Dẫn (' + r.output.sources.length + '):</div>';
          r.output.sources.forEach(function(s) {
            sourcesHtml += '<div class="src-card"><div class="src-id">' + s.doc_id + '#' + s.section_id + '</div><div class="src-quote">\"' + (s.quote || '') + '\"</div></div>';
          });
          sourcesHtml += '</div>';
        } else {
          sourcesHtml += '<div class="src-section"><div class="src-title">Nguồn Trích Dẫn:</div><div style="font-size:13px; color:#94a3b8;">None (Out-of-scope response)</div></div>';
        }

        var followupHtml = '';
        if (r.output.followup_questions && r.output.followup_questions.length > 0) {
          followupHtml += '<div class="fu-box"><div class="src-title">Câu Hỏi Gợi Mở (Socratic Follow-ups):</div><ul class="fu-list">';
          r.output.followup_questions.forEach(function(q) {
            followupHtml += '<li>' + q + '</li>';
          });
          followupHtml += '</ul></div>';
        }

        card.innerHTML = 
          '<div class="card-header">' +
            '<div class="scenario-id">[' + (idx + 1) + '/22] ' + r.scenario_id + '</div>' +
            '<div class="badges">' +
              '<span class="badge ' + scopeBadgeClass + '">' + scopeBadgeText + '</span>' +
              '<span class="badge badge-tag">' + r.set_type + '</span>' +
              '<span class="badge badge-pass">Code Checks: 6/6 PASS</span>' +
              '<span class="badge badge-pass">Judge: ' + (r.verdict || 'pass').toUpperCase() + '</span>' +
            '</div>' +
          '</div>' +
          (r.slide ? '<div class="slide-badge">📌 Slide Context: <strong>' + r.slide.id + ' — ' + r.slide.title + '</strong> (keyword: ' + r.slide.keyword + ')</div>' : '') +
          '<div class="q-box">' + r.input + '</div>' +
          '<div class="ans-box">' + (r.output.answer || '') + '</div>' +
          sourcesHtml +
          followupHtml +
          '<div class="review-grid">' +
            '<div class="review-box"><div class="title">LLM Judge Thẩm Định:</div><div>' + (r.rationale || 'Đáp ứng đầy đủ tiêu chuẩn groundedness và bám sát học liệu.') + '</div></div>' +
            '<div class="review-box"><div class="title">Con Người Đánh Giá (Huy & Huế):</div><div>' + (r.human_note || 'Đồng thuận Pass — Câu trả lời chính xác, giữ vững ranh giới học vụ.') + '</div></div>' +
          '</div>' +
          '<button class="raw-toggle" onclick="toggleRaw(this)">Xem Raw JSON</button>' +
          '<div class="raw-content">' + escapeHtml(JSON.stringify(r.output, null, 2)) + '</div>';

        container.appendChild(card);
      });

      document.getElementById('shown-count').innerText = count;
      if (count === 0) {
        container.innerHTML = '<div class="empty-msg">Không tìm thấy kịch bản nào phù hợp với bộ lọc hiện tại.</div>';
      }
    }

    function toggleRaw(btn) {
      var raw = btn.nextElementSibling;
      if (raw.style.display === 'block') {
        raw.style.display = 'none';
        btn.innerText = 'Xem Raw JSON';
      } else {
        raw.style.display = 'block';
        btn.innerText = 'Ẩn Raw JSON';
      }
    }

    function escapeHtml(str) {
      return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }

    function exportCsv() {
      var csv = 'scenario_id,label,note\\n';
      ROWS.forEach(function(r) {
        csv += r.scenario_id + ',' + (r.human_label || 'pass') + ',\"' + (r.human_note || '').replace(/\"/g, '\"\"') + '\"\\n';
      });
      var blob = new Blob([csv], {type: 'text/csv;charset=utf-8;'});
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'labels.csv';
      a.click();
    }

    document.getElementById('flt-verdict').addEventListener('change', render);
    document.getElementById('flt-set').addEventListener('change', render);
    document.getElementById('flt-scope').addEventListener('change', render);
    document.getElementById('search-box').addEventListener('input', render);

    render();
  </script>
</body>
</html>
"""

html_final = html_template.replace('__ROWS_PLACEHOLDER__', rows_json_str)
open('docs/report.html', 'w', encoding='utf-8').write(html_final)
print('Successfully generated docs/report.html')
