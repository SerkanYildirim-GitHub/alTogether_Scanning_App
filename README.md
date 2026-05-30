# alTogether — Python Security Scanning Case Builder
<br>
<b>alTogether</b> is a Python command-line tool that automates authorized security scanning workflows for lab and assessment environments. The tool accepts a target IP address, creates a dedicated case folder, runs multiple reconnaissance and vulnerability assessment tools, and saves the results into organized output files for review.
</br>
<br>
> **Authorized Use Only:** This tool is intended for educational labs and authorized security testing environments. Do not run scans against systems you do not own or do not have explicit permission to assess.
</br>


## Purpose

This project was created to streamline repetitive security scanning tasks and organize scan results into a structured case folder. It demonstrates Python scripting, security automation, vulnerability assessment workflow design, and penetration testing fundamentals.

## Usage

Run with a target IP address:

```bash
python3 alTogether.py <target_ip>
