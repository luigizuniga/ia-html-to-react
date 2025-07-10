import React, { useCallback } from 'react';
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
