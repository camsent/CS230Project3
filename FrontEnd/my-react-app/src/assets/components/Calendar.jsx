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

 
function CalendarApp() {
   const [eventsService] = useState(() => createEventsServicePlugin());

  const [newEvent, setNewEvent] = useState({
    title: '',
    start: '',
    end: '',
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

  const handleAddEvent = () => {
    const { title, start, end } = newEvent;

    if (!title || !start || !end) {
      alert('Please enter title, start, and end.');
      return;
    }

    try {
      // Convert datetime-local string (e.g. "2025-10-26T18:30") → Temporal.ZonedDateTime
      const startPlain = Temporal.PlainDateTime.from(start.length === 16 ? `${start}:00` : start);
      const endPlain = Temporal.PlainDateTime.from(end.length === 16 ? `${end}:00` : end);

      // Use the local system time zone
      const tz = Temporal.Now.timeZoneId();
      const startZoned = startPlain.toZonedDateTime(tz);
      const endZoned = endPlain.toZonedDateTime(tz);

      const eventToAdd = {
        id: String(Date.now()),
        title,
        start: startZoned,
        end: endZoned,
      };

      eventsService.add(eventToAdd);
      console.log('Event added:', eventToAdd);

      // Tell calendar to refresh
      if (calendar.reloadEvents) {
        calendar.reloadEvents();
        console.log('Calendar reloaded');
      }

      // Reset form
      setNewEvent({ title: '', start: '', end: '' });
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
          type="datetime-local"
          value={newEvent.start}
          onChange={(e) => setNewEvent({ ...newEvent, start: e.target.value })}
          style={{ padding: '8px', borderRadius: '6px', border: '1px solid #ccc' }}
        />

        {/* end datetime */}
        <input
          type="datetime-local"
          value={newEvent.end}
          onChange={(e) => setNewEvent({ ...newEvent, end: e.target.value })}
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