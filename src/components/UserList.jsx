import React from 'react';
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
