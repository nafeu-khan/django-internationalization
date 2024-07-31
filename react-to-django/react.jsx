import axios from 'axios';
import React, { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';

function App() {
  const { t, i18n } = useTranslation();
  const [message, setMessage] = useState('');

  useEffect(() => {
    const selectedLanguage = localStorage.getItem('selectedLanguage') || 'en';
    i18n.changeLanguage(selectedLanguage);

    axios.get('/api/my-view/', {
      headers: {
        'Accept-Language': selectedLanguage,
      },
    })
    .then(response => {
      setMessage(response.data.message);
    })
    .catch(error => {
      console.error('Error fetching message:', error);
    });
  }, [i18n]);

  const changeLanguage = (lng) => {
    i18n.changeLanguage(lng);
    localStorage.setItem('selectedLanguage', lng);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>{t('welcome')}</h1>
        <p>{message}</p>
        <button onClick={() => changeLanguage('en')}>English</button>
        <button onClick={() => changeLanguage('fr')}>French</button>
        <button onClick={() => changeLanguage('bn')}>Bengali</button>
      </header>
    </div>
  );
}

export default App;
