# Скрипт для запуска GUI калькулятора через WSLg
# Требуется: Windows 11 или Windows 10 с WSLg

Write-Host "🚀 Запуск калькулятора с GUI через WSLg..." -ForegroundColor Green

# Проверяем WSLg
$wslVersion = wsl --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ WSL не установлен. Установите WSL2: wsl --install" -ForegroundColor Red
    exit 1
}

Write-Host "✅ WSL обнаружен" -ForegroundColor Green

# Получаем путь к сокету X11 в WSL
$wslDistro = "Ubuntu"  # Измените на вашу дистрибуцию WSL

# Запускаем контейнер с GUI через WSL
Write-Host "🎨 Запуск GUI приложения..." -ForegroundColor Cyan

docker run --rm `
    -e "DISPLAY=:0" `
    -e "QT_X11_NO_MITSHM=1" `
    -v "/run/desktop/mnt/host/wslg/.X11-unix:/tmp/.X11-unix:rw" `
    -v "/run/desktop/mnt/host/wslg:/mnt/wslg:rw" `
    --name calculator-gui `
    coofol/calculator-app:latest

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Калькулятор закрыт" -ForegroundColor Green
} else {
    Write-Host "❌ Ошибка запуска. Код: $LASTEXITCODE" -ForegroundColor Red
    Write-Host ""
    Write-Host "💡 Альтернативные варианты:" -ForegroundColor Yellow
    Write-Host "1. Используйте Windows Terminal с WSL2" -ForegroundColor Yellow
    Write-Host "2. Установите VcXsrv: https://sourceforge.net/projects/vcxsrv/" -ForegroundColor Yellow
}
