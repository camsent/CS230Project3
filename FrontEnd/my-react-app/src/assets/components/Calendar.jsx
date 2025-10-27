import React, { useState, useEffect } from 'react';
import { useCalendarApp, ScheduleXCalendar } from '@schedule-x/react'
import {
  createViewDay,
  createViewMonthAgenda,
  createViewMonthGrid,
  createViewWeek,
} from '@schedule-x/calendar'
import { createEventsServicePlugin } from '@schedule-x/events-service'
import 'temporal-polyfill/global'
import '@schedule-x/theme-default/dist/index.css'

export const API_URL = 'http://127.0.0.1:8000' 

function CalendarApp() {
   const [eventsService] = useState(() => createEventsServicePlugin());

  const [newEvent, setNewEvent] = useState({
    title: '',
    dueDate: '',
  });

  const calendar = useCalendarApp({
    views: [
      createViewDay(),
      createViewWeek(),
      createViewMonthGrid(),
      createViewMonthAgenda(),
    ],
    events: [],
    plugins: [eventsService],
  });

  const handleAddEvent = async () => {
    const { title, dueDate} = newEvent;

    if (!title || !dueDate) {
      alert('Please enter title and due date');
      return;
    }

    try {
      const date = Temporal.PlainDate.from(dueDate);

      const eventToAdd = {
        id: String(Date.now()),
        title,
        start: date,
        end: date,
      };

      eventsService.add(eventToAdd);
      console.log('Event added:', eventToAdd);

      // Tell calendar to refresh
      if (calendar.reloadEvents) {
        calendar.reloadEvents();
        console.log('Calendar reloaded');
      }

      const dateString = date.toString();

      const response = await fetch(`${API_URL}/task/create`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include', // ✅ sends session cookie
        body: JSON.stringify({
        title: eventToAdd.title,
        start: dateString, // ✅ convert to string
      }),
    });


    if (!response.ok) throw new Error('Failed to send task');

    const data = await response.json();
    console.log('Task sent to backend:', data);

      // Reset form
      setNewEvent({ title: '', dueDate: ''});
    } catch (err) {
      console.error('Error adding event:', err);
      alert('Invalid date/time format. Check your start and end values.');
    }
  };

 
    return (
       <div
      style={{
        width: '90%',
        maxWidth: '1000px',
        margin: '40px auto',
        fontFamily: 'Arial, sans-serif',
      }}
    >
      <h1 style={{ textAlign: 'center', color: '#3b82f6' }}>Event Calendar</h1>

      {/* Add Event Form */}
      <div
        style={{
          display: 'flex',
          flexWrap: 'wrap',
          alignItems: 'center',
          gap: '10px',
          justifyContent: 'center',
          marginBottom: '20px',
        }}
      >
        <input
          type="text"
          placeholder="Event Title"
          value={newEvent.title}
          onChange={(e) => setNewEvent({ ...newEvent, title: e.target.value })}
          style={{ padding: '8px', borderRadius: '6px', border: '1px solid #ccc' }}
        />

        <input
          type="date"
          value={newEvent.dueDate}
          onChange={(e) => setNewEvent({ ...newEvent, dueDate: e.target.value })}
          style={{ padding: '8px', borderRadius: '6px', border: '1px solid #ccc' }}
        />

        <button
          onClick={handleAddEvent}
          style={{
            backgroundColor: '#3b82f6',
            color: 'white',
            border: 'none',
            padding: '8px 16px',
            borderRadius: '6px',
            cursor: 'pointer',
            fontWeight: 'bold',
          }}
        >
          Add Event
        </button>
      </div>
      <div
        style={{
          backgroundColor: 'white',
          borderRadius: '12px',
          boxShadow: '0 4px 10px rgba(0,0,0,0.1)',
          padding: '10px',
        }}
      >
        <ScheduleXCalendar calendarApp={calendar} />
      </div>
      </div>
    )
  }

 
export default CalendarApp;