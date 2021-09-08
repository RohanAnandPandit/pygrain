# pygrain
An application development framework built on the
Pygame library with integration for Tkinter windows.

You can install pygrain using
> pip install pygrain

## UI Components
There are several built-in UI components such as
- Frame
- Button
- Scroll Bar
- Slider
- Image
- Text Box  
- Point
- Tkinter Window

## Event Handling
Use the `bind` method on components to add an event handler for 
any combination of keyboard/mouse events

Mouse Events
- `left click`
- `left up`
- `right click`
- `right up`
- `middle click`
- `middle up`
- `scroll up`
- `scroll down`
- `mousemotion`

Special Events
- `always` - called on every loop

For example:

`component.bind('left click', lambda target: print('Hello World'))`

`component.bind({'left click', 'right click'}, 'm, lambda target: print('Hello World'))`

The event handler function should accept one argument for the calling component 
and should return a boolean depending on whether the event is valid or not
If `false` is returned then the event will be passed to lower level components.

Multiple event handlers can be added for the same set of events and all of them will
be called in the order they were added.
