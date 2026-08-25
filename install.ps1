# =============================================================================
# celebrity-elysia — one-line installer (PowerShell / Windows)
#
#   irm https://raw.githubusercontent.com/chen2940/celebrity-elysia/main/install.ps1 | iex
#
# Optional args (passed to tools/install.py), e.g.:
#   $args = @("--host", "claude-code,workbuddy", "--force"); irm ... | iex
# =============================================================================
$ErrorActionPreference = 'Stop'

$Repo   = 'chen2940/celebrity-elysia'
$Branch = 'main'
$TmpDir = Join-Path $env:TEMP ("celebrity-elysia-install-" + [guid]::NewGuid().ToString('N'))

try {
    New-Item -ItemType Directory -Path $TmpDir -Force | Out-Null

    Write-Host "==> Downloading celebrity-elysia ($Branch) from GitHub ..."
    $ZipPath = Join-Path $TmpDir 'skill.zip'
    Invoke-WebRequest -Uri "https://github.com/$Repo/archive/refs/heads/$Branch.zip" -OutFile $ZipPath

    Write-Host "==> Extracting ..."
    Expand-Archive -Path $ZipPath -DestinationPath $TmpDir -Force
    $SkillSrc = Join-Path $TmpDir "celebrity-elysia-$Branch"

    if (-not (Test-Path (Join-Path $SkillSrc 'SKILL.md'))) {
        throw "Downloaded archive does not look like a skill repo (no SKILL.md)."
    }

    $Py = $null
    foreach ($candidate in @('python', 'py')) {
        $cmd = Get-Command $candidate -ErrorAction SilentlyContinue
        if ($cmd) { $Py = $candidate; break }
    }
    if (-not $Py) {
        throw 'Python 3 is required. Install it (https://www.python.org), then run again.'
    }

    Write-Host "==> Installing (python: $Py) ..."
    & $Py (Join-Path $SkillSrc 'tools\install.py') --source $SkillSrc @args

    Write-Host "==> Done."
}
finally {
    Remove-Item -Recurse -Force $TmpDir -ErrorAction SilentlyContinue
}
