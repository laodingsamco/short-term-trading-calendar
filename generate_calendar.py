name: Weekly Calendar Update

on:
  schedule:
    - cron: "0 1 * * 1"  # 每周一 UTC 1:00，对应北京时间上午9点
  workflow_dispatch:     # 允许手动触发

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.x"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install ics pytz

      - name: Generate .ics file
        run: python generate_calendar.py

      - name: Commit and push changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add short_term_trading.ics
          git commit -m "Auto update .ics calendar" || echo "No changes to commit"
          git push
