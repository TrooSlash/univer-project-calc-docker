# Современный способ запуска GUI калькулятора на Windows (2025)

## 🚀 Рекомендуемые методы

### **Метод 1: WSLg (Встроен в Windows 11)**

**Самый современный и простой способ!**

✅ **Преимущества:**
- Встроен в Windows 11 и Windows 10 (build 19044+)
- Автоматическая настройка
- Аппаратное ускорение GPU
- Поддержка звука

**Шаги:**

1. Убедитесь, что WSL2 установлен:
   ```powershell
   wsl --version
   ```

2. Запустите калькулятор через скрипт:
   ```powershell
   .\run-gui-wslg.ps1
   ```

Или вручную:
```powershell
docker run --rm `
    -e "DISPLAY=:0" `
    -e "QT_X11_NO_MITSHM=1" `
    -v "/run/desktop/mnt/host/wslg/.X11-unix:/tmp/.X11-unix:rw" `
    -v "/run/desktop/mnt/host/wslg:/mnt/wslg:rw" `
    coofol/calculator-app:latest
```

---

### **Метод 2: X410 (Платный, но лучший UX)**

**X410** - современный коммерческий X-сервер для Windows.

✅ **Преимущества:**
- Автоматическая интеграция с WSL2
- Поддержка 4K дисплеев
- Аппаратное ускорение OpenGL
- Нативный вид приложений
- Цена: $9.99 в Microsoft Store

**Установка:**
1. Установите из Microsoft Store: https://www.microsoft.com/store/apps/9NLP712ZMN9Q
2. Запустите X410
3. Запустите калькулятор:
   ```powershell
   docker run --rm -e DISPLAY=host.docker.internal:0 coofol/calculator-app:latest
   ```

---

### **Метод 3: VcXsrv (Бесплатный)**

**Классический метод, работает стабильно.**

**Установка:**

1. Скачайте VcXsrv: https://sourceforge.net/projects/vcxsrv/

2. Запустите **XLaunch**:
   - Multiple windows
   - Display number: `0`
   - Start no client
   - ✅ **Disable access control**
   - ❌ **Native opengl** (отключить!)

3. Запустите калькулятор:
   ```powershell
   docker run --rm -e DISPLAY=host.docker.internal:0 coofol/calculator-app:latest
   ```

---

## 🆕 **Новинка 2024-2025: WSL2 GUI Apps**

Microsoft значительно улучшила WSLg в 2024-2025:
- Автоматическое масштабирование HiDPI
- Поддержка нескольких мониторов
- Копирование/вставка между Windows и Linux приложениями
- Drag-and-drop файлов

**Системные требования:**
- Windows 11 (любая версия)
- Windows 10 build 19044+ с последними обновлениями

---

## 🎯 **Рекомендация**

Для современного опыта в 2025 году:

1. **Windows 11 → WSLg** (встроено, бесплатно)
2. **Требуется лучший UX → X410** ($9.99)
3. **Windows 10 старые → VcXsrv** (бесплатно)

---

## 📝 **Быстрый запуск**

```powershell
# Запуск через WSLg (Windows 11)
.\run-gui-wslg.ps1

# Запуск через X-сервер (VcXsrv/X410)
docker run --rm -e DISPLAY=host.docker.internal:0 coofol/calculator-app:latest
```
