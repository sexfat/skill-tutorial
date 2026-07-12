# Skill Tutorial

Repo: https://github.com/sexfat/skill-tutorial

同一個任務「幫我摘要一個檔案」，分別寫成「浪費 token」與「省 token」兩種 SKILL.md，用來教學如何撰寫 Claude Code skill：如何界定觸發範圍、如何避免不必要的工具呼叫、如何控制輸出邊界。

## 內容

- `.claude/skills/summarize-file-bad/SKILL.md`：浪費 token 示範版，刻意包含多餘的 `ls`/`find`/重複讀檔、全文覆述、逐段落長篇說明、主動加碼建議等步驟。
- `.claude/skills/summarize-file-good/SKILL.md`：省 token 示範版，只做任務必要的最小動作，輸出精簡條列摘要。
- `demo/sample.py`：用來被摘要的範例檔案。
- `demo/skill-writing-tutorial.html`：教學頁面，整理對照案例、實測數據與撰寫 skill 的檢查清單。
