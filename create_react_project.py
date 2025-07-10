import os
import shutil
import sys
import filecmp # Para comparar el contenido de los archivos

# --- Variables Globales ---
CREATED_FILES = []
MODIFIED_FILES = []

# --- Contenidos de Archivos (como cadenas multilinea) ---
# Hemos escapado las comillas simples y dobles para que Python no las interprete como fin de cadena
INDEX_HTML_CONTENT = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My React App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
"""

MAIN_JSX_CONTENT = """import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './index.css'; // You might need to create this file or use App.css

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
"""

APP_JSX_CONTENT = """import React from 'react';
import UserPanel from './components/UserPanel';
import './App.css';

function App() {
  return (
    <div className="App">
      <UserPanel />
    </div>
  );
}

export default App;
"""

APP_CSS_CONTENT = """/* src/App.css */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    background-color: #f4f4f4;
    color: #333;
}

.user-panel-container {
    background-color: #fff;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    margin: 40px auto;
}

h1 {
    color: #0056b3;
    text-align: center;
    margin-bottom: 30px;
}

button {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    margin-bottom: 20px;
    display: block;
    width: 100%;
}

button:hover {
    background-color: #0056b3;
}

button:disabled {
    background-color: #a0a0a0;
    cursor: not-allowed;
}

.hidden {
    display: none;
}

.loading-message {
    color: #007bff;
    font-style: italic;
    text-align: center;
    margin-top: 10px;
}

.error-message {
    color: #dc3545;
    font-weight: bold;
    text-align: center;
    margin-top: 10px;
}

#userList {
    list-style: none;
    padding: 0;
}

#userList li {
    background-color: #e9ecef;
    margin-bottom: 10px;
    padding: 15px;
    border-radius: 5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-left: 5px solid #007bff;
}

#userList li strong {
    color: #333;
}

#userList li span {
    font-size: 0.9em;
    color: #555;
}
"""

USER_LIST_JSX_CONTENT = """import React from 'react';
import useUserStore from '../store/userStore';

const UserList = () => {
  const users = useUserStore((state) => state.users);

  if (users.length === 0) {
    return <p className="loading-message">No hay usuarios cargados.</p>;
  }

  return (
    <ul id="userList">
      {users.map((user) => (
        <li key={user.id}>
          <strong>{user.name}</strong>
          <span>({user.email})</span>
        </li>
      ))}
    </ul>
  );
};

export default UserList;
"""

USER_PANEL_JSX_CONTENT = """import React, { useCallback } from 'react';
import useUserStore from '../store/userStore';
import UserList from './UserList';
import '../App.css';

const UserPanel = () => {
  const { isLoading, error, fetchUsers } = useUserStore((state) => ({
    isLoading: state.isLoading,
    error: state.error,
    fetchUsers: state.fetchUsers,
  }));

  const handleLoadUsers = useCallback(() => {
    fetchUsers();
  }, [fetchUsers]);

  return (
    <div className="user-panel-container">
      <h1>Gestión de Usuarios</h1>
      <button onClick={handleLoadUsers} disabled={isLoading}>
        {isLoading ? 'Cargando...' : 'Cargar Usuarios'}
      </button>

      {isLoading && <p className="loading-message">Cargando...</p>}
      {error && <p className="error-message">{error}</p>}

      {!isLoading && !error && <UserList />}
    </div>
  );
};

export default UserPanel;
"""

USER_STORE_JS_CONTENT = """import { create } from 'zustand';
import axios from 'axios';

const useUserStore = create((set) => ({
  users: [],
  isLoading: false,
  error: null,

  fetchUsers: async () => {
    set({ isLoading: true, error: null });
    try {
      const response = await axios.get('https://jsonplaceholder.typicode.com/users');
      set({ users: response.data, isLoading: false });
    } catch (error) {
      console.error('Error fetching users:', error);
      set({ error: 'Hubo un error al cargar los usuarios. Inténtalo de nuevo.', isLoading: false });
    }
  },

  clearUsers: () => set({ users: [], error: null }),
}));

export default useUserStore;
"""

PACKAGE_JSON_CONTENT = """{
  "name": "my-react-app",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint . --ext js,jsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview"
  },
  "dependencies": {
    "axios": "^1.7.2",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "zustand": "^4.5.2"
  },
  "devDependencies": {
    "@types/react": "^18.3.3",
    "@types/react-dom": "^18.3.0",
    "@vitejs/plugin-react": "^5.0.0",
    "eslint": "^8.57.0",
    "eslint-plugin-react": "^7.34.2",
    "eslint-plugin-react-hooks": "^4.6.2",
    "eslint-plugin-react-refresh": "^0.4.7",
    "vite": "^5.3.1"
  }
}
"""

GITIGNORE_CONTENT = """# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

# Diagnostic reports (https://nodejs.org/api/report.html)
.report/

# Node modules
node_modules/
dist/
dist-ssr/
*.local

# Editor directories and files
.idea/
.vscode/
*.suo
*.ntvs*
*.njsproj
*.sln
*.bak

# Environment variables
.env
.env.local
.env.*.local

# npm package manager cache
.npm
.yarn-cache

# MacOS
.DS_Store

# Windows
Thumbs.db
"""

VITE_CONFIG_JS_CONTENT = """import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
});
"""

# --- Funciones de Utilidad ---

def clear_screen():
    """Limpia la pantalla de la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def confirm_action(prompt):
    """Pide al usuario que confirme una acción."""
    while True:
        response = input(f"{prompt} (s/n): ").lower()
        if response in ['s', 'si']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Respuesta no válida. Por favor, ingresa 's' o 'n'.")

def create_directory(path):
    """Crea un directorio si no existe y lo registra."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"  - Carpeta creada: {path}")

def create_or_update_file(file_path, content):
    """Crea o actualiza un archivo condicionalmente."""
    temp_file_path = file_path + ".tmp" # Usamos un archivo temporal para la comparación

    try:
        with open(temp_file_path, "w", encoding="utf-8") as f:
            f.write(content)

        if not os.path.exists(file_path):
            shutil.copyfile(temp_file_path, file_path)
            CREATED_FILES.append(file_path)
            print(f"  - Archivo creado: {file_path}")
        else:
            # Compara archivos binariamente para evitar problemas de codificación/EOL
            if not filecmp.cmp(temp_file_path, file_path, shallow=False):
                shutil.copyfile(temp_file_path, file_path)
                MODIFIED_FILES.append(file_path)
                print(f"  - Archivo modificado: {file_path}")
            # else: Contenido igual, no hacer nada
    except Exception as e:
        print(f"Error al procesar el archivo {file_path}: {e}")
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

def select_base_directory():
    """Permite al usuario seleccionar un directorio base de forma interactiva."""
    current_path = os.path.expanduser("~") # Iniciar desde la carpeta HOME del usuario
    
    while True:
        clear_screen()
        print("--- Selección de Directorio Base ---")
        print("Navega con los números, '..' para subir, 'S' para seleccionar, 'Q' para salir.")
        print(f"\nDirectorio actual: {current_path}\n")

        # Obtener y numerar solo subdirectorios, excluyendo ocultos y comunes
        entries = sorted([
            e for e in os.listdir(current_path) 
            if os.path.isdir(os.path.join(current_path, e)) 
            and not e.startswith('.') # Excluir carpetas ocultas
            and e not in ['node_modules', 'dist', '.git'] # Excluir carpetas de proyecto comunes
        ])
        
        for i, entry in enumerate(entries):
            print(f"  [{i+1}] {entry}/")

        print("\n  [..] Subir un nivel")
        print("  [S]  Seleccionar este directorio")
        print("  [Q]  Salir")

        choice = input("\nElige una opción: ").strip()

        if choice.lower() == 's':
            print(f"\nHas seleccionado: {current_path}")
            if confirm_action(f"¿Confirmas que '{current_path}' es la ruta base correcta para tu proyecto?"):
                return current_path
            else:
                continue # Permite al usuario re-seleccionar

        elif choice.lower() == 'q':
            print("Operación cancelada por el usuario.")
            sys.exit(0)

        elif choice == '..':
            parent_path = os.path.dirname(current_path)
            if parent_path and parent_path != current_path: # Evitar subir más allá de la raíz
                current_path = parent_path
            else:
                print("Ya estás en el directorio raíz accesible.")
                input("Presiona Enter para continuar...") # Pausar para que el usuario vea el mensaje
        
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(entries):
                new_path = os.path.join(current_path, entries[idx])
                if os.path.isdir(new_path):
                    current_path = new_path
                else: # Esto no debería ocurrir si se filtran bien los directorios
                    print("La selección no es un directorio válido.")
                    input("Presiona Enter para continuar...")
            else:
                print("Número de opción inválido.")
                input("Presiona Enter para continuar...")
        else:
            print("Opción no reconocida.")
            input("Presiona Enter para continuar...")

# --- Lógica Principal del Script ---
def main():
    clear_screen()
    print("--- Creador/Actualizador de Proyectos React ---")
    print("Este script te ayudará a configurar la estructura de tu proyecto React.")
    print("Por favor, selecciona la carpeta donde deseas crear tu proyecto.")
    input("Presiona Enter para comenzar la selección de directorio...")

    base_project_dir = select_base_directory()
    
    final_project_path = os.path.join(base_project_dir)

    clear_screen()
    print("--- Confirmación Final ---")
    print(f"El proyecto se creará/actualizará en: {final_project_path}")
    print("Esto podría crear nuevas carpetas y/o modificar archivos existentes.")
    if not confirm_action("¿Estás seguro de que deseas continuar?"):
        print("Operación cancelada.")
        sys.exit(0)

    print("\nIniciando creación/actualización de la estructura...\n")

    # Crear la carpeta raíz del proyecto y cambiar a ella
    create_directory(final_project_path)
    os.chdir(final_project_path)

    # --- Carpetas y Archivos Principales del Proyecto React ---
    create_directory("public")
    create_or_update_file("public/index.html", INDEX_HTML_CONTENT)

    create_directory("src")
    create_directory("src/assets")
    create_directory("src/components")
    create_directory("src/store")

    create_or_update_file("src/main.jsx", MAIN_JSX_CONTENT)
    create_or_update_file("src/App.jsx", APP_JSX_CONTENT)
    create_or_update_file("src/App.css", APP_CSS_CONTENT)
    create_or_update_file("src/components/UserList.jsx", USER_LIST_JSX_CONTENT)
    create_or_update_file("src/components/UserPanel.jsx", USER_PANEL_JSX_CONTENT)
    create_or_update_file("src/store/userStore.js", USER_STORE_JS_CONTENT)
    
    # Otros archivos comunes del proyecto
    create_or_update_file("package.json", PACKAGE_JSON_CONTENT)
    create_or_update_file(".gitignore", GITIGNORE_CONTENT)
    create_or_update_file("vite.config.js", VITE_CONFIG_JS_CONTENT)

    # --- Resumen Final ---
    clear_screen()
    print("--------------------------------------------------------")
    print("       Resumen de la Creación/Actualización del Proyecto")
    print("--------------------------------------------------------")
    print(f"Proyecto ubicado en: {final_project_path}\n")

    if CREATED_FILES:
        print("Archivos CREADOS:")
        for file in CREATED_FILES:
            print(f"  - {file}")
    else:
        print("No se crearon archivos nuevos.")
    print("")

    if MODIFIED_FILES:
        print("Archivos MODIFICADOS:")
        for file in MODIFIED_FILES:
            print(f"  - {file}")
    else:
        print("No se modificaron archivos existentes.")
    print("")

    print("--- Próximos Pasos ---")
    print(f"1. Navega al directorio del proyecto: cd \"{final_project_path}\"")
    print("2. Instala las dependencias: npm install")
    print("3. Ejecuta el servidor de desarrollo: npm run dev")
    print("--------------------------------------------------------")

if __name__ == "__main__":
    main()