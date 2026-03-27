quarto publish gh-pages --no-prompt
quarto render
xcopy /y /s docs\*.* v:\nginx-php-www\www\cdn.lrn4life.org\AI-2025-2026\  