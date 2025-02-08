# React + TypeScript + Vite + FastAPI + PyWebview

## Setup

### Backend (FastAPI & PyWebview)

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   ```
   ```bash
   source env/bin/activate  # Linux/macOS
    ```
   ```bash
   env\Scripts\activate.bat  # Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Update dependencies:**
   ```bash
   pip freeze > requirements.txt
   ```

## Technologies

### Frontend: React + TypeScript + Vite
- **React**: Component-based UI architecture with a virtual DOM for optimized performance.
- **TypeScript**: Static typing for improved code reliability and maintainability.
- **Vite**: Fast build and development environment for modern frontend applications.
- **Modular Approach**: The frontend can be replaced with any framework capable of building a static page or SPA.
- **Use Case**: Ideal for user interfaces that require minimal system interactions, reducing browser dependency. Suitable for applications requiring direct device interactions, such as POS software.

### Backend: FastAPI
- **FastAPI**: High-performance web framework with built-in async support, automatic OpenAPI documentation, and data validation.
- **Optimized for System Interaction**: Enables seamless integration with operating systems and devices.
- **Compare to ElectronJS**: ElectronJS is still great but not always usable. Eliminates reliance on heavy third-party libraries or advanced C++ knowledge, making complex system interactions more accessible.

### Desktop Integration: PyWebview
- **PyWebview**: Provides a lightweight native WebView for rendering the frontend.
- **Full-Stack Desktop Application**: Combines FastAPI and a frontend SPA into a standalone desktop application with direct OS and hardware integration.

## References
- [Vite Documentation](https://vitejs.dev)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [PyWebview Documentation](https://pywebview.flowrl.com)

