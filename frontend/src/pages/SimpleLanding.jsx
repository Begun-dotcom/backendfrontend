import { useState } from 'react';
import { Services } from '../services/services';

function SimpleLanding() {
  const [phone, setPhone] = useState('');
  const [description, setDescription] = useState('');
  const [status, setStatus] = useState('');

  const sendToBackend = async (phone, description) => {
   const response = await Services.send_content(phone, description)

};
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!phone) return;

    setStatus('sending');
    try {
        await sendToBackend(phone, description);
        setStatus('success');
        setPhone('');
        setDescription('');
    } catch (error) {
        setStatus('error');
        setPhone('');
        setDescription('');
    }
    
    setTimeout(() => setStatus(''), 3000);
    
  };


  

  return (
    <div>
      {/* Шапка с фото */}
      <div className="relative h-screen bg-cover bg-center" 
           style={{ backgroundImage: "url('/hero.jpg')" }}>
        <div className="absolute inset-0 bg-black/40" />
        <div className="relative z-10 flex items-center justify-center h-full text-center text-white">
          <h1 className="text-4xl font-bold">Заголовок</h1>
        </div>
      </div>

      {/* Форма внизу */}
      <div className="p-8 text-center flex flex-col">
        <h2 className="text-2xl mb-4">Оставьте заявку</h2>
        <form onSubmit={handleSubmit} className="max-w-md mx-auto flex flex-col ga">
          <input
            type="tel"
            placeholder="+7 (___) ___-__-__"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
            className="w-full p-3 border rounded-lg mb-3"
            required
          />
          <input
            type="text"
            placeholder="Описание"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="w-full p-3 border rounded-lg mb-3"
            required
          />
          <button
            type="submit"
            disabled={status === 'sending'}
            className="w-full bg-blue-600 text-white p-3 rounded-lg hover:bg-blue-700"
          >
            {status === 'sending' ? 'Отправка...' : 'Отправить'}
          </button>
          {status === 'success' && (
            <p className="text-green-600 mt-2">✅ Заявка отправлена!</p>
          )}
          {status === 'error' && (
            <p className="text-red-600 mt-2">❌ Ошибка отправки. Попробуйте позже.</p>
          )}
        </form>
      </div>
    </div>
  );
}

export default SimpleLanding
